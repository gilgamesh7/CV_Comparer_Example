import logging
from pathlib import Path

# Initialise Logger & environment
logging.basicConfig(format="[{asctime}] - {funcName} - {lineno} - {message}", style='{')
logger = logging.getLogger("CV-COMPARE")

# List of CVs to process
list_of_linked_in_cv_links = [
    'https://www.linkedin.com/in/rajesh-babu-7203785/',
    'https://www.linkedin.com/in/jason-paris-3404565/',
    'https://www.linkedin.com/in/jolie-hodson-she-her-8248a44a/',
    'https://www.linkedin.com/in/mark-aue/'
]

# Generate file names
data_directory = Path()/'data'
data_directory.mkdir(parents=True, exist_ok=True)
index_file_name = data_directory / 'cv_index.json'