import os
from typing import List

from llama_index import GPTSimpleVectorIndex, download_loader

from environment_setup import logger, list_of_cvs, data_directory

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

def generate_indices_for_cvs(list_of_cv_documents: List)-> object:
    try:
        logger.info(f"Generating indices for {len(list_of_cv_documents)} documents")

        list_of_cv_indices = []
        for cv_document in list_of_cv_documents:
            cv_index = GPTSimpleVectorIndex.from_documents([cv_document])
            list_of_cv_indices.append(cv_index)


        logger.info(f"Returning {len(list_of_cv_indices)} indices for CVs")
        return(list_of_cv_indices)
    except Exception as err:
        logger.error(f"{err}")
        raise err    

def save_indices_to_files(list_of_cv_indices: List)-> None:
    try:
        # save to disk
        for file_suffix, cv_index in enumerate(list_of_cv_indices):
            cv_index.save_to_disk(data_directory / f'cv_index_file_{file_suffix}.json')
    except Exception as err:
        logger.error(f"{err}")
        raise err  


def main()-> None:
    try:
        logger.info("Starting CV Comparer using OpenAI API , phase download & index...")

        list_of_cv_documents = get_cvs_from_linked_in()
        logger.info(f"{len(list_of_cv_documents)} documents fetched from Linked In")

        list_of_cv_indices = generate_indices_for_cvs(list_of_cv_documents)
        logger.info(f"{len(list_of_cv_indices)} indices generated")

        save_indices_to_files(list_of_cv_indices)

    except Exception as err:
        logger.error(f"{err}")    
    finally:
        logger.info("... finished CV Comparer using OpenAI API , phase download & index")

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logger.error(f"{err}")    