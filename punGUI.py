import tkinter as tk
from tkinter import *
from gpt3_access import getPrompt

# Root GUI object
root = tk.Tk()

# Translates input text into pun version
def generate():
    originalText = str(input.get())
    response = getPrompt(originalText)
    print(response)
    
    # Disect the actual output text from entire resposne
    outPiece = []
    outPiece = response.splitlines()
    out_text = str(outPiece[6])
    output.insert(1, out_text[22:-1])

inputLabel = Label(root, text="Enter a sentence: ")
inputLabel.grid(row=0, column=0)
inputLabel.pack()

# Input text box
input = Entry(root, width=50)
input.pack()

# Generate pun button
genButton = Button(root, text="Punify", command=generate)
genButton.pack()

# Output box
output = Entry(root, width=50)
output.pack()


root.mainloop()