import tkinter as tk
from tkinter import *
from gpt3_access import getPrompt

# Root GUI object
root = tk.Tk()
root.title('Pun Generator')
root.geometry("450x200")

# CHeck if text is empty
def isEmpty(text):
    print("Empty text")
    return str(text.get(1.0,tk.END)) == ""

# Translates input text into pun version
def generate():
    if isEmpty(user_input) is True:
        user_input.insert(1.0, 'Please write something.')
        return
    
    output.delete(1.0, tk.END)
    originalText = str(user_input.get(1.0, tk.END))
    response = getPrompt(originalText)
    print(response)
    
    # Disect the actual output text from entire resposne
    outPiece = []
    outPiece = response.splitlines()
    out_text = str(outPiece[6])
    output.insert(1.0, out_text[20:-1])

# Input Label
inputLabel = Label(root, text="Enter a sentence: ")
inputLabel.grid(row=0, column=0)
inputLabel.pack()

# Input text box
user_input = Text(root, width=50, height=3)
user_input.pack()

# Generate pun button
genButton = Button(root, text="Punify", bg="#ff704d", command=generate, padx=10, pady=5)
genButton.pack()

# Output Label
output_label = Label(root, text="Punny Version:")
output_label.pack()

# Output box
output = Text(root, width=50, height=3)
output.pack()


root.mainloop()