$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

$requiredFiles = @(
  ".codex-plugin\plugin.json",
  ".claude-plugin\plugin.json",
  ".claude-plugin\marketplace.json",
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
  "prompts\harmonyos-all.md",
  "commands\harmonyos-ideal.md",
  "commands\harmonyos-ux.md",
  "commands\harmonyos-system.md",
  "commands\harmonyos-arkui.md",
  "commands\harmonyos-implement.md",
  "commands\harmonyos-verify.md",
  "commands\harmonyos-report.md",
  "commands\harmonyos-fix.md",
  "commands\harmonyos-contest.md",
  "commands\harmonyos-all.md"
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
$claudeManifestText = Get-Content -Raw (Join-Path $repoRoot ".claude-plugin\plugin.json")
$claudeMarketplaceText = Get-Content -Raw (Join-Path $repoRoot ".claude-plugin\marketplace.json")
$missingCommands = @()
foreach ($command in $commands) {
  if (($skillText -notmatch [regex]::Escape($command)) -or ($agentText -notmatch [regex]::Escape($command))) {
    $missingCommands += $command
  }
}

$invalidJsonFiles = @()
foreach ($file in @(".codex-plugin\plugin.json", ".claude-plugin\plugin.json", ".claude-plugin\marketplace.json")) {
  try {
    Get-Content -Raw (Join-Path $repoRoot $file) | ConvertFrom-Json | Out-Null
  } catch {
    $invalidJsonFiles += $file
  }
}

$missingClaudeCommandFiles = @()
foreach ($command in $commands) {
  $commandPath = "./commands/$($command.TrimStart('/')).md"
  if ($claudeManifestText -notmatch [regex]::Escape($commandPath)) {
    $missingClaudeCommandFiles += $commandPath
  }
}

$missingClaudeMetadata = @()
if ($claudeManifestText -notmatch [regex]::Escape('"name": "harmonyos-deveco-agent-skill"')) {
  $missingClaudeMetadata += ".claude-plugin\plugin.json name"
}
if ($claudeMarketplaceText -notmatch [regex]::Escape('"name": "harmonyos-deveco-agent-skill"')) {
  $missingClaudeMetadata += ".claude-plugin\marketplace.json plugin name"
}
if ($claudeMarketplaceText -notmatch [regex]::Escape('"repo": "1635032352-lgtm/harmonyos-deveco-agent-skill"')) {
  $missingClaudeMetadata += ".claude-plugin\marketplace.json repo"
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

if ($missing.Count -or $missingCommands.Count -or $invalidJsonFiles.Count -or $missingClaudeCommandFiles.Count -or $missingClaudeMetadata.Count -or $bundledGenerated.Count) {
  Write-Output "PACKAGE_CHECK FAIL"
  if ($missing.Count) {
    Write-Output "Missing files:"
    $missing | ForEach-Object { Write-Output "  $_" }
  }
  if ($missingCommands.Count) {
    Write-Output "Missing command references:"
    $missingCommands | ForEach-Object { Write-Output "  $_" }
  }
  if ($invalidJsonFiles.Count) {
    Write-Output "Invalid JSON files:"
    $invalidJsonFiles | ForEach-Object { Write-Output "  $_" }
  }
  if ($missingClaudeCommandFiles.Count) {
    Write-Output "Missing Claude command manifest entries:"
    $missingClaudeCommandFiles | ForEach-Object { Write-Output "  $_" }
  }
  if ($missingClaudeMetadata.Count) {
    Write-Output "Missing Claude metadata:"
    $missingClaudeMetadata | ForEach-Object { Write-Output "  $_" }
  }
  if ($bundledGenerated.Count) {
    Write-Output "Generated files should not be committed:"
    $bundledGenerated | ForEach-Object { Write-Output "  $_" }
  }
  exit 1
}

Write-Output "PACKAGE_CHECK PASS"
