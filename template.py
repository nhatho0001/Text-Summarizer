import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO , format= '%(asctime)s - %(message)s') 

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for path in list_of_files:
    crate_path = Path(path)
    pathFoder , pathFile = os.path.split(crate_path)
    if pathFoder != "":
         os.makedirs(pathFoder , exist_ok= True)

    if not os.path.exists(crate_path) or os.path.getsize(crate_path) == 0:
         with open(crate_path , 'w'):
            pass
    else:
        logging.info("File was exists")
         
         
