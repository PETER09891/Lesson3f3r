import random
import tkinter as tk

# Create window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

choices = ["Rock", "Paper", "Scissors"]

# Function to play game
def play(user):
    comp = random.choice(choices)

    if user == comp:
        result = "Tie"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        result = "You Win"
    else:
        result = "You Lose"

    label.config(text="You: " + user +
                      "\nComputer: " + comp +
                      "\nResult: " + result)

# Label
label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 11))
label.pack(pady=20)

# Buttons with width
rock_btn = tk.Button(root, text="Rock", width=15, command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=15, command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors"))
scissors_btn.pack(pady=5)

root.mainloop()