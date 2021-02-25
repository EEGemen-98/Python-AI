import openai

# Retrieve and use API key
key_file = open("mykey.env", "r")
box = key_file.read()
key = box[17:60]
openai.api_key = key

# Prompt examples
exm_file = open("examples.txt", "r")
examples = exm_file.read()

def getPrompt(text_in):
    return str(openai.Completion.create(
        engine="davinci", 
        prompt=examples + text_in, 
        max_tokens=30, 
        temperature= 0.72,
        frequency_penalty=0.3,
        presence_penalty=0.5,
        best_of=2,
        stop="\n\n"))