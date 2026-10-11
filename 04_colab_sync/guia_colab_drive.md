# 🚀 Conexión de Google Colab con Google Drive (Talento Tech - ML)

Carpeta vinculada en Google Drive:
- **Enlace web:** [Abrir carpeta en Google Drive](https://drive.google.com/drive/folders/1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd?usp=drive_link)
- **ID de Carpeta:** `1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd`

---

## 📌 Opción 1: Montar Google Drive en Colab (Recomendada)

Copia y pega este bloque de código al inicio de cualquier cuaderno de Google Colab:

```python
# 1. Montar Google Drive
from google.colab import drive
import os
from pathlib import Path

drive.mount('/content/drive')

# 2. Configurar ruta de trabajo
# Si creaste un acceso directo en 'Mi unidad' con el nombre 'Talento Tech - ML':
drive_workspace = Path('/content/drive/MyDrive/Talento Tech - ML')

# Si no existe la carpeta, la crea automáticamente en tu Drive:
drive_workspace.mkdir(parents=True, exist_ok=True)
os.chdir(drive_workspace)

print(f"✅ Entorno listo. Directorio actual de trabajo: {os.getcwd()}")
print("📁 Archivos disponibles:")
print(os.listdir(drive_workspace))
```

> **💡 Consejo importante para Google Colab:**
> Para ver esta carpeta directamente en `/content/drive/MyDrive/`:
> 1. Abre el enlace de la carpeta en tu navegador: [Carpeta Drive](https://drive.google.com/drive/folders/1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd?usp=drive_link)
> 2. Haz clic en el título de la carpeta > **"Organizar"** > **"Agregar acceso directo"**.
> 3. Elige **"Mi unidad"** y confirma. ¡Así Colab podrá leerla y guardar allí directamente!

---

## 📌 Opción 2: Sincronización Automática desde tu PC

Desde tu máquina local tienes los siguientes scripts listos en `04_colab_sync/`:

1. **`autenticar_drive.bat`**: Ejecútalo para abrir el navegador e iniciar sesión con tu cuenta de Google. Esto renueva el token para el servidor MCP y los scripts de sincronización.
2. **`sincronizar_todo.bat`**: Sube automáticamente todo lo que tengas en `01_clases/`, `02_proyectos/` y `03_recursos/` a la carpeta de Google Drive.
3. **Línea de comandos (PowerShell)**:
   ```powershell
   # Ver archivos en Drive
   python 04_colab_sync/drive_manager.py --list

   # Subir un notebook específico
   python 04_colab_sync/drive_manager.py --upload "01_clases/clase_01_intro.ipynb"

   # Sincronizar todo el espacio de trabajo
   python 04_colab_sync/drive_manager.py --sync-workspace
   ```
