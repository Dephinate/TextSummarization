
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
    root_dir: Path
    status_file: str
    all_required_files: list
    local_data_folder: Path

# Entity for Data Transformation Configuration


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: str

# Entity for Model Training COnfiguration


@dataclass
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: str
    num_training_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: int
    logging_steps: int
    evaluation_strategy: str
    eval_steps: float
    save_steps: float
    gradient_accumulation_steps: int


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_path: Path
    model_path: Path
    metric_file_name: Path
