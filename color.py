import tkinter as tk
import random

class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Identifying Game")

        self.colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown"]
        self.score = 0

        self.create_ui()

    def create_ui(self):
        self.color_label = tk.Label(self.root, text="", font=("Arial", 18))
        self.color_label.pack(pady=20)

        self.input_entry = tk.Entry(self.root, font=("Arial", 14))
        self.input_entry.pack(pady=10)

        self.check_button = tk.Button(self.root, text="Check", command=self.check_guess)
        self.check_button.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.new_game_button = tk.Button(self.root, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=10)

        self.new_game()

    def new_game(self):
        self.current_color = random.choice(self.colors)
        self.current_font_color = random.choice(self.colors)
        self.color_label.config(text=self.current_color, fg=self.current_font_color)
        self.input_entry.delete(0, tk.END)
        self.update_score()

    def check_guess(self):
        user_guess = self.input_entry.get().lower()
        if user_guess == self.current_font_color:
            self.score += 1
            self.new_game()
        else:
            self.score -= 1
            self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorGame(root)
    root.mainloop()
