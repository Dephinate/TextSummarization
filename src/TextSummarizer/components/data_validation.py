import os
from TextSummarizer.entity import DataValidationConfig
from TextSummarizer.logging import logger


class DataValidation:
    def __init__(
        self,
        config: DataValidationConfig
    ) -> None:
        self.config = config

    def validate_all_files_exist(self):

        try:

            validation_status = None
            files_in_local_data_folder = os.listdir(
                self.config.local_data_folder)

            for file in self.config.all_required_files:
                if file not in files_in_local_data_folder:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                        logger.info(
                            f"Data Validation Status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                        logger.info(
                            f"Data Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
