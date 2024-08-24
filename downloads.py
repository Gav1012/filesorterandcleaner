import os
import shutil
from pathlib import Path

downloads_folder = Path.home() / 'Downloads'

def create_folder(folder_path):
    if not folder_path.exists():
        folder_path.mkdir(parents=True, exist_ok=True)

def move_file(file, destination_folder):
    create_folder(destination_folder)
    shutil.move(str(file), str(destination_folder / file.name))

for file in downloads_folder.iterdir():
    if file.is_file():
        print(file.name)