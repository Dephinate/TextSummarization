
# Data Ingestion
from dataclasses import dataclass
from pathlib import Path


# Entity for Data Ingestion Configuration
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# Entity for Data Validation Configuration
@dataclass
class DataValidationConfig:
    root_dir:Path
    status_file:str
    all_required_files:list
    local_data_folder: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: str