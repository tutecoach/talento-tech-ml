# 🔌 Estado y Configuración de Integraciones Externas

---

## 1. 📁 Google Drive (Servidor MCP `gdrive`) — ✅ CONECTADO Y OPERATIVO

Google Drive está completamente sincronizado. Se ha localizado e indexado el árbol de carpetas del curso:
- **Carpeta Principal:** `Machine learning` (ID: `1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd`)
- **Documento Clave:** `INFO MACHINE LEARNING` (Comisión #26240, ID Zoom, contactos docentes)
- **Subcarpetas Vinculadas:**
  - `01_Clases`: Teóricos y resúmenes en Markdown y PDF (Clases 01 a 06).
  - `02_Ejercicios_y_Practicas`: Ejercicios prácticos en PDF (Clases 01 a 06).
  - `03_Proyectos_y_Entregables`: Cuaderno de la preentrega (`Pre_entrega26.ipynb`).
  - `04_Colab_Notebooks`: Cuadernos interactivos de las clases (`Clase_5.ipynb`, `Clase_6.ipynb`, `Clase_8.ipynb`, etc.).

---

## 2. 📚 NotebookLM (Servidor MCP `notebooklm`) — ⏳ PENDIENTE DE REFRESCAR TOKENS

- **Diagnóstico actual:** Al realizar `notebook_list`, la API de Google responde con `RPC Error 16: Authentication expired`.
- **Causa técnica:** El archivo local de credenciales `C:\Users\n_e_o\.notebooklm-mcp\auth.json` contiene cookies que expiraron el 30/09.
- **Cómo dejarlo activo en 1 minuto:**
  1. **Opción A (Recomendada - CLI automático):**
     Cierra temporalmente Google Chrome y en una terminal ejecuta:
     ```bash
     python -m notebooklm_mcp.auth_cli
     ```
  2. **Opción B (Pegar Cookies desde DevTools):**
     - Abre [notebooklm.google.com](https://notebooklm.google.com/) en tu navegador habitual con tu cuenta activa.
     - Presiona `F12` (Herramientas de Desarrollador) -> ve a la pestaña **Network** (Red).
     - Haz un clic en cualquier libreta o recarga la página (`F5`).
     - Selecciona cualquier petición a `notebooklm.google.com`, busca en **Request Headers** el valor completo de `Cookie` y cópialo.
     - Ejecuta en terminal:
       ```bash
       python -m notebooklm_mcp.auth_cli --file
       ```
       O me pegas el string de cookies aquí y lo guardo de inmediato con `save_auth_tokens`.
