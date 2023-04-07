import os
from pathlib import Path
from typing import List

from llama_index import GPTSimpleVectorIndex, download_loader

from environment_setup import logger, list_of_linked_in_cv_links, index_file_name

try:
    openai_api_key = os.environ.get('OPENAI_API_KEY')

    if openai_api_key is None:
        raise ValueError("OpenAI API Key not found. Expecting OPENAI_API_KEY in the environment")
except ValueError as err:
    logger.error(f"{err}")
    exit()

def get_cvs_from_linked_in()-> List:
    try:
        logger.info("Initialise web page loader")
        SimpleWebPageReader = download_loader("SimpleWebPageReader")
        loader = SimpleWebPageReader()

        logger.info("Generate list with all CVs from Linked In")

        list_of_cv_documents = loader.load_data(urls=list_of_linked_in_cv_links)

        logger.info(f"Returning {len(list_of_cv_documents)} documents")
        return list_of_cv_documents
    except Exception as err:
        logger.error(f"{err}")
        raise err

def generate_index_for_cvs(list_of_cv_documents: List)-> object:
    try:
        logger.info("Generating indices for {len(list_of_cv_documents)} documents")

        cv_index = GPTSimpleVectorIndex.from_documents(list_of_cv_documents)

        logger.info(f"Returning index for CVs")
        return(cv_index)
    except Exception as err:
        logger.error(f"{err}")
        raise err    

def save_index_to_file(index: object)-> None:
    try:
        index_file = Path()/'data'/'index.json'
        # save to disk
        index.save_to_disk(index_file)
    except Exception as err:
        logger.error(f"{err}")
        raise err  


def main():
    try:
        logger.info("Starting CV Comparer using OpenAI API ...")

        list_of_cv_documents = get_cvs_from_linked_in()
        logger.info(f"{len(list_of_cv_documents)} documents fetched from Linked In")

        index = generate_index_for_cvs(list_of_cv_documents)

        save_index_to_file(index)

    except Exception as err:
        logger.error(f"{err}")    
    finally:
        logger.info("... finished CV Comparer using OpenAI API")

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logger.error(f"{err}")    