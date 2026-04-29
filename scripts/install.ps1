param(
  [string]$CodexHome = "$HOME\.codex"
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$skillSource = Join-Path $repoRoot "skills\harmonyos-deveco"
$promptSource = Join-Path $repoRoot "prompts"
$skillTarget = Join-Path $CodexHome "skills\harmonyos-deveco"
$promptTarget = Join-Path $CodexHome "prompts"

if (-not (Test-Path $skillSource)) {
  throw "Missing skill source: $skillSource"
}

New-Item -ItemType Directory -Force -Path $skillTarget, $promptTarget | Out-Null
Copy-Item -Recurse -Force (Join-Path $skillSource "*") $skillTarget
Copy-Item -Force (Join-Path $promptSource "harmonyos-*.md") $promptTarget

Write-Output "Installed harmonyos-deveco skill to $skillTarget"
Write-Output "Installed harmonyos slash prompts to $promptTarget"
Write-Output "Restart or reopen Codex if slash prompts are not visible immediately."
