import openai

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Ssebowa chatbot"
def openai_create(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response.choices[0].text



def chatgpt_clone(input):
    print(input)
    output = openai_create(input)
    return output.strip(".\n\n")