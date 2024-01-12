# Data Ingestion
from TextSummarizer.constants import *
from TextSummarizer.utils.common import read_yaml, create_directories
from TextSummarizer.entity import DataIngestionConfig, DataValidationConfig

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
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config

    # Method to read Data Validation Config
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir ,
            status_file= config.status_file,
            all_required_files= config.all_required_files,
            local_data_folder= config.local_data_folder
        ) 
        return data_validation_config