import logging
from pathlib import Path

# Initialise Logger & environment
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {lineno} - {message}", style='{')
logger = logging.getLogger("CV-COMPARE")

# Generate source directories
data_directory = Path()/'data'
data_directory.mkdir(parents=True, exist_ok=True)

indices_directory = Path()/'indices'
indices_directory.mkdir(parents=True, exist_ok=True)

comparison_directory = Path()/'comparisons'
comparison_directory.mkdir(parents=True, exist_ok=True)

# List of people
list_of_people = [
    'Rajesh Babu',
    'Jolie Hosdon',
    'Mark Aue',
    'Jason Paris'
    ]
