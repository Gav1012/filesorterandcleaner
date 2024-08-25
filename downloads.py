import os
import shutil
from pathlib import Path

extensions = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.jpeg': 'Images',
    '.gif': 'Images',
    '.webp': 'Images',
    '.pdf': 'PDF',
    '.doc': 'Text',
    '.docx': 'Text',
    '.txt': 'Text',
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.mp4': 'Video',
    '.mov': 'Video',
    '.exe': 'Executables'
}

# holds location of the downloads folder
downloads_folder = Path.home() / 'Downloads'
# creates folder to put files in if folder doesn't exist
def create_folder(folder_path):
    if not folder_path.exists():
        folder_path.mkdir(parents=True, exist_ok=True)
# moves file(s) into folder, calls create_folder
def move_file(file, destination_folder):
    create_folder(destination_folder)
    shutil.move(str(file), str(destination_folder / file.name))
# goes through all files in downloads folder, checks if it's a file
# and if it's extension in the extensions dictionary, moves it to the corresponding folder
for file in downloads_folder.iterdir():
    if file.is_file():
        if file.suffix in extensions:
            print("moved: ", file)
            destination = extensions[file.suffix]
            move_file(file, downloads_folder / destination)