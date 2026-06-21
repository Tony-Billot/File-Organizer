# 📁 File Organizer (Python)

A simple and powerful Python script that automatically organizes files in a folder based on their extensions.

---

## 🚀 Features

- Automatically sorts files into categories
- Supports images, documents, videos, audio, archives, code, and more
- Recursively scans folders
- Automatically creates missing directories
- Configurable via `.config` file

---

## 📂 Supported Categories

- 🖼️ Images (`.jpg`, `.png`, `.gif`, etc.)
- 📄 Documents (`.pdf`, `.docx`, `.txt`, etc.)
- 🎬 Videos (`.mp4`, `.mov`, `.mkv`, etc.)
- 🎵 Audio (`.mp3`, `.wav`, `.flac`, etc.)
- 📦 Archives (`.zip`, `.rar`, `.7z`, etc.)
- 💻 Code (`.py`, `.js`, `.html`, `.css`, etc.)
- 🧠 Python / ML files (`.pkl`, `.pth`, `.ipynb`, etc.)
- ⚙️ Executables (`.exe`, `.msi`, etc.)
- 📁 Others (fallback category)

---

## ⚙️ Configuration

Create a `.config` file in the project root:

```text
FOLDER=the_folder_you_want_to_organize
