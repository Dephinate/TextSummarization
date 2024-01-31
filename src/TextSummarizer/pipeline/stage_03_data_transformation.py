# Initialize object of Config Manager
# Get DataTransformation COnfigurations
# Use those configurations to intialize Tranformation component

from TextSummarizer.config.configurations import ConfigurationManager
from TextSummarizer.components.data_transformation import DataTransformation


class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(
            config=data_transformation_config)
        data_transformation.convert()
