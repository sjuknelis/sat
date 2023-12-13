import sys, json

with open(sys.argv[1] + ".json", "r") as f:
    data = json.load(f)

    messages = [
        [
            {"role": "user", "content": "Generate an SAT reading passage. Provide this passage as a JSON array of strings, where each string is one line.\nThe response should contain nothing but the passage in its JSON format, broken up into reasonably sized lines (at least 8 words per line)."},
            {"role": "assistant", "content": json.dumps(data["passage"])}
        ],
        [
            {"role": "user", "content": "Create a difficult SAT reading question for a literary narrative passage (potentially one provided earlier in the chat history). Provide the correct answer. When listing the answer choices, do not include any letter prefixes like \"A.\"\nSome of the questions should refer to specific quotes in the passage. When quoting from the passage, include the line number.\nRepresent the question in JSON array format as follows, and don't include anything other than the JSON representation in your response: {question: string, answers: string[], correct_answer_index: number, category: string}[]"},
            {"role": "assistant", "content": json.dumps(data["question_set"][0])}
        ]
    ]
    for question in data["question_set"][1:]:
        messages.append([
            {"role": "user", "content": "Generate another difficult SAT reading question for this passage in the same format."},
            {"role": "assistant", "content": json.dumps(question)}
        ])

with open(sys.argv[1] + "-training.jsonl", "w") as f:
    for message_set in messages:
        f.write(json.dumps({"messages": message_set}) + "\n")