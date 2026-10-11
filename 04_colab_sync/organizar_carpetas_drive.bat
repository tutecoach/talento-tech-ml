@echo off
chcp 65001 > nul
echo ========================================================
echo   Organizador de Archivos y Subcarpetas en Google Drive
echo   Carpeta ID: 1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd
echo ========================================================
echo.
echo Clasificando y moviendo archivos a:
echo  1. 01_Clases
echo  2. 02_Ejercicios_y_Practicas
echo  3. 03_Proyectos_y_Entregables
echo  4. 04_Colab_Notebooks
echo  5. 05_Datasets_y_Recursos
echo  6. 06_Material_Adicional
echo.
python "%~dp0drive_manager.py" --organize-files
echo.
pause
