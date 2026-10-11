"""
Gestor de sincronización entre el entorno local de Talento Tech - ML y Google Drive / Google Colab.
Carpeta vinculada:
- Nombre / Destino: Talento Tech - ML
- Folder ID: 1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd
- URL: https://drive.google.com/drive/folders/1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd?usp=drive_link
"""

import os
import sys
import io
import argparse
from pathlib import Path
from typing import Optional, List, Dict, Any

# Asegurar codificación UTF-8 en consola de Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.errors import HttpError

# Alcance completo para leer, crear y organizar archivos en Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

# Carpeta principal asignada
TALENTO_TECH_FOLDER_ID = "1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd"
TALENTO_TECH_FOLDER_URL = "https://drive.google.com/drive/folders/1J0UZv6eVfVS5wiWrxY4-kC9mclB4dlLd?usp=drive_link"

# Rutas estándar de credenciales y tokens
BASE_DIR = Path(__file__).resolve().parent
WORKSPACE_DIR = BASE_DIR.parent

TOKEN_CANDIDATE_PATHS = [
    Path(r"c:\Users\n_e_o\IA\Orden GDrive\token.json"),
    BASE_DIR / "token.json",
    WORKSPACE_DIR / "token.json"
]

CREDS_CANDIDATE_PATHS = [
    Path(r"c:\Users\n_e_o\IA\Orden GDrive\credentials.json"),
    BASE_DIR / "credentials.json",
    WORKSPACE_DIR / "credentials.json"
]


def get_existing_file(candidates: List[Path]) -> Optional[Path]:
    for p in candidates:
        if p and p.exists():
            return p
    return None


def get_credentials(force_reauth: bool = False) -> Credentials:
    """Obtiene o renueva las credenciales OAuth 2.0."""
    creds = None
    token_path = get_existing_file(TOKEN_CANDIDATE_PATHS)

    if token_path and not force_reauth:
        try:
            creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
        except Exception as e:
            print(f"[-] Aviso al leer token existente ({token_path}): {e}")
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token and not force_reauth:
            try:
                print("[*] Renovando token de acceso expirado...")
                creds.refresh(Request())
            except Exception as e:
                print(f"[-] No se pudo refrescar el token ({e}). Iniciando reautenticación completa...")
                creds = None

        if not creds or not creds.valid:
            creds_path = get_existing_file(CREDS_CANDIDATE_PATHS)
            if not creds_path:
                raise FileNotFoundError(
                    "No se encontró credentials.json en ninguna de las rutas esperadas:\n"
                    + "\n".join(str(p) for p in CREDS_CANDIDATE_PATHS)
                )

            print("[*] Abriendo navegador para autorización de Google Drive...")
            flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), SCOPES)
            creds = flow.run_local_server(
                port=0,
                authorization_prompt_message=(
                    "\n======================================================\n"
                    "Si el navegador no abre automáticamente, copia y abre este enlace:\n"
                    "{url}\n"
                    "======================================================\n"
                ),
                success_message="¡Autenticación completada con éxito! Puedes cerrar esta pestaña."
            )

        # Guardar en la ruta primaria (Orden GDrive para que MCP y otros scripts lo sincronicen)
        primary_token_path = TOKEN_CANDIDATE_PATHS[0]
        try:
            primary_token_path.parent.mkdir(parents=True, exist_ok=True)
            with open(primary_token_path, "w", encoding="utf-8") as f:
                f.write(creds.to_json())
            print(f"[+] Token guardado en: {primary_token_path}")
        except Exception as e:
            print(f"[-] No se pudo guardar en {primary_token_path}: {e}")

        # Guardar también copia local en 04_colab_sync
        local_token_path = BASE_DIR / "token.json"
        try:
            with open(local_token_path, "w", encoding="utf-8") as f:
                f.write(creds.to_json())
            print(f"[+] Copia de token guardada en: {local_token_path}")
        except Exception as e:
            print(f"[-] No se pudo guardar copia local: {e}")

    return creds


