import os
import shutil


def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist. Please check the path.")
        return

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".avif"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
        "Documents": [".pdf", ".csv", ".md", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".odt"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Programs": [".exe"]
    }

    moved_files = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in categories.items():
                if file_ext in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    moved_files += 1
                    moved = True
                    break

            if not moved:
                category_folder = os.path.join(folder_path, "Other")
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                moved_files += 1

    print(f"Organization complete! {moved_files} file(s) moved.")


if __name__ == "__main__":
    print("=== File Organizer ===")
    folder = input("Enter the full path to the folder you want to organize: ").strip()

    if folder:
        organize_files(folder)
    else:
        print("No folder path entered. Exiting...")
