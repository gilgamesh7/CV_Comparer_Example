import os
from typing import List

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

from environment_setup import logger, data_directory, indices_directory

try:
    openai_api_key = os.environ.get('OPENAI_API_KEY')

    if openai_api_key is None:
        raise ValueError("OpenAI API Key not found. Expecting OPENAI_API_KEY in the environment")
except ValueError as err:
    logger.error(f"{err}")
    exit()

def generate_documents_from_pdfs()-> List:
    try:
        logger.info("Generate documents list with all CVs from PDFs")
        list_of_cv_documents = SimpleDirectoryReader('data').load_data()

        logger.info(f"Returning {len(list_of_cv_documents)} documents")
        return list_of_cv_documents
    except Exception as err:
        logger.error(f"{err}")
        raise err

def generate_index_for_cvs(list_of_cv_documents: List)-> object:
    try:
        logger.info(f"Generating index for {len(list_of_cv_documents)} documents")

        cv_index = GPTSimpleVectorIndex.from_documents(list_of_cv_documents)

        # list_of_cv_indices = []
        # for cv_document in list_of_cv_documents:
        #     cv_index = GPTSimpleVectorIndex.from_documents([cv_document])
        #     list_of_cv_indices.append(cv_index)

        logger.info(f"Returning {type(cv_index)} for CVs")
        return(cv_index)
    except Exception as err:
        logger.error(f"{err}")
        raise err    

def save_index_to_file(cv_index: object)-> None:
    try:
        logger.info(f"Saving index to file")

        cv_index.save_to_disk(indices_directory / f'cv_index.json')
    except Exception as err:
        logger.error(f"{err}")
        raise err  


def main()-> None:
    try:
        logger.info("Starting CV Comparer using OpenAI API , phase download & index...")

        list_of_cv_documents = generate_documents_from_pdfs()
        logger.info(f"{len(list_of_cv_documents)} documents created from PDFs")

        cv_index = generate_index_for_cvs(list_of_cv_documents)
        logger.info(f"Index generated")

        save_index_to_file(cv_index)

    except Exception as err:
        logger.error(f"{err}")    
    finally:
        logger.info("... finished CV Comparer using OpenAI API , phase download & index")

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logger.error(f"{err}")    