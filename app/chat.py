from datetime import date
from duckduckgo_search import ddg_answers
import random
import json
import os
f = open('static/intents.json')
data = json.load(f)
data = data['intents']

os.path.join(f"static/{date.today()}.txt")
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
        final = ("1 : "+results[0]["text"]+"\n"+"2 : "+results[1]["text"]+"\n"+"3 : "+results[2]["text"])

    dictionary[query] = final
    print(dictionary)
    f = open(f"static/{date.today()}.txt", 'a')
    f.write(str(dictionary)+"\n")
    print(final)
    return {"generated_text":final}