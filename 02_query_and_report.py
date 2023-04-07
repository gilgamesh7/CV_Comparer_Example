import os

from llama_index import GPTSimpleVectorIndex, QuestionAnswerPrompt
from openpyxl import Workbook
from datetime import datetime

from environment_setup import logger, indices_directory, list_of_people, comparison_directory

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
        index = GPTSimpleVectorIndex.load_from_disk(indices_directory /'cv_index.json')


        # Create comparison spreadsheet
        comparison_file_name = comparison_directory / f'report_{datetime.today().date()}.xlsx'
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "CV Comparision Table"

        # Generate comparison spreadsheet spreadsheet
        for column_number, person in enumerate(list_of_people):
            # Get first answer
            query_str = f"What skills does {person} have ?"
            response = index.query(query_str, text_qa_template=QA_PROMPT)
            # Write answer to sheet
            sheet[f'A{column_number+1}'] = response.response

        for column_number, person in enumerate(list_of_people):
            # Get second answer
            query_str = f"How many years experience does {person} have ?"
            response = index.query(query_str, text_qa_template=QA_PROMPT)
            # Write answer to sheet
            sheet[f'B{column_number+1}'] = response.response

        for column_number, person in enumerate(list_of_people):
            # Get third  answer
            query_str = f"Is {person} a good fit for a product owner role ?"
            response = index.query(query_str, text_qa_template=QA_PROMPT)
            # Write answer to sheet
            sheet[f'C{column_number+1}'] = response.response

        for column_number, person in enumerate(list_of_people):
            # Get fourth  answer
            query_str = f"Will {person} thrive in an agile squad ?"
            response = index.query(query_str, text_qa_template=QA_PROMPT)
            # Write answer to sheet
            sheet[f'D{column_number+1}'] = response.response

        for column_number, person in enumerate(list_of_people):
            # Get fifth  answer
            query_str = f"Does {person} show an aptitude for continuous learning and tradecraft development ?"
            response = index.query(query_str, text_qa_template=QA_PROMPT)
            # Write answer to sheet
            sheet[f'E{column_number+1}'] = response.response

        for column_number, person in enumerate(list_of_people):
            # Get sixth  answer
            query_str = f"Will {person} be easy and approachable to others in the squad ?"
            response = index.query(query_str, text_qa_template=QA_PROMPT)
            # Write answer to sheet
            sheet[f'F{column_number+1}'] = response.response

        workbook.save(comparison_file_name)
        workbook.close()    


    except Exception as err:
        logger.error(f"{err}")    
    finally:
        logger.info("... finished CV Comparer using OpenAI API, phase query & report")

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logger.error(f"{err}") 