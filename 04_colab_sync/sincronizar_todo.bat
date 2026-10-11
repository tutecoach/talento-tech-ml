@echo off
chcp 65001 > nul
echo ========================================================
echo   Sincronizando Workspace con Google Drive
echo   Carpeta ID: 1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd
echo ========================================================
echo.
python "%~dp0drive_manager.py" --sync-workspace
echo.
pause
