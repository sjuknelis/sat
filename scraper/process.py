import json

from lines import get_passage_lines

def process_content(content):
    question_set = []
    for (index, question) in enumerate(content["questions"]):
        answers_items = content["answers"][index * 4:(index + 1) * 4]
        correct_answer_index = [index for (index, answers_item) in enumerate(answers_items) if "Correct" in answers_item.split("\n")[0]][0]
        answers = "\n".join([answer.split("\n")[2:] for answer in answers_items])

        question_set.append({
            "question": question,
            "answers": answers,
            "correct_answer_index": correct_answer_index
        })
    
    data = {
        "passage": get_passage_lines(content["passage"]),
        "question_set": question_set
    }
    with open("../data/" + content["title"] + ".json", "w") as f:
        json.dump(data, f)