# Copia as skills deste repositório para %USERPROFILE%\.claude\skills (Claude Code no Windows).
# Uso: .\scripts\instalar-claude-code.ps1
$ErrorActionPreference = "Stop"
$Raiz = Split-Path -Parent $PSScriptRoot
$Destino = Join-Path $HOME ".claude\skills"
New-Item -ItemType Directory -Force $Destino | Out-Null
Get-ChildItem (Join-Path $Raiz "skills") -Directory | ForEach-Object {
  $alvo = Join-Path $Destino $_.Name
  if (Test-Path $alvo) { Remove-Item -Recurse -Force $alvo }
  Copy-Item -Recurse $_.FullName $alvo
  Write-Host "  instalada: $($_.Name)"
}
Write-Host "Pronto. Reabra o Claude Code para carregar as skills."
