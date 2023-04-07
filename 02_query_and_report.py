import os

from llama_index import GPTSimpleVectorIndex, QuestionAnswerPrompt

from environment_setup import logger, data_directory

try:
    openai_api_key = os.environ.get('OPENAI_API_KEY')

    if openai_api_key is None:
        raise ValueError("OpenAI API Key not found. Expecting OPENAI_API_KEY in the environment")
except ValueError as err:
    logger.error(f"{err}")
    exit()

def main()-> None:
    try:
        logger.info("Starting CV Comparer using OpenAI API , phase query & report...")

        logger.info("Create Prompt & Query String")
        QA_PROMPT_TMPL = (
            "Hello, I have some context information for you:\n"
            "---------------------\n"
            "{context_str}"
            "\n---------------------\n"
            "Based on this context, could you please help me understand the answer to this question: {query_str}?\n"
        )
        QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)

        logger.info("Read index file")
        index = GPTSimpleVectorIndex.load_from_disk(data_directory /'cv_index_file_0.json')

        query_str = "What skills does Rajesh Babu Have ?"
        response = index.query(query_str, text_qa_template=QA_PROMPT)
        logger.info(response)


    except Exception as err:
        logger.error(f"{err}")    
    finally:
        logger.info("... finished CV Comparer using OpenAI API, phase query & report")

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logger.error(f"{err}") 