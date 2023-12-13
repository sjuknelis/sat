import sys, json

with open(sys.argv[1], "r") as f:
    data = json.load(f)

    for question in data["question_set"]:
        question["answers"] = ["\n".join(answer) for answer in question["answers"]]

with open(sys.argv[1], "w") as f:
    json.dump(data, f)