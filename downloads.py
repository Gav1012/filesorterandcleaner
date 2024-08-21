import os
import shutil
from pathlib import Path

downloads_folder = Path.home() / 'Downloads'

for file in downloads_folder.iterdir():
    if file.is_file():
        print(file.name)