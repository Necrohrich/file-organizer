# File Organizer (Python)

A simple Python script that organizes files in a folder into categorized subfolders based on their file extensions.

## Features
- Categorizes files into:
  - **Images**: `.jpg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`, `.avif`
  - **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`
  - **Documents**: `.pdf`, `.csv`, `.md`, `.doc`, `.docx`, `.txt`, `.xlsx`, `.pptx`, `.odt`
  - **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`
  - **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
  - **Programs**: `.exe`
  - **Other**: Any file with an unknown extension
- Automatically creates target folders if they don't exist.
- Moves files instead of copying them, keeping the folder clean.

## Requirements
- Python 3.x
- No external libraries needed (uses only Python standard library)

## Installation
Clone the repository or download the script:
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/file-organizer.git
````

## Usage

Run the script and follow the prompts:

```bash
python file_organizer.py
```

You will be asked to:

1. Enter the **full path** to the folder you want to organize.

Example session:

```
=== File Organizer ===
Enter the full path to the folder you want to organize: C:\Users\YourName\Downloads
Organization complete! 42 file(s) moved.
```

## License

MIT License

Хочешь, чтобы я сделал?
```
