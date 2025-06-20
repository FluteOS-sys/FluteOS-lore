# FluteOS Core Push Setup Script
# Author: Vincent Cricelli
# Date: 2025-06-19

# ----------------------------------------
# Disable default background Windows bloat
# ----------------------------------------
Get-Service *diagnostic* | Stop-Service -Force -ErrorAction SilentlyContinue
Set-Service "DiagTrack" -StartupType Disabled
Set-Service "dmwappushservice" -StartupType Disabled

# ----------------------------------------
# Install Core Dev Utilities with Chocolatey
# ----------------------------------------
choco install python --pre -y
choco install git -y
choco install pycharm-community -y
choco install obsidian -y
choco install everything -y
choco install powertoys -y

# ----------------------------------------
# Optional Tools (add when needed)
# ----------------------------------------
# choco install autoruns -y
# choco install vscode -y
# choco install anaconda -y

Write-Host "`n✅ FluteOS Core Dev Environment Setup Complete.`n" -ForegroundColor Green
