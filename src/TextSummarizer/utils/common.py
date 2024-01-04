#   1) A yaml opener with some sort exception handler
#   2) A function to check size of any file

import os
from pathlib import Path
from TextSummarizer.logging import logger
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from typing import Any


# Read contents of a yaml file and return a ConfigBox
@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox

    Args:
        path to the yaml (str): Path like input

    Raises:
        ValueErro: is yaml is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e


# Function to create directories   
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Function to create directories

    Args:
        path_to_directories (list): list of directory paths 
    """
    for path in  path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


# Function to get the size of a file
@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    Args:
        path (Path): path of the file
    
    Returns:
        file size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"