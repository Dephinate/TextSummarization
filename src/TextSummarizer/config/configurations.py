
from TextSummarizer.constants import *
from TextSummarizer.utils.common import read_yaml, create_directories
from TextSummarizer.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig


class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            param_filepath=PARAMS_FILE_PATH) -> None:

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(param_filepath)

        create_directories([self.config.artifacts_root])

    # Method to read Data Ingestion Config

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    # Method to read Data Validation Config
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            all_required_files=config.all_required_files,
            local_data_folder=config.local_data_folder
        )
        return data_validation_config

    # Method to read Data Transformation Configuration
    def get_data_transformation_config(self) -> DataIngestionConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )
        return data_transformation_config

    # Method to read model trainer configuration

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            num_training_epochs=params.num_training_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps

        )
        return model_trainer_config
        # Method to real model evaluation configuration

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_path=config.tokenizer_path,
            model_path=config.model_path,
            metric_file_name=config.metric_file_name

        )
        return model_evaluation_config
