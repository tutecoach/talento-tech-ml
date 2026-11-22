# 🔌 Estado y Configuración de Integraciones Externas

---

## 1. 📁 Google Drive (Servidor MCP / CLI `gdrive`) — ✅ CONECTADO Y SINCRONIZADO

Google Drive está completamente sincronizado con el repositorio local. Estructura indexada del curso:
- **Carpeta Principal:** `Machine learning` (ID: `1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd`)
- **Documento Clave:** `INFO MACHINE LEARNING` (Comisión #26240, ID Zoom, contactos docentes)
- **Subcarpetas Vinculadas:**
  - `01_Clases` (`1MarNh0EPP4x5nq8z2VC3tmniObbVWLHf`): Teóricos y resúmenes en Markdown y PDF (Clases 01 a 08 y 10 a 16). *Pendiente teórico de Clase 09.*
  - `02_Ejercicios_y_Practicas` (`16WQHww4NzqpwEobl_I6BnQhtsLXWOtxQ`): Ejercicios prácticos en PDF (Clases 01 a 08), en Markdown (Clases 07, 08 y 10 a 15) y `Practica_K-Means.md`.
  - `03_Proyectos_y_Entregables` (`1Pqr-AtRrUv_YoEv_W4YXnXf2bzedrObe`):
    - Preentrega archivada: `HERNANDEZ MATIAS H - Comisión 26240 - TPI Data Analytics/` (`1DY8Si57sSVaHQaL74p8PFVsr1pHNNZzp`) y `ML - Consigna Pre-entrega.*`.
    - Entrega Final oficial: carpeta **`HERNANDEZ MATIAS H - Comisión 26240 - TPI Machine Learning`** (`1qlKrshYD_2ZqjH_gToYyP0Jt4nvjdiUT`) con `Pre_entrega26.ipynb` (`1Xuc2NMKoCCsg2QH1H7RNSqadfTVYN0HF`), `dataset.csv` (`1D-hpD1zvoAng0lD9Mci4_jXukBtS_G17`) e `informe_final.md` (`1kmaUo-ZMdGkDZcC9Vv9GbBipCuW200gZ`), además de `ML_Consigna_Entrega_Final.md`, `ML - Checklist Entrega Final.docx`, `CHECKLIST_ENTREGA_FINAL.md` y `ML_Referencia_Docente_Pre_entrega26.ipynb`.
  - `04_Colab_Notebooks` (`1bL2wThSTkSCxYubNOsjx83WZk_Xn2gD1`): Cuadernos interactivos de las clases (`Copia de clase4_2026b.ipynb`, `Clase_5.ipynb`, `Clase_6.ipynb`, `Copia de (Alumnos)Clase_7.ipynb`, `Clase_8.ipynb`, `Copia de (Alumnos)Clase_9.ipynb`, `Copia de (Nuevo26)clase_9b.ipynb`, entre otros).

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