def get_drive_service(force_reauth: bool = False):
    """Retorna cliente de la API Google Drive v3."""
    creds = get_credentials(force_reauth=force_reauth)
    return build('drive', 'v3', credentials=creds)


def get_folder_info(folder_id: str = TALENTO_TECH_FOLDER_ID) -> Dict[str, Any]:
    """Obtiene información básica de la carpeta."""
    service = get_drive_service()
    return service.files().get(
        fileId=folder_id,
        fields="id, name, mimeType, webViewLink, owners, shared"
    ).execute()


def list_folder_contents(folder_id: str = TALENTO_TECH_FOLDER_ID, recursive: bool = False) -> List[Dict[str, Any]]:
    """Lista elementos dentro de la carpeta especificada."""
    service = get_drive_service()
    query = f"'{folder_id}' in parents and trashed = false"
    items = []
    page_token = None

    while True:
        results = service.files().list(
            q=query,
            pageSize=100,
            fields="nextPageToken, files(id, name, mimeType, modifiedTime, size, webViewLink)",
            pageToken=page_token
        ).execute()

        files = results.get('files', [])
        for f in files:
            f['isFolder'] = (f.get('mimeType') == 'application/vnd.google-apps.folder')
            items.append(f)
            if recursive and f['isFolder']:
                items.extend(list_folder_contents(folder_id=f['id'], recursive=True))

        page_token = results.get('nextPageToken')
        if not page_token:
            break

    return items


def find_or_create_subfolder(folder_name: str, parent_id: str = TALENTO_TECH_FOLDER_ID) -> str:
    """Busca o crea una subcarpeta dentro del directorio padre."""
    service = get_drive_service()
    query = f"'{parent_id}' in parents and name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])
    if files:
        return files[0]["id"]

    # Crear subcarpeta
    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    created = service.files().create(body=folder_metadata, fields='id').execute()
    print(f"[+] Subcarpeta creada en Drive: '{folder_name}' (ID: {created['id']})")
    return created['id']


def upload_file(local_path: str, parent_folder_id: str = TALENTO_TECH_FOLDER_ID) -> Dict[str, Any]:
    """Sube o actualiza un archivo local en Google Drive."""
    service = get_drive_service()
    p = Path(local_path).resolve()
    if not p.is_file():
        raise FileNotFoundError(f"Archivo no encontrado: {local_path}")

    filename = p.name
    # Verificar si ya existe con el mismo nombre en la carpeta
    query = f"'{parent_folder_id}' in parents and name = '{filename}' and trashed = false"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    existing = results.get("files", [])

    media = MediaFileUpload(str(p), resumable=True)

    if existing:
        file_id = existing[0]['id']
        updated = service.files().update(
            fileId=file_id,
            media_body=media,
            fields='id, name, webViewLink'
        ).execute()
        print(f"[+] Archivo actualizado en Drive: {filename} (ID: {updated['id']})")
        return updated
    else:
        file_metadata = {
            'name': filename,
            'parents': [parent_folder_id]
        }
        uploaded = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name, webViewLink'
        ).execute()
        print(f"[+] Archivo subido a Drive: {filename} (ID: {uploaded['id']})")
        return uploaded


def sync_directory_to_drive(local_dir: str, target_subfolder_name: Optional[str] = None):
    """Sube recursivamente un directorio local a Google Drive."""
    src = Path(local_dir).resolve()
    if not src.is_dir():
        print(f"[-] Directorio inexistente: {local_dir}")
        return

    dest_folder_id = TALENTO_TECH_FOLDER_ID
    if target_subfolder_name:
        dest_folder_id = find_or_create_subfolder(target_subfolder_name, TALENTO_TECH_FOLDER_ID)

    for item in src.iterdir():
        if item.name.startswith(('.', '__pycache__', 'node_modules')):
            continue
        if item.is_file():
            try:
                upload_file(str(item), parent_folder_id=dest_folder_id)
            except Exception as e:
                print(f"[-] Error al subir {item.name}: {e}")
        elif item.is_dir():
            sub_id = find_or_create_subfolder(item.name, dest_folder_id)
            sync_subdir(item, sub_id)


