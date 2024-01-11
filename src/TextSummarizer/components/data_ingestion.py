import os
import urllib.request as request
import zipfile
from pathlib import Path
from TextSummarizer.utils.common import get_size
from TextSummarizer.logging import logger
from TextSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(
            self,
            config: DataIngestionConfig
            ) -> None:
        self.config = config

    # Method to download the file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
                )
            logger.info(f'{filename} download! with the following info: \n{header}')
        else:
            logger.info(f"File already exits of size: {get_size(Path(self.config.local_data_file))}")

    # Method to Extract the downloaded file
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            