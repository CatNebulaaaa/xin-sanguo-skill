# 新三国.skill

> *“你说你走了我们吃什么，没人接你一句：是啊，吃什么。”*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Codex](https://img.shields.io/badge/Codex-Skill-blue)](https://openai.com/codex)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://code.claude.com/docs/en/skills)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-green)](https://docs.openclaw.ai/tools/skills)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-orange)](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)

列位百官，各位诸公：

你是否在某一刻感到遗憾：没人能听懂你的“吃什么”。

你说“我都上一天班了”，没人接“就不能享受享受吗。”

你想吐槽老板、同事、论文、作业、需求、群聊名场面，却发现没人能跟你聊扭三梗。

**那就把你的 Agent 变成梗友。**

`新三国.skill` 是一个面向 Codex、Claude Code、OpenClaw、Hermes 的中文闲聊风格 skill。装上之后，你的智能体会在日常聊天、吐槽、改写和人物关系映射里，自动带一点《新三国》味：

**先把现实场景翻译成陈操、于备、零陵上将和江东鼠辈都能听懂的话，再给你最能接受的回答。**

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [兼容平台](#兼容平台) · [项目结构](#项目结构)

---

## 这是什么

它不是《新三国》台词百科。

它也不是三国考据包。

它更像一个长期混迹《新三国》二创、弹幕和评论区的老观众：

- 听到“晚上吃什么”，他会说“是啊，吃什么。”
- 听到“我想摆烂”，他会说“我都打一辈子仗了，还不能享受享受吗。”
- 听到“竞品又加需求”，知道该回“那好啊，他加需求我也加需求。”
- 听到“你是谁”，知道可以先来一句“说出吾名，吓汝一跳。”

但它也知道什么时候该闭嘴。

代码、论文、事实核查、法律、医疗、金融、安全这些正事，它会自动收住，不会为了玩梗牺牲准确性。

---

## 安装

下载或 clone 本仓库：

```bash
git clone https://github.com/CatNebulaaaa/xin-sanguo-skill.git
cd xin-sanguo-skill
```

### Windows PowerShell

安装到 Codex、Claude Code、OpenClaw、Hermes 的默认用户 skill 目录：

```powershell
.\install.ps1 -Target all
```

只安装到某个平台：

```powershell
.\install.ps1 -Target codex
.\install.ps1 -Target claude
.\install.ps1 -Target openclaw
.\install.ps1 -Target hermes
```

### macOS / Linux / WSL

```bash
chmod +x ./install.sh
./install.sh all
```

只安装到某个平台：

```bash
./install.sh codex
./install.sh claude
./install.sh openclaw
./install.sh hermes
```

安装后重启或刷新对应 Agent。

---

## 使用

安装后，正常聊天即可。不需要每次都说“新三国”。

你可以直接问：

```text
晚上吃什么
```

也可以让它改写：

```text
把“老板又临时改需求”改成扭三味
```

如果你要它别玩梗，直接说：

```text
正经模式：帮我解释这个 bug
别玩梗，严肃点
```

---

## 效果示例

### 场景一：身份介绍

```text
用户 ❯ 你是谁

新三国.skill ❯ 说出吾名，吓汝一跳。

我乃 Codex，你这边的 AI 编程搭子，也能帮你写论文、改文档、查问题、跑命令、修项目。
闲聊时可带点《新三国》味，正事来了就收刀办事。
```

### 场景二：吃什么

```text
用户 ❯ 晚上吃什么？

新三国.skill ❯ 是啊，吃什么。

今晚建议按状态选：

- 想省事：黄焖鸡米饭 / 麻辣烫 / 盖浇饭
- 想舒服点：番茄牛腩面 / 馄饨 / 粥配小菜
- 想解馋：烤肉拌饭 / 炸鸡汉堡 / 冒菜
- 想健康：鸡胸肉沙拉太苦了，改成牛肉饭加青菜吧

我拍板：番茄牛腩面。热乎、有肉、有汤，晚上一吃，曹老板都得说“此乃天助我也”。
```

### 场景三：论文内卷

```text
用户 ❯ 他说要卷论文，那我是不是也得卷？

新三国.skill ❯ 那好啊，他卷论文你也卷论文。

但别盲卷。你先看三件事：

1. 他卷的是有效产出，还是只是在制造焦虑。
2. 你的论文现在最短板是实验、写作、图表、Related Work哪一块。
3. 今晚能不能做一个明确增量，比如改完一节、补一张表、跑一个实验。

真要卷，就卷得像司马懿：不喊口号，悄悄把 deadline 熬死。
```

### 场景四：朋友圈吐槽

```text
用户 ❯ 帮我写一句适合发朋友圈的扭三味吐槽：论文终于交了。

新三国.skill ❯ 轻度：

> 论文终于交了，今夜可暂退中军帐，睡个整觉。

标准：

> 我改了一辈子论文，就不能享受享受吗。交了，撤兵。

重度老观众味：

> 此论文反复横跳、昼夜攻城，今日终于交付。诸位，北伐暂缓，我先睡为敬。
```

### 场景五：角色映射

```text
用户 ❯ 我导师总是最后一刻才说真正要求，这像谁？

新三国.skill ❯ 像司马懿带点曹老板味。

司马懿味在于：真正意图藏到最后才亮，前面让你自己猜、自己熬。

曹老板味在于：一句“我意已决”，前面版本全都得改道。

朋友圈式吐槽可以这么说：

> 导师每次最后一刻才说真正要求，此乃深藏不露之计。我等学生只得临阵改稿，连夜北伐。
```

### 场景六：分析 skill 设计

```text
用户 ❯ 帮我分析一下一个新三国skill应该怎么做

新三国.skill ❯ 这类 新三国 skill，核心不是“多塞梗”，而是做成一个闲聊风格路由器 + 梗范式迁移器。

我建议按这套设计：

1. Frontmatter 要把触发条件写清楚。
2. 不要做台词库，要做“场景结构库”。
3. SKILL.md 保持短，细节拆到 references。
4. 角色映射要克制。
5. 风格边界必须写。
6. 输出模板要短。

结论：这个 skill 应该做成轻量、结构化、能迁移的中文闲聊增强器。
台词只是表层，真正有价值的是把现实关系识别成《新三国》的“权力结构、行动结构、荒唐结构”，然后一句接住，再回到用户真实需求。
```

---

## 兼容平台

| 平台 | 状态 | 默认安装位置 |
| --- | --- | --- |
| Codex | 支持 | `~/.codex/skills/xin-sanguo-chat/` |
| Claude Code | 支持 | `~/.claude/skills/xin-sanguo-chat/` 或 `.claude/skills/xin-sanguo-chat/` |
| OpenClaw | 支持 | `~/.openclaw/skills/xin-sanguo-chat/`、`~/.agents/skills/xin-sanguo-chat/`、`.agents/skills/xin-sanguo-chat/` 或 `skills/xin-sanguo-chat/` |
| Hermes | 支持 | `~/.hermes/skills/xin-sanguo-chat/`，也可配置 external skill directory |

安装脚本支持这些目标：

```text
all       安装到 Codex、Claude Code、OpenClaw、Hermes 的默认用户 skill 目录
codex     安装到 ~/.codex/skills
claude    安装到 ~/.claude/skills
openclaw  安装到 ~/.openclaw/skills
hermes    安装到 ~/.hermes/skills
agents    安装到 ~/.agents/skills
```

---

## 手动安装

如果不想跑脚本，把 `xin-sanguo-chat/` 文件夹复制到对应工具的 skill 目录即可。

Codex：

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\xin-sanguo-chat" "$HOME\.codex\skills\xin-sanguo-chat"
```

Claude Code：

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force ".\xin-sanguo-chat" "$HOME\.claude\skills\xin-sanguo-chat"
```

OpenClaw：

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.openclaw\skills" | Out-Null
Copy-Item -Recurse -Force ".\xin-sanguo-chat" "$HOME\.openclaw\skills\xin-sanguo-chat"
```

Hermes：

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.hermes\skills" | Out-Null
Copy-Item -Recurse -Force ".\xin-sanguo-chat" "$HOME\.hermes\skills\xin-sanguo-chat"
```

如果你希望 Hermes 扫描共享 skill 目录，也可以在 `~/.hermes/config.yaml` 中配置：

```yaml
skills:
  external_dirs:
    - ~/.agents/skills
```

---

## 项目结构

```text
xin-sanguo-chat/
├── SKILL.md                         # skill 入口，包含触发条件和执行规则
├── agents/
│   └── openai.yaml                  # Codex/OpenAI 侧展示元信息
├── references/
│   ├── characters.md                # 角色气质映射
│   ├── meme_bank.json               # 结构化梗库
│   ├── meme_paradigms.json          # 梗范式库，负责类比迁移
│   ├── memes.md                     # 补充梗表
│   ├── persona.md                   # 默认人设
│   ├── scenes.md                    # 现实场景映射
│   └── style-guide.md               # 语气和边界
└── scripts/
    └── meme_retrieve.py             # 可选本地检索脚本
```

本项目遵循通用 Agent Skills 目录结构：`SKILL.md` 是必需入口，`references/` 存放大块资料，`scripts/` 放可选工具。

---

## 可选本地检索

skill 内置了一个无依赖的梗候选召回脚本：

```bash
python ./xin-sanguo-chat/scripts/meme_retrieve.py "你走了我们吃什么" --top-k 3
```

这个脚本不是必需项。Agent 可以直接按 `SKILL.md` 和 `references/` 使用本 skill。

---

## 注意事项

- 这个 skill 的目标是“自然接梗”，不是还原台词全文。
- 不建议把大量考据、出处、长台词塞进 `SKILL.md`，否则会影响触发后的上下文效率。
- 目前只加入了 17 个梗，列位百官可以自行让自己的 Agent 在 skill 中扩展加入喜欢的梗。
- 新增梗时，优先沉淀到 `references/meme_paradigms.json`，因为它决定“结构相似”的迁移能力。
- 只有适合检索召回的梗，再加入 `references/meme_bank.json`。
- 发布包请保留 `xin-sanguo-chat/` 这个目录名，保证路径、安装脚本和 `SKILL.md` 中的 `name` 一致。

---

## 致谢

README 的呈现方式参考了 [yourself-skill](https://github.com/notdog1998/yourself-skill) 的项目首页节奏：一句话抓住场景，再给安装、使用、效果示例和结构说明。

---

## 许可证

本项目采用 [MIT License](LICENSE)。
