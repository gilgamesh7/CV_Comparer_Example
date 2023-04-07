import logging
from pathlib import Path

# Initialise Logger & environment
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {lineno} - {message}", style='{')
logger = logging.getLogger("CV-COMPARE")

# List of CVs to process, downloaded from :
# 'https://www.linkedin.com/in/rajesh-babu-7203785/',
# 'https://www.linkedin.com/in/jason-paris-3404565/',
# 'https://www.linkedin.com/in/jolie-hodson-she-her-8248a44a/',
# 'https://www.linkedin.com/in/mark-aue/'
list_of_cvs = [
    'Jason_Paris.pdf',
    'Jolie_Hodson.pdf',
    'Mark_Aue.pdf',
    'Rajesh Babu.pdf'
]

# Generate file names
data_directory = Path()/'data'
data_directory.mkdir(parents=True, exist_ok=True)