def sync_subdir(src_path: Path, parent_id: str):
    for item in src_path.iterdir():
        if item.name.startswith(('.', '__pycache__', 'node_modules')):
            continue
        if item.is_file():
            try:
                upload_file(str(item), parent_folder_id=parent_id)
            except Exception as e:
                print(f"[-] Error al subir {item.name}: {e}")
        elif item.is_dir():
            sub_id = find_or_create_subfolder(item.name, parent_id)
            sync_subdir(item, sub_id)


def download_file(file_id: str, destination_path: str) -> str:
    """Descarga un archivo desde Google Drive."""
    service = get_drive_service()
    dest = Path(destination_path).resolve()
    dest.parent.mkdir(parents=True, exist_ok=True)

    request = service.files().get_media(fileId=file_id)
    with io.FileIO(str(dest), 'wb') as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            if status:
                print(f"Descargando {int(status.progress() * 100)}%...")

    print(f"[+] Archivo descargado en: {dest}")
    return str(dest)


def init_course_structure(folder_id: str = TALENTO_TECH_FOLDER_ID) -> Dict[str, str]:
    """
    Crea y ordena la jerarquía completa de subcarpetas en Google Drive:
    - 01_Clases
    - 02_Ejercicios_y_Practicas
    - 03_Proyectos_y_Entregables
    - 04_Colab_Notebooks
    - 05_Datasets_y_Recursos
    - 06_Material_Adicional
    """
    subcarpetas = [
        ("01_Clases", "Clases teóricas, diapositivas, resúmenes y grabaciones."),
        ("02_Ejercicios_y_Practicas", "Guías prácticas, laboratorios y ejercicios semanales."),
        ("03_Proyectos_y_Entregables", "Proyecto integrador, entregas parciales y avances de cursada."),
        ("04_Colab_Notebooks", "Cuadernos (.ipynb) ejecutados y sincronizados desde Google Colab."),
        ("05_Datasets_y_Recursos", "Datasets (CSV, JSON, Parquet), modelos guardados y recursos de datos."),
        ("06_Material_Adicional", "Bibliografía recomendada, cheatsheets, lecturas y tutoriales.")
    ]

    print(f"\n[*] Creando y organizando estructura en Google Drive (Carpeta ID: {folder_id})...\n")
    created_map = {}
    for name, desc in subcarpetas:
        sub_id = find_or_create_subfolder(name, folder_id)
        created_map[name] = sub_id
        print(f"  📁 [OK] {name:<26} -> ID: {sub_id}")

    print("\n✅ ¡Estructura de Google Drive organizada con éxito!")
    return created_map


def classify_file(filename: str) -> str:
    """Clasifica un archivo según su nombre y extensión."""
    name_lower = filename.lower()

    # 1. Entregas y proyectos
    if any(k in name_lower for k in ["entrega", "pre_entrega", "proyecto", "integrador"]):
        return "03_Proyectos_y_Entregables"

    # 2. Ejercicios prácticos
    if any(k in name_lower for k in ["ejercicio", "ejercicios", "practic", "practica"]):
        return "02_Ejercicios_y_Practicas"

    # 3. Notebooks de Colab
    if filename.endswith(".ipynb"):
        return "04_Colab_Notebooks"

    # 4. Material de clase (diapositivas, apuntes, resúmenes)
    if any(k in name_lower for k in ["clase", "presentacion", "teoria"]):
        return "01_Clases"

    # 5. Datasets y Recursos
    if any(filename.endswith(ext) for ext in [".csv", ".xlsx", ".json", ".parquet", ".pkl", ".h5"]):
        return "05_Datasets_y_Recursos"

    # 6. Material complementario (infografías, calendarios, PDFs generales)
    return "06_Material_Adicional"


