import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "src/config.py",
    "src/utils.py",
    "src/models.py",
    "src/routes.py",
    "src/main.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    
]

for file_path in list_of_files:
    path = Path(file_path)
    file_dir, file_name = os.path.split(path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir}")

    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, "w") as f:
            logging.info(f"Creating empty file: {file_name}")
            pass
        
    else:
        logging.info(f"File already exists: {file_name}")

logging.info("All files created successfully")