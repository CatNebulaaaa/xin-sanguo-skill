# xin-sanguo-chat

一个面向 Codex、Claude Code、OpenClaw 和 Hermes 的《新三国》闲聊风格 Agent Skill。

它不是台词百科，也不是三国考据包。核心目标是让 Agent 在中文闲聊、吐槽、轻松改写和关系映射里，先判断现实语境的关系结构和情绪，再自然迁移一点《新三国》梗味。

## Compatibility

| Platform | Status | Install location |
| --- | --- | --- |
| Codex | Supported | `~/.codex/skills/xin-sanguo-chat/` |
| Claude Code | Supported | `~/.claude/skills/xin-sanguo-chat/` or `.claude/skills/xin-sanguo-chat/` |
| OpenClaw | Supported | `~/.openclaw/skills/xin-sanguo-chat/`, `~/.agents/skills/xin-sanguo-chat/`, `.agents/skills/xin-sanguo-chat/`, or `skills/xin-sanguo-chat/` |
| Hermes | Supported | `~/.hermes/skills/xin-sanguo-chat/` or an external skill directory configured in `~/.hermes/config.yaml` |

The packaged skill directory is:

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

This follows the common Agent Skills layout: a required `SKILL.md` with YAML frontmatter, plus optional `references/`, `scripts/`, and platform metadata under `agents/`.

## Install

Download or clone this repository, then run one of the installers from the repository root.

Windows PowerShell:

```powershell
.\install.ps1 -Target all
```

macOS, Linux, or WSL:

```bash
chmod +x ./install.sh
./install.sh all
```

Supported installer targets:

```text
all       install to Codex, Claude Code, OpenClaw, and Hermes default user skill dirs
codex     install to ~/.codex/skills
claude    install to ~/.claude/skills
openclaw  install to ~/.openclaw/skills
hermes    install to ~/.hermes/skills
agents    install to ~/.agents/skills
```

Examples:

```powershell
.\install.ps1 -Target claude
.\install.ps1 -Target hermes
```

```bash
./install.sh codex
./install.sh agents
```

## Manual Install

Copy the `xin-sanguo-chat/` folder into the skill directory for your tool.

Codex:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\xin-sanguo-chat" "$HOME\.codex\skills\xin-sanguo-chat"
```

Claude Code:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force ".\xin-sanguo-chat" "$HOME\.claude\skills\xin-sanguo-chat"
```

OpenClaw:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.openclaw\skills" | Out-Null
Copy-Item -Recurse -Force ".\xin-sanguo-chat" "$HOME\.openclaw\skills\xin-sanguo-chat"
```

Hermes:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.hermes\skills" | Out-Null
Copy-Item -Recurse -Force ".\xin-sanguo-chat" "$HOME\.hermes\skills\xin-sanguo-chat"
```

Hermes can also scan shared skill directories. Add this to `~/.hermes/config.yaml` if you prefer a shared location:

```yaml
skills:
  external_dirs:
    - ~/.agents/skills
```

## Test

Restart the target agent after installation, then try:

```text
晚上吃什么
我都上一天班了，想摆烂
把“老板又临时改需求”改成新三国味
正经模式：帮我解释这个 bug
```

Expected behavior:

- Casual Chinese chat and complaints get a short, fitting Xin Sanguo-flavored line before the practical answer.
- Rewrite requests return several short versions.
- Serious technical, academic, legal, medical, financial, safety, and fact-checking tasks stay restrained or exit the meme style.

## Optional Local Retrieval

The skill includes a dependency-free helper script for local candidate retrieval:

```bash
python ./xin-sanguo-chat/scripts/meme_retrieve.py "你走了我们吃什么" --top-k 3
```

The script is optional. Agents can use the reference files directly without running it.

## Publishing Notes

For GitHub releases, include the repository as-is. Users can install from a ZIP download or a `git clone` with the installer scripts above.

Keep the distributable skill folder named `xin-sanguo-chat` so GitHub paths, slash commands, and platform installers stay ASCII and match the `name` in `SKILL.md`.

## References

- Claude Code Skills: https://code.claude.com/docs/en/skills
- Claude Skill authoring best practices: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- OpenClaw Skills: https://docs.openclaw.ai/tools/skills
- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
