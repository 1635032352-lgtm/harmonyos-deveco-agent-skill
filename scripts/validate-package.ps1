$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

$requiredFiles = @(
  ".codex-plugin\plugin.json",
  "README.md",
  ".gitignore",
  "skills\harmonyos-deveco\SKILL.md",
  "skills\harmonyos-deveco\agents\openai.yaml",
  "skills\harmonyos-deveco\scripts\search_docs.py",
  "skills\harmonyos-deveco\scripts\build_local_index.py",
  "prompts\harmonyos-ideal.md",
  "prompts\harmonyos-ux.md",
  "prompts\harmonyos-system.md",
  "prompts\harmonyos-arkui.md",
  "prompts\harmonyos-implement.md",
  "prompts\harmonyos-verify.md",
  "prompts\harmonyos-report.md",
  "prompts\harmonyos-fix.md",
  "prompts\harmonyos-contest.md",
  "prompts\harmonyos-all.md"
)

$missing = @()
foreach ($file in $requiredFiles) {
  $path = Join-Path $repoRoot $file
  if (-not (Test-Path $path)) {
    $missing += $file
  }
}

$commands = @(
  "/harmonyos-ideal",
  "/harmonyos-ux",
  "/harmonyos-system",
  "/harmonyos-arkui",
  "/harmonyos-implement",
  "/harmonyos-verify",
  "/harmonyos-report",
  "/harmonyos-fix",
  "/harmonyos-contest",
  "/harmonyos-all"
)

$skillText = Get-Content -Raw (Join-Path $repoRoot "skills\harmonyos-deveco\SKILL.md")
$agentText = Get-Content -Raw (Join-Path $repoRoot "skills\harmonyos-deveco\agents\openai.yaml")
$missingCommands = @()
foreach ($command in $commands) {
  if (($skillText -notmatch [regex]::Escape($command)) -or ($agentText -notmatch [regex]::Escape($command))) {
    $missingCommands += $command
  }
}

$generatedFiles = @(
  "skills\harmonyos-deveco\references\docs.sqlite",
  "skills\harmonyos-deveco\references\docs-index.jsonl"
)

$bundledGenerated = @()
foreach ($file in $generatedFiles) {
  if (Test-Path (Join-Path $repoRoot $file)) {
    $bundledGenerated += $file
  }
}

if ($missing.Count -or $missingCommands.Count -or $bundledGenerated.Count) {
  Write-Output "PACKAGE_CHECK FAIL"
  if ($missing.Count) {
    Write-Output "Missing files:"
    $missing | ForEach-Object { Write-Output "  $_" }
  }
  if ($missingCommands.Count) {
    Write-Output "Missing command references:"
    $missingCommands | ForEach-Object { Write-Output "  $_" }
  }
  if ($bundledGenerated.Count) {
    Write-Output "Generated files should not be committed:"
    $bundledGenerated | ForEach-Object { Write-Output "  $_" }
  }
  exit 1
}

Write-Output "PACKAGE_CHECK PASS"
