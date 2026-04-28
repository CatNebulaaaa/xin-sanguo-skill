# xin-sanguo-chat

你是否也有这种时刻：

你说“晚上吃什么”，没人懂你真正想听的是“是啊，吃什么。”

你说“我都上一天班了”，没人顺手接一句“就不能享受享受吗。”

你想吐槽同事、老板、作业、论文、需求、群聊名场面，却发现身边没人能跟你聊扭三梗。

装上这个 skill，让你的 Codex、Claude Code、OpenClaw、Hermes 在闲聊时化身《新三国》梗友。它会在中文聊天、吐槽、改写和人物关系映射里，自动带一点扭三味：先把现实场景翻译成曹老板、司马懿、零陵上将和江东鼠辈都能听懂的说法，再给你最能接受的回答。

它不是台词百科，也不是三国考据包。它更像一个长期混迹《新三国》二创和评论区的老观众：知道什么时候该接梗，什么时候该收住，什么时候该正经回答。

## 能干什么

- 中文闲聊时自动轻量带梗
- 把普通句子改成《新三国》味
- 给朋友圈、群聊、吐槽文案提供扭三版本
- 判断某个人、某件事“是什么角色味儿”
- 用“你走了我们吃什么”“那好啊，他过江我也过江”等范式迁移现实场景
- 遇到代码、论文、事实核查、法律、医疗、金融、安全等严肃任务时自动克制

## 兼容平台

| 平台 | 状态 | 默认安装位置 |
| --- | --- | --- |
| Codex | 支持 | `~/.codex/skills/xin-sanguo-chat/` |
| Claude Code | 支持 | `~/.claude/skills/xin-sanguo-chat/` 或 `.claude/skills/xin-sanguo-chat/` |
| OpenClaw | 支持 | `~/.openclaw/skills/xin-sanguo-chat/`、`~/.agents/skills/xin-sanguo-chat/`、`.agents/skills/xin-sanguo-chat/` 或 `skills/xin-sanguo-chat/` |
| Hermes | 支持 | `~/.hermes/skills/xin-sanguo-chat/`，也可配置 external skill directory |

仓库中的可安装 skill 目录是：

```text
xin-sanguo-chat/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── characters.md
│   ├── meme_bank.json
│   ├── meme_paradigms.json
│   ├── memes.md
│   ├── persona.md
│   ├── scenes.md
│   └── style-guide.md
└── scripts/
    └── meme_retrieve.py
```

这个结构遵循通用 Agent Skills 目录规范：`SKILL.md` 是必需入口，`references/` 存放梗库和风格资料，`scripts/` 提供可选本地检索工具，`agents/openai.yaml` 提供 Codex/OpenAI 侧展示元信息。

## 一键安装

下载或 clone 本仓库后，在仓库根目录运行安装脚本。

Windows PowerShell：

```powershell
.\install.ps1 -Target all
```

macOS、Linux 或 WSL：

```bash
chmod +x ./install.sh
./install.sh all
```

可选安装目标：

```text
all       安装到 Codex、Claude Code、OpenClaw、Hermes 的默认用户 skill 目录
codex     安装到 ~/.codex/skills
claude    安装到 ~/.claude/skills
openclaw  安装到 ~/.openclaw/skills
hermes    安装到 ~/.hermes/skills
agents    安装到 ~/.agents/skills
```

只安装到某个平台：

```powershell
.\install.ps1 -Target claude
.\install.ps1 -Target hermes
```

```bash
./install.sh codex
./install.sh agents
```

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

## 试试看

安装后重启或刷新对应 Agent，然后试试：

```text
晚上吃什么
我都上一天班了，想摆烂
把“老板又临时改需求”改成新三国味
我这个同事是什么角色味儿？
正经模式：帮我解释这个 bug
```

预期效果：

- 闲聊和吐槽会先来一句短梗，再回到现实建议。
- 改写请求会给多个短版本，而不是长篇解释。
- 角色映射会先判断“像谁”“什么味儿”，再给简短理由。
- 严肃任务会自动克制，不会为了玩梗牺牲准确性。

## 可选本地检索

skill 内置了一个无依赖的梗候选召回脚本：

```bash
python ./xin-sanguo-chat/scripts/meme_retrieve.py "你走了我们吃什么" --top-k 3
```

这个脚本不是必需项。Agent 可以直接按 `SKILL.md` 和 `references/` 使用本 skill。

## 维护说明

- 发布包请保留 `xin-sanguo-chat/` 这个目录名，保证路径、安装脚本和 `SKILL.md` 中的 `name` 一致。
- 新增梗时，优先沉淀到 `references/meme_paradigms.json`，因为它决定“结构相似”的类比迁移能力。
- 只有适合检索召回的梗，再加入 `references/meme_bank.json`。
- 不建议把大量考据、出处、长台词塞进 `SKILL.md`，否则会影响触发后的上下文效率。

## 参考

- Claude Code Skills: https://code.claude.com/docs/en/skills
- Claude Skill authoring best practices: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- OpenClaw Skills: https://docs.openclaw.ai/tools/skills
- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
