import os
from pathlib import Path
from typing import List

from llama_index import GPTSimpleVectorIndex, download_loader

from application_logger import logger

try:
    openai_api_key = os.environ.get('OPENAI_API_KEY')

    if openai_api_key is None:
        raise ValueError("OpenAI API Key not found. Expecting OPENAI_API_KEY in the environment")
except ValueError as err:
    logger.error(f"{err}")
    exit()

def get_cvs_from_linked_in()-> List:
    try:
        # Initialise web page loader
        SimpleWebPageReader = download_loader("SimpleWebPageReader")
        loader = SimpleWebPageReader()

        list_of_linked_in_cv_links = [
            'https://www.linkedin.com/in/rajesh-babu-7203785/',
            'https://www.linkedin.com/in/jason-paris-3404565/',
            'https://www.linkedin.com/in/jolie-hodson-she-her-8248a44a/',
            'https://www.linkedin.com/in/mark-aue/'
        ]

        list_of_cv_documents = loader.load_data(urls=list_of_linked_in_cv_links)
        # for cv_link in list_of_linked_in_cv_links:
        #     cv_document = loader.load_data(urls=['https://arstechnica.com/gadgets/2023/04/9-best-accessories-for-macbook-pro-and-mac-mini/'])
        return list_of_cv_documents
    except Exception as err:
        logger.error(f"{err}")
        raise err

def main():
    try:
        logger.info("Starting CV Comparer using OpenAI API ...")

        list_of_cv_documents = get_cvs_from_linked_in()
        logger.info(f"{len(list_of_cv_documents)} documents fetched from Linked In")
    except Exception as err:
        logger.error(f"{err}")    
    finally:
        logger.info("... finished CV Comparer using OpenAI API")

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logger.error(f"{err}")    