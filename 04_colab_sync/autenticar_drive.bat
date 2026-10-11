@echo off
chcp 65001 > nul
echo ========================================================
echo   Autenticación de Google Drive - Talento Tech ML
echo ========================================================
echo.
echo Se abrirá tu navegador para iniciar sesión con Google.
echo Acepta los permisos de Google Drive para autorizar la sincronización.
echo.
python "%~dp0drive_manager.py" --auth
echo.
pause
