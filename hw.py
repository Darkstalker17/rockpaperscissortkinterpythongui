from tkinter import *
import random

root = Tk()
root.geometry("800x600")
root.title("ROCK*PAPER*SCISSORS")

label = Label(root, text="Lets play rock paper Scissors!", font=("Impact", 50))
label.place(x=0, y=50, width=800, height=70)

label1 = Label(root, text="Please choose an option: ", font=("Impact", 35))
label1.place(x=0, y=400, width=800, height=70)

result_label = Label(root, text="", font=("Impact", 30))
result_label.place(x=0, y=300, width=800, height=50)

def play(choice):
    global user_choice
    comp_choice = random.choice(["rock", "paper", "scissors"])
    user_choice = choice

    if user_choice == "rock":
        paper.config(state="disabled")
        scissors.config(state="disabled")
    elif user_choice == "paper":
        rock.config(state="disabled")
        scissors.config(state="disabled")
    elif user_choice == "scissors":
        rock.config(state="disabled")
        paper.config(state="disabled")

    if user_choice == comp_choice:
        result = f"TIE! COMPUTER CHOSE {comp_choice.upper()}"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        result = f"YOU WON! COMPUTER CHOSE {comp_choice.upper()}"
    else:
        result = f"YOU LOST! COMPUTER CHOSE {comp_choice.upper()}"

    result_label.config(text=result)

    rock.config(state="normal")
    paper.config(state="normal")
    scissors.config(state="normal")

rock = Button(root, text="ROCK", command=lambda: play("rock"))
paper = Button(root, text="PAPER", command=lambda: play("paper"))
scissors = Button(root, text="SCISSORS", command=lambda: play("scissors"))

rock.place(x=50, y=500, width=200, height=50)
paper.place(x=300, y=500, width=200, height=50)
scissors.place(x=550, y=500, width=200, height=50)

root.mainloop()
