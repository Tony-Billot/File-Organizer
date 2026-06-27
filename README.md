# 📁 File Organizer (Python)

A simple and powerful Python script that automatically organizes files in a folder based on their extensions.

---

## 🚀 Features

- 🧠 Automatically sorts files into categories
- 📂 Supports images, documents, videos, audio, archives, code, and more
- 🔁 Recursively scans folders and subfolders
- 📁 Automatically creates missing directories
- ⚙️ Fully configurable via `.config`
- 🛡️ Built-in validation and error handling

---

## 📂 Supported Categories

- 🖼️ **Images** → `.jpg`, `.png`, `.gif`, `.webp`, `.svg`
- 📄 **Documents** → `.pdf`, `.docx`, `.txt`, `.md`
- 🎬 **Videos** → `.mp4`, `.mov`, `.mkv`, `.avi`, `.webm`
- 🎵 **Audio** → `.mp3`, `.wav`, `.flac`, `.ogg`
- 📦 **Archives** → `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- 💻 **Code** → `.py`, `.js`, `.ts`, `.html`, `.css`, `.cpp`
- 🧠 **Python / ML** → `.pkl`, `.pth`, `.ipynb`
- ⚙️ **Executables** → `.exe`, `.msi`, `.bat`, `.sh`
- 📁 **Others** → fallback category

---

## ⚙️ Configuration

Create a `.config` file in the root directory:

```ini
FOLDER=/path/to/your/folder
