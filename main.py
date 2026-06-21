import os
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