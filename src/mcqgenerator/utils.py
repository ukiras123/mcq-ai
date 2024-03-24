import os
from PyPDF2 import PdfReader
import json
import traceback


def read_file(file):
    if file.name.endswith('.pdf'):
        try:
            reader=PdfReader(file)
            text=[]
            for page_number in range(1):
                page = reader.pages[page_number]
                page_text = page.extract_text()
                
                text.append(page_text)
            return ''.join(text)
        except Exception as e:
            raise Exception(f"Error reading PDF file: {e}")
        
    elif file.name.endswith('.txt'):
        try:
            with open(file.name, 'r') as f:
                return f.read()
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
       