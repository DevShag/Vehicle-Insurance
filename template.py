import os
from pathlib import Path

# Folders name
sorce_code_folder = "src"
component_folder = "component"
configuration = "configuration"
cloud_storage = "cloud_storage"

list_of_files = [
    f"{sorce_code_folder}/__init__.py",
    f"{sorce_code_folder}/{component_folder}/__init__.py",
    f"{sorce_code_folder}/{component_folder}/data_ingestion.py",
    f"{sorce_code_folder}/{component_folder}/data_validation.py",
    f"{sorce_code_folder}/{component_folder}/data_transformation.py",
    f"{sorce_code_folder}/{component_folder}/data_validation.py",
    f"{sorce_code_folder}/{component_folder}/model_trainer.py",
    f"{sorce_code_folder}/{component_folder}/model_evaluation.py",
    f"{sorce_code_folder}/{component_folder}/model_pusher.py",
    f"{sorce_code_folder}/{configuration}/__init__.py",
    f"{sorce_code_folder}/{configuration}/mongo_db_connection.py",
    f"{sorce_code_folder}/{configuration}/aws_connection.py",
    f"{sorce_code_folder}/{cloud_storage}/__init__.py",
    f"{sorce_code_folder}/{cloud_storage}/aws_storage/py",
    f"{sorce_code_folder}/data_access/__init__.py",
    f"{sorce_code_folder}/data_access/proj1.py",
    f"{sorce_code_folder}/constants/__init__.py",
    f"{sorce_code_folder}/entity/__init__.py",
    f"{sorce_code_folder}/entity/config_entity.py",
    f"{sorce_code_folder}/entity/artifact_entity.py",
    f"{sorce_code_folder}/entity/estimator.py",
    f"{sorce_code_folder}/entity/s3_estimator.py",
    f"{sorce_code_folder}/exception/__init__.py",
    f"{sorce_code_folder}/logger/__init__.py",
    f"{sorce_code_folder}/pipeline/__init__.py",
    f"{sorce_code_folder}/pipeline/training_pipeline.py",
    f"{sorce_code_folder}/pipeline/prediction_pipeline.py",
    f"{sorce_code_folder}/utils/__init__.py",
    f"{sorce_code_folder}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")


