import json
from difflib import get_close_matches

def load_json_file(file_path : str) -> dict:
    with open (file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def saving_to_json (file_path : str, data : dict):
    with open (file_path , 'w') as file:
        json.dump(data, file, indent = 4)


def find_best_match (user_question : str, questions : list[str]) -> str | None:
    best_matches : list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return best_matches[0] if best_matches else None


def get_answer(question : str, DataBase : dict) -> str | None :
    for q in DataBase["questions"]:
        if q["question"] == question:
            return q["answer"]


def chatBot():
    dataBase : dict = load_json_file('TinyDB.json')
    
    while True:
        userInput : str = input('You: ')
    
        if userInput.lower() == 'quit':
            break

        best_match : str | None = find_best_match(userInput, [q["question"] for q in dataBase["questions"]])

        if best_match != None:
            answer : str = get_answer(best_match, dataBase)
            print (f'Beto: {answer}')
        else:
            print ('Beto: i don\'t know the answer, Can you teach me?')
            teachable_answer : str = input('Please give me the answer or "skip" to skip: ')

            if teachable_answer.lower() != "skip":
                dataBase["questions"].append({"question" : userInput, "answer": teachable_answer })
                saving_to_json('TinyDB.json', dataBase)
                print ('Beto: Thank you, i have learned a new answer!')



if __name__ == "__main__":
    chatBot()



