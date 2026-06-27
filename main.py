import shutil
import pathlib

# Read configuration file
config_path = pathlib.Path(".config")
config = {}

with open(config_path, "r") as f:
    for line in f:
        line = line.strip()
        if "=" in line and not line.startswith("#"):  # ignore les commentaires
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()
if "FOLDER" not in config or not config["FOLDER"]:
    print("Erreur : la clé FOLDER est absente ou vide dans .config.")
    print("Ajoutez cette ligne dans .config : FOLDER=/chemin/vers/dossier")
    exit(1)

# Check if the specified folder exists and is a directory
FOLDER = pathlib.Path(config["FOLDER"])
if not FOLDER.exists():
    print(f"Erreur : le dossier spécifié n'existe pas : {FOLDER}")
    exit(1)
if not FOLDER.is_dir():
    print(f"Erreur : le chemin spécifié n'est pas un dossier : {FOLDER}")
    exit(1)

CATEGORIES = {
    # 🖼️ Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".webp": "Images",

    # 📄 Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".md": "Documents",
    ".odt": "Documents",

    # 📊 Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",

    # 🎬 Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".webm": "Videos",

    # 🎵 Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".ogg": "Audio",

    # 📦 Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    # 💻 Code
    ".py": "Code",
    ".js": "Code",
    ".ts": "Code",
    ".html": "Code",
    ".css": "Code",
    ".cpp": "Code",
    ".c": "Code",
    ".java": "Code",
    ".json": "Code",
    ".xml": "Code",

    # ⚙️ Executables / installers
    ".exe": "Executables",
    ".msi": "Executables",
    ".bat": "Executables",
    ".sh": "Executables",

    # 🧠 Python / ML files
    ".pth": "Python Files",
    ".pkl": "Python Files",
    ".ipynb": "Python Notebooks",
}


def get_category(extension):
    return CATEGORIES.get(extension.lower(), "Others")

def create_folder(folder):
    for category in set(CATEGORIES.values()):
        (folder / category).mkdir(exist_ok=True)
    (folder / "Others").mkdir(exist_ok=True)

def get_files(folder):
    files = []
    ignored = set(CATEGORIES.values()) | {"Others"}
    for item in folder.iterdir():
        if item.is_file():
            files.append(item)
        elif item.is_dir() and item.name not in ignored:
            files.extend(get_files(item))
    return files

def move_file(file, destination_folder):
    category = get_category(file.suffix)
    category_folder = destination_folder / category
    category_folder.mkdir(exist_ok=True)
    target_path = get_unique_path(category_folder, file.name)
    shutil.move(str(file), str(target_path))
    print(f"Moved {file.name} to {category_folder} !")

def organize(folder):
    create_folder(folder)
    files = get_files(folder)

    for file in files:
        move_file(file, folder)
    print("Files organized successfully!")


def get_unique_path(destination_folder, file_name):
    file_path = pathlib.Path(file_name)
    base_name, extension = file_path.stem, file_path.suffix
    counter = 1
    new_file_name = file_name
    while (destination_folder / new_file_name).exists():
        new_file_name = f"{base_name} ({counter}){extension}"
        counter += 1
    return destination_folder / new_file_name


if __name__ == "__main__":
    organize(FOLDER)