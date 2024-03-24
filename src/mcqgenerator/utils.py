import os
import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswith('.pdf'):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extractText()
            return text
        except Exception as e:
            raise Exception(f"Error reading PDF file: {e}")
        
    elif file.name.endswith('.txt'):
        try:
            with open(file.name, 'r') as f:
                return f.read().decode('utf-8')
        except Exception as e:
            raise Exception(f"Error reading TXT file: {e}")
    else:
        raise Exception(f"Unsupported file format: {file.name}")
    
    
def get_table_data(quiz_str):
    try:
        quiz_dict=json.loads(quiz_str)
        quiz_table_data=[]
        
        for key,value in quiz_dict.items():
           mcq = value["mcq"]
           options = " | ".join(
            [
                f"{option}: {option_value}" for option, option_value in value["options"].items()
                ]
            )
           correct = value["correct"]
           quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
    except Exception as e:
        raise Exception(f"Error parsing quiz string: {e}")
    
    return quiz_table_data
       