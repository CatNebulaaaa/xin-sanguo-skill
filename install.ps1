param(
    [ValidateSet("all", "codex", "claude", "openclaw", "hermes", "agents")]
    [string]$Target = "all"
)

$ErrorActionPreference = "Stop"

$SkillName = "xin-sanguo-chat"
$Source = Join-Path $PSScriptRoot $SkillName

if (-not (Test-Path (Join-Path $Source "SKILL.md"))) {
    throw "Cannot find $SkillName/SKILL.md. Run this installer from the repository root."
}

function Install-Skill {
    param(
        [string]$Root
    )

    $Destination = Join-Path $Root $SkillName
    New-Item -ItemType Directory -Force -Path $Destination | Out-Null
    Copy-Item -Path (Join-Path $Source "*") -Destination $Destination -Recurse -Force
    Write-Host "Installed $SkillName -> $Destination"
}

$Targets = switch ($Target) {
    "all" {
        @(
            Join-Path $HOME ".codex\skills"
            Join-Path $HOME ".claude\skills"
            Join-Path $HOME ".openclaw\skills"
            Join-Path $HOME ".hermes\skills"
        )
    }
    "codex" { @(Join-Path $HOME ".codex\skills") }
    "claude" { @(Join-Path $HOME ".claude\skills") }
    "openclaw" { @(Join-Path $HOME ".openclaw\skills") }
    "hermes" { @(Join-Path $HOME ".hermes\skills") }
    "agents" { @(Join-Path $HOME ".agents\skills") }
}

foreach ($Root in $Targets) {
    Install-Skill -Root $Root
}
