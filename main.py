import json
from difflib import get_close_matches

def load_json_file(file_path : str) -> dict:
    with open (file_path, 'r') as file:
        data :dict = json.load(file)
    return data


def saving_to_json (file_path : str, data : dict):
    with open (file_path , 'w') as file:
        json.dump(file, data, indent = 4)


def find_best_match (user_question : str, questions : list[str]) -> str | None:
    best_match : str = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return best_match if best_match else None


def get_answer(question : str, DataBase : dict) -> str | None :
    for q in DataBase["questions"]:
        if q["question"] == question:
            return q["answer"]


def chatBot():
    pass