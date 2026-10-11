# ☁️ Sincronización con Google Drive y Google Colab

En esta sección gestionamos los enlaces, scripts y copias de seguridad de los cuadernos ejecutados en **Google Colab** y almacenados en **Google Drive**.

---

## 📂 Carpeta oficial vinculada en Google Drive

- **Enlace web:** [Google Drive - Talento Tech - ML](https://drive.google.com/drive/folders/1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd?usp=drive_link)
- **ID de la carpeta:** `1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd`

---

## 🛠️ Herramientas disponibles en este directorio

| Archivo | Función |
| :--- | :--- |
| [`drive_manager.py`](file:///c:/Users/n_e_o/IA/Talento%20Tech%20-%20ML/04_colab_sync/drive_manager.py) | Script principal para listar, subir, descargar y sincronizar carpetas contra Google Drive. |
| [`autenticar_drive.bat`](file:///c:/Users/n_e_o/IA/Talento%20Tech%20-%20ML/04_colab_sync/autenticar_drive.bat) | Lanzador rápido en Windows para abrir el navegador y autorizar el acceso con Google Drive. |
| [`sincronizar_todo.bat`](file:///c:/Users/n_e_o/IA/Talento%20Tech%20-%20ML/04_colab_sync/sincronizar_todo.bat) | Script para subir los contenidos de `01_clases/`, `02_proyectos/` y `03_recursos/` a Google Drive. |
| [`guia_colab_drive.md`](file:///c:/Users/n_e_o/IA/Talento%20Tech%20-%20ML/04_colab_sync/guia_colab_drive.md) | Guía paso a paso para montar Drive en Colab y configurar el auto-guardado de notebooks. |

---

## 🚀 Flujo de trabajo con Google Colab:

1. **Montar Google Drive en tu notebook de Colab:**
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
2. **Guardar modelos y cuadernos:**
   Al crear un acceso directo a la carpeta en "Mi unidad", tus notebooks pueden guardar datasets, checkpoints y reportes directamente en `Talento Tech - ML`.
3. **Sincronización bidireccional:**
   Usa `python 04_colab_sync/drive_manager.py --sync-workspace` para mantener tu repositorio local y Google Drive siempre al día.
