# CV_Comparer_Example
Training exercise using OpenAI API to compare CVs

# Setup on VDI
- Set up virtual env : python3 -m venv venv --upgrade-deps
- poetry init
- poetry config virtualenvs.in-project true
- poetry install
    - poetry add
    - poetry remove
- on python shell
    - MacOS : export OPENAI_API_KEY=
    - Powershell : $env:OPENAI_API_KEY=

# Run on VDI
-  Add PDF CVs to data directory
-  Run 01_generate_indices.py to generate the index file
-  Run 02_query_and_report.py to gerenate the excel report in comparisons directory