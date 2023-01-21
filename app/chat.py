from datetime import date
from duckduckgo_search import ddg_answers
import random
import json
import os
import requests
f = open('static/intents.json')
data = json.load(f)
data = data['intents']

os.path.join(f"static/{date.today()}.txt")
API_URL = "https://api-inference.huggingface.co/models/Qiliang/bart-large-cnn-samsum-ChatGPT_v3"
headers = {"Authorization": "Bearer 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"}

def querychat(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
def chat(query):
    dictionary = {}
    for i in data:
        if query.lower() in (str(i['patterns'])).lower():
            final = random.choice(i["responses"])
            break
        else:
            final = ""
    if final == "":
        results = ddg_answers(query, related=True)
        if len(results) < 1:
            output = querychat({"inputs": "The answer to the universe is",})
            final = output[0]['generated_text']
        else:            
            final = ("1 : "+results[0]["text"]+"\n"+"2 : "+results[1]["text"]+"\n"+"3 : "+results[2]["text"])

    dictionary[query] = final
    print(dictionary)
    if final == "":
        final = "Please Remodify your query..."
    # f = open(f"static/{date.today()}.txt", 'a')
    # f.write(str(dictionary)+"\n")
    # print(final)
    return {"generated_text":final}