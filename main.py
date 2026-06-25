import shutil
import pathlib

# read configuration

config = {}

with open(".config", "r") as f:
    for line in f:
        if "=" in line:
            key, value = line.strip().split("=", 1)
            config[key] = value

FOLDER = pathlib.Path(config["FOLDER"])

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
    shutil.move(str(file), str(category_folder / file.name))
    print(f"Moved {file.name} to {category_folder} !")


def organize(folder):
    create_folder(folder)
    files = get_files(folder)

    for file in files:
        move_file(file, folder)
    print("Files organized successfully!")


if __name__ == "__main__":
    organize(FOLDER)