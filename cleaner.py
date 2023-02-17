import pandas as pd
import csv
from glob import glob

def cleaner(file_path):
    # path of the questions
    # Note: Best to use absolute path
    QUESTIONS_PATH = file_path.strip()

    # path of the answers
    ANSWERS_PATH = f"{QUESTIONS_PATH[:-14]}Answers.xlsx"

    # create a CSV file
    CSV_PATH = f"{ANSWERS_PATH[:-5]}.csv" 

    # get unique questions
    df_question = pd.read_excel(QUESTIONS_PATH)
    unique_questions = []

    for index, row in df_question.iterrows():
        unique_questions.append(row['QUESTION'])


    # get questions with choices but not in question bank
    clean_questions = []
    missing_questions = []

    df_answers = pd.read_excel(ANSWERS_PATH)

    for index, row in df_answers.iterrows():
        # Access data for each column by column name
            
            if row['question'] in unique_questions:
                clean_questions.append((row['choice_number'], row['question']))
            else:
                
                missing_questions.append((row['choice_number'], row['question']))

    if len(missing_questions)!=0:
        for row in missing_questions:
            with open(CSV_PATH, 'a', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([row[0], row[1]])

        print(f"There are *{len(missing_questions)}* choices na hindi included ang question sa {QUESTIONS_PATH} file.")

    if len(missing_questions) == 0:
        print(f"Lahat ng questions sa {ANSWERS_PATH} ay available sa {QUESTIONS_PATH}")

folder_name = "FDG-Justin"
question = glob(f"{folder_name}/*Questions.xlsx")
print(question)

for xlsx_file in question:
    cleaner(xlsx_file)