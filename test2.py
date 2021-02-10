import openai

# Retrieve and use API key
key_file = open("mykey.env", "r")
box = key_file.read()
key = box[17:60]
openai.api_key = key

engine_List = ["davinci", "curie", "ada", "babbage"]

print("\n\n>>>> Welcome to OpenAI's GPT-3 Playground <<<<\n\n")

def user_prompt():
    print("Your engine options are: \n")
    print(engine_List)
    print("\nPlease choose an engine")

    ## User input params

    #Input Engine
    corr_engine = False

    while corr_engine == False:
        engine = input("Input engine ID: ")
        try:
            engine_List.index(engine)
            
        except ValueError:
            print("Try Again")
            continue
        
        corr_engine = True

    corr_engine = False

    #Input Prompt
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("(Tip) Providing examples of desired outputs for given inputs")
    print("helps the AI a lot with understanding what it is being told to do.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    user_input = input("Enter prompt: ")

    #Input Max Tokens
    corr_tokens = False

    while corr_tokens == False:
        try:
            tok = int(input("Enter desired max number of tokens: "))
            if tok > 0 and tok < 2048:
                corr_tokens = True
        except ValueError:
            print("Please enter a number between 0 and 2048")

            
    corr_tokens = False

    # Response
    response = str(openai.Completion.create(engine="davinci", prompt=user_input, max_tokens=tok))
    output = []
    output = response.splitlines()
    out_text = str(output[6])
    print("\nResponse: ")
    print(out_text[14:]) # Prints the output inside the text: bracket
    #print(response)

user_prompt()


def retry():
    yes_no = ["y", "yes", "Y", "Yes", "N", "n", "No", "no"]
    print("\nTry another prompt?")
    corr_entry = False
    while corr_entry == False:
        restart = input("y / n: ")
        try:
            yes_no.index(restart)
            
        except ValueError:
            print("Invalid input. Please do 'y' for yes, 'n' for no.")
            continue
        
        corr_entry = True

    corr_entry = False

    finish = False
    while finish == False:
        if yes_no.index(restart) <= 3:
            user_prompt()
            retry()
        else:
            print("\n\nGoodbye!")
            finish = True
            exit

retry()