def move_file(service, file_id: str, source_folder_id: str, target_folder_id: str) -> Any:
    """Mueve un archivo en Drive de una carpeta a otra."""
    return service.files().update(
        fileId=file_id,
        addParents=target_folder_id,
        removeParents=source_folder_id,
        fields='id, parents'
    ).execute()


def organize_root_files(folder_id: str = TALENTO_TECH_FOLDER_ID) -> Dict[str, List[str]]:
    """Mueve todos los archivos sueltos de la raíz a su subcarpeta correspondiente."""
    service = get_drive_service()
    subfolder_map = init_course_structure(folder_id)

    root_items = list_folder_contents(folder_id=folder_id, recursive=False)
    files_to_move = [it for it in root_items if not it.get("isFolder")]

    if not files_to_move:
        print("[*] No hay archivos sueltos en la raíz de Google Drive. Todo está ordenado.")
        return {}

    print(f"\n[*] Moviendo {len(files_to_move)} archivos a sus subcarpetas correspondientes...\n")
    moved_summary = {k: [] for k in subfolder_map.keys()}

    for f in files_to_move:
        fname = f["name"]
        fid = f["id"]
        target_name = classify_file(fname)
        target_id = subfolder_map[target_name]

        try:
            move_file(service, fid, folder_id, target_id)
            moved_summary[target_name].append(fname)
            print(f"  ➡️  {fname}  ==>  {target_name}/")
        except Exception as e:
            print(f"  ❌ Error moviendo {fname}: {e}")

    print("\n🎉 ¡Todos los archivos fueron clasificados y organizados en sus subcarpetas con éxito!")
    return moved_summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gestor de sincronización con Google Drive de Talento Tech")
    parser.add_argument("--auth", action="store_true", help="Fuerza el flujo de reautenticación OAuth 2.0")
    parser.add_argument("--list", action="store_true", help="Lista el contenido de la carpeta en Google Drive")
    parser.add_argument("--init-structure", action="store_true", help="Crea y organiza las subcarpetas del curso")
    parser.add_argument("--organize-files", action="store_true", help="Mueve archivos sueltos a sus subcarpetas")
    parser.add_argument("--upload", type=str, help="Sube un archivo a la carpeta vinculada")
    parser.add_argument("--sync-workspace", action="store_true", help="Sincroniza 01_clases, 02_proyectos y recursos")

    args = parser.parse_args()

    if args.auth:
        print("[*] Iniciando autenticación interactiva...")
        creds = get_credentials(force_reauth=True)
        print("[+] Autenticación completada con éxito.")
    elif args.init_structure:
        init_course_structure()
    elif args.organize_files:
        organize_root_files()
    elif args.list:
        info = get_folder_info()
        print(f"\n📂 Carpeta vinculada: {info.get('name')} (ID: {info.get('id')})")
        print(f"🔗 Enlace: {info.get('webViewLink')}\n")
        items = list_folder_contents()
        if not items:
            print("La carpeta está vacía.")
        else:
            print("Contenido:")
            for it in items:
                prefix = "[📁 Carpeta]" if it.get("isFolder") else "[📄 Archivo]"
                print(f" - {prefix} {it.get('name')} (ID: {it.get('id')})")
    elif args.upload:
        upload_file(args.upload)
    elif args.sync_workspace:
        print("[*] Sincronizando clases y proyectos hacia Google Drive...")
        sync_directory_to_drive(str(WORKSPACE_DIR / "01_clases"), "01_Clases")
        sync_directory_to_drive(str(WORKSPACE_DIR / "02_proyectos"), "03_Proyectos_y_Entregables")
        sync_directory_to_drive(str(WORKSPACE_DIR / "03_recursos"), "05_Datasets_y_Recursos")
        print("[+] Sincronización finalizada.")
    else:
        parser.print_help()
