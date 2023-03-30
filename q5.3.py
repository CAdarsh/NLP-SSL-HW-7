import json
import random
import math



secret_key = "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"
import os
import openai

openai.api_key = secret_key

def call_davinci(prompt, golden_answer):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(f'\nCompletion: {response["choices"][0]["text"].strip()}')
    print(f'Golden Answer: {golden_answer}')
    print(f'Score: {1 if response["choices"][0]["text"].strip() == str(golden_answer) else 0}\n')
    
    # print(response["choices"][0]["text"].strip() == str(golden_answer))
    return 1 if response["choices"][0]["text"].strip() == str(golden_answer) else 0


data = []
# Open the file in read mode
with open('dev.jsonl', 'r') as f:
    # Load the JSON data from the file
    for line in f:
        data.append(json.loads(line))

selected_propmts = []



selected = True
score = 0
iterations = 30

for i in range(iterations):
    prompt = ""
    for a in range(4):
        selected = True
        while selected:
            random_val = math.floor(random.random() * len(data))
            if random_val in selected_propmts or data[random_val]["answer"] == False:
                continue
            selected_propmts.append(random_val)
            prompt += f'Question: {data[random_val]["question"]}\nAnswer: {data[random_val]["answer"]}\n'
            selected = False
    
    selected = True
    while selected:
        random_val = math.floor(random.random() * len(data))
        if random_val in selected_propmts or data[random_val]["answer"] == True:
            continue
        selected_propmts.append(random_val)
        prompt += f'Question: {data[random_val]["question"]}\nAnswer: {data[random_val]["answer"]}\n'
        selected = False
        
    test_data = {}
    selected = True
    
    while selected:    
        random_val = math.floor(random.random() * len(data))
        if random_val in selected_propmts:
            continue
        test_data = { "question": data[random_val]["question"],  "answer": data[random_val]["answer"] }

        prompt += f'Question: {test_data["question"]}\nAnswer: '

        print(prompt)
        score += call_davinci(prompt, test_data["answer"])
        selected = False
    
print(f'Accuracy: {score/iterations * 100}')
        
    