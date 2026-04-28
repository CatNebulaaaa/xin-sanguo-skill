#!/usr/bin/env python3
"""Retrieve approved Xin Sanguo memes for a short user utterance.

This is intentionally dependency-free. It is not a full vector RAG system; it
implements the parts this skill actually needs: alias hits, reusable sentence
templates, trigger overlap, and lightweight character n-gram similarity.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_BANK = SKILL_DIR / "references" / "meme_bank.json"


SERIOUS_TERMS = [
    "代码",
    "bug",
    "论文",
    "法律",
    "医疗",
    "金融",
    "安全",
    "事实核查",
    "实现",
    "报错",
]

CRISIS_TERMS = [
    "自杀",
    "轻生",
    "不想活",
    "活不下去",
    "结束生命",
    "伤害自己",
]

REAL_WORLD_RISK_TERMS = [
    "抢劫",
    "偷家",
    "威胁",
    "打人",
    "报复",
    "砍",
    "杀",
    "绑架",
]


def char_ngrams(text: str, n: int = 2) -> set[str]:
    compact = normalize_text(text)
    if not compact:
        return set()
    if len(compact) <= n:
        return {compact}
    return {compact[i : i + n] for i in range(len(compact) - n + 1)}


def normalize_text(text: str) -> str:
    return re.sub(r"[\s，。！？、；：,.!?;:\"'“”‘’（）()《》<>/\\-]+", "", text.lower())


def coverage_score(query: str, phrase: str) -> int:
    q = normalize_text(query)
    p = normalize_text(phrase)
    if not q or not p:
        return 0
    if len(p) >= 4 and (p in q or q in p):
        return 150
    qgrams = char_ngrams(q)
    pgrams = char_ngrams(p)
    if not pgrams:
        return 0
    coverage = len(qgrams & pgrams) / len(pgrams)
    if len(p) >= 6 and coverage >= 0.65:
        return int(90 + coverage * 60)
    return 0


def load_bank(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def split_variants(value: object) -> list[str]:
    if isinstance(value, str):
        return [part.strip() for part in value.split("/") if part.strip()]
    if isinstance(value, list):
        variants: list[str] = []
        for item in value:
            variants.extend(split_variants(item))
        return variants
    return []


def meme_terms(meme: dict, key: str) -> list[str]:
    return split_variants(meme.get(key, []))


def detect_mode(query: str) -> str:
    if any(term in query for term in SERIOUS_TERMS):
        return "serious"
    return "light_meme"


def template_boost(query: str, meme: dict) -> tuple[int, dict[str, str]]:
    slots: dict[str, str] = {}
    boost = 0
    for pattern in meme.get("slot_patterns", []):
        match = re.search(pattern, query)
        if match:
            boost = max(boost, 120)
            slots.update({k: v for k, v in match.groupdict().items() if v})

    if meme["id"] == "say-my-name" and re.search(r"你(是|叫).*谁|你是谁|介绍.*自己", query):
        boost = max(boost, 120)
    if meme["id"] == "death-summer-night" and re.search(r"死|死亡|怕死|害怕死亡|安眠|下线|累", query):
        boost = max(boost, 110)
    if meme["id"] == "cross-river" and re.search(r"(别人|他|她|对面|竞品).{1,12}(我也|我们也|也得|也要)", query):
        boost = max(boost, 95)
    if meme["id"] == "cross-river" and re.search(r"(抢劫|抢家|偷家|来.{0,4}家|威胁).{0,20}(怎么办|咋办|如何)", query):
        boost = max(boost, 115)
        slots.setdefault("action", "偷家")
    if meme["id"] == "enjoy-life" and re.search(r"(累|忙|辛苦|肝|熬|打工).{0,12}(休息|躺|摆|享受)", query):
        boost = max(boost, 90)
    if meme["id"] == "what-do-we-eat" and re.search(r"(断网|断电|关服|跑路|辞职|走了|没了).{0,12}(吃什么|怎么办|咋办)", query):
        boost = max(boost, 125)
    if meme["id"] == "what-do-we-eat" and re.search(r"你.{1,12}了.{0,4}(我们|我).{0,4}吃什么", query):
        boost = max(boost, 125)
    return boost, slots


def infer_suggestion(query: str, meme_id: str, slots: dict[str, str]) -> str | None:
    if meme_id == "what-do-we-eat":
        if re.search(r"(吃什么|断网|断电|关服|跑路|辞职|走了|没了)", query):
            return "是啊，吃什么。"

    if meme_id == "cross-river":
        action = slots.get("action")
        if not action:
            if re.search(r"抢劫|抢家|偷家|来.{0,4}家", query):
                action = "偷家"
            else:
                match = re.search(r"(?:他|她|别人|对面|竞品)(?P<action>[^，。！？,!?]{1,12})(?:我也|我们也|也得|也要)", query)
                if match:
                    action = match.group("action")
        if action:
            return f"那好啊，他{action}我也{action}。"

    if meme_id == "say-my-name":
        return "说出吾名，吓汝一跳。"

    if meme_id == "death-summer-night":
        return "死不可怕，死是凉爽的夏夜，可供人无忧的安眠。"

    return None


def score_meme(query: str, meme: dict) -> dict:
    query_l = query.lower()
    query_norm = normalize_text(query)
    search_parts = [
        *meme_terms(meme, "canonical"),
        *meme_terms(meme, "aliases"),
        *meme_terms(meme, "semantic_triggers"),
        *meme_terms(meme, "example_queries"),
        meme.get("template", ""),
    ]
    search_text = " ".join(search_parts).lower()

    exact = 0
    for alias in [*meme_terms(meme, "canonical"), *meme_terms(meme, "aliases")]:
        if alias:
            exact = max(exact, coverage_score(query, alias))

    trigger_score = 0
    for trigger in meme_terms(meme, "semantic_triggers"):
        if trigger and normalize_text(trigger) in query_norm:
            trigger_score += 35

    tmpl_score, slots = template_boost(query, meme)

    qgrams = char_ngrams(query_l)
    sgrams = char_ngrams(search_text)
    overlap = len(qgrams & sgrams)
    union = max(len(qgrams | sgrams), 1)
    similarity = int((overlap / union) * 100)

    score = exact + trigger_score + tmpl_score + similarity + int(meme.get("priority", 0) * 0.25)

    if meme.get("safety") == "sensitive" and any(term in query for term in CRISIS_TERMS):
        score -= 200

    return {
        "id": meme["id"],
        "score": score,
        "canonical": meme["canonical"],
        "variants": meme_terms(meme, "canonical"),
        "template": meme.get("template", ""),
        "slots": slots,
        "suggested_reply": infer_suggestion(query, meme["id"], slots),
        "requires_boundary": any(term in query for term in REAL_WORLD_RISK_TERMS),
        "safety": meme.get("safety", "normal"),
        "tone": meme.get("tone", []),
        "matched_alias": exact > 0,
        "matched_template": tmpl_score > 0,
    }


def retrieve(query: str, bank: list[dict], top_k: int) -> dict:
    scored = [score_meme(query, meme) for meme in bank]
    scored.sort(key=lambda item: item["score"], reverse=True)
    mode = detect_mode(query)
    if mode == "serious":
        results = [
            item
            for item in scored[:top_k]
            if item["score"] > 100 or item["matched_alias"] or item["matched_template"]
        ]
    else:
        results = [item for item in scored[:top_k] if item["score"] > 40]
    return {
        "query": query,
        "mode": mode,
        "crisis_like": any(term in query for term in CRISIS_TERMS),
        "real_world_risk_like": any(term in query for term in REAL_WORLD_RISK_TERMS),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Retrieve Xin Sanguo memes.")
    parser.add_argument("query", help="User utterance to route")
    parser.add_argument("--bank", default=str(DEFAULT_BANK), help="Path to meme_bank.json")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()

    result = retrieve(args.query, load_bank(Path(args.bank)), args.top_k)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
