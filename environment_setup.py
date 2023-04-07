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

# create questions list - THIS DORES NOT WORK IN FOR LOOP
# person=""
# list_of_questions = [
#     f"What skills does {person} have ?",
#     f"How many years experience does {person} have ?",
#     f"Is {person} a good fit for a product owner role ?",
#     f"Will {person} thrive in an agile squad ?",
#     f"Does {person} show an aptitude for continuous learning and tradecraft development ?",
#     f"Will {person} be easy and approachable to others in the squad ?"
# ]