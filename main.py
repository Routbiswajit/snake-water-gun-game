"""
Gun / Water / Snake — Tkinter GUI version

Rules (classic rock-paper-scissors style, 3-way cycle):
    gun   beats snake
    water beats gun
    snake beats water
"""

import random
import tkinter as tk
from tkinter import font as tkfont

CHOICES = {0: "Gun", 1: "Water", 2: "Snake"}
EMOJI = {0: "\U0001F52B", 1: "\U0001F4A7", 2: "\U0001F40D"}  # gun, water drop, snake

# what each choice beats: key beats value
BEATS = {0: 2, 1: 0, 2: 1}


def determine_result(you: int, computer: int) -> str:
    """Return 'draw', 'win', or 'lose' from the human player's perspective."""
    if you == computer:
        return "draw"
    elif BEATS[you] == computer:
        return "win"
    else:
        return "lose"


class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gun · Water · Snake")
        self.root.geometry("420x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self.score_you = 0
        self.score_computer = 0

        title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        result_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        choice_font = tkfont.Font(family="Helvetica", size=13)
        button_font = tkfont.Font(family="Helvetica", size=14)

        tk.Label(
            root, text="Gun · Water · Snake", font=title_font,
            bg="#1e1e2f", fg="white"
        ).pack(pady=(20, 10))

        self.score_label = tk.Label(
            root, text="You: 0    Computer: 0", font=choice_font,
            bg="#1e1e2f", fg="#aaaaaa"
        )
        self.score_label.pack(pady=(0, 15))

        self.choices_label = tk.Label(
            root, text="Make your move!", font=choice_font,
            bg="#1e1e2f", fg="white", justify="center"
        )
        self.choices_label.pack(pady=(0, 10))

        self.result_label = tk.Label(
            root, text="", font=result_font,
            bg="#1e1e2f", fg="#4caf50"
        )
        self.result_label.pack(pady=(0, 20))

        button_frame = tk.Frame(root, bg="#1e1e2f")
        button_frame.pack(pady=10)

        for value, label in CHOICES.items():
            btn = tk.Button(
                button_frame,
                text=f"{EMOJI[value]}\n{label}",
                font=button_font,
                width=8,
                height=3,
                bg="#3a3a5c",
                fg="white",
                activebackground="#55558a",
                activeforeground="white",
                relief="flat",
                command=lambda v=value: self.play(v),
            )
            btn.pack(side="left", padx=8)

        tk.Button(
            root, text="Reset Score", font=choice_font,
            bg="#2a2a40", fg="#cccccc", relief="flat",
            command=self.reset_score,
        ).pack(pady=(25, 0))

    def play(self, you: int):
        computer = random.choice(list(CHOICES.keys()))
        result = determine_result(you, computer)

        self.choices_label.config(
            text=f"You: {EMOJI[you]} {CHOICES[you]}    "
                 f"Computer: {EMOJI[computer]} {CHOICES[computer]}"
        )

        if result == "draw":
            self.result_label.config(text="It's a draw!", fg="#f0c419")
        elif result == "win":
            self.score_you += 1
            self.result_label.config(text="You win! \U0001F389", fg="#4caf50")
        else:
            self.score_computer += 1
            self.result_label.config(text="You lose!", fg="#e74c3c")

        self.score_label.config(
            text=f"You: {self.score_you}    Computer: {self.score_computer}"
        )

    def reset_score(self):
        self.score_you = 0
        self.score_computer = 0
        self.score_label.config(text="You: 0    Computer: 0")
        self.choices_label.config(text="Make your move!")
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()