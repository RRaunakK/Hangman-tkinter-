import tkinter as tk
from tkinter import messagebox
import random

# List of words for the hangman game
WORDS = ["python", "hangman", "challenge", "programming", "developer", "interface"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        # Initialize game variables
        self.word_to_guess = random.choice(WORDS).upper()
        self.reveal_letters()
        self.guessed_word = [char if char.isalpha() else "_" for char in self.word_with_hints]
        self.attempts_left = 6
        self.guessed_letters = set()

        # Create UI elements
        self.word_label = tk.Label(root, text=" ".join(self.guessed_word), font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.info_label = tk.Label(root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 14))
        self.info_label.pack()

        self.letter_entry = tk.Entry(root, font=("Arial", 16))
        self.letter_entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", font=("Arial", 14), command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=self.reset_game)
        self.reset_button.pack(pady=10)

    def reveal_letters(self):
        # Randomly reveal a few letters of the word
        reveal_count = len(self.word_to_guess) // 3
        indices_to_reveal = random.sample(range(len(self.word_to_guess)), reveal_count)
        self.word_with_hints = ''.join(
            [self.word_to_guess[i] if i in indices_to_reveal else "_" for i in range(len(self.word_to_guess))]
        )

    def make_guess(self):
        letter = self.letter_entry.get().strip().upper()
        self.letter_entry.delete(0, tk.END)

        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if letter in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"You already guessed the letter '{letter}'.")
            return

        self.guessed_letters.add(letter)

        if letter in self.word_to_guess:
            for i, char in enumerate(self.word_to_guess):
                if char == letter:
                    self.guessed_word[i] = letter
            self.word_label.config(text=" ".join(self.guessed_word))

            if "_" not in self.guessed_word:
                messagebox.showinfo("Congratulations!", "You guessed the word correctly!")
                self.reset_game()
        else:
            self.attempts_left -= 1
            self.info_label.config(text=f"Attempts left: {self.attempts_left}")

            if self.attempts_left == 0:
                messagebox.showerror("Game Over", f"You lost! The word was '{self.word_to_guess}'.")
                self.reset_game()

    def reset_game(self):
        self.word_to_guess = random.choice(WORDS).upper()
        self.reveal_letters()
        self.guessed_word = [char if char.isalpha() else "_" for char in self.word_with_hints]
        self.attempts_left = 6
        self.guessed_letters = set()

        self.word_label.config(text=" ".join(self.guessed_word))
        self.info_label.config(text=f"Attempts left: {self.attempts_left}")
        self.letter_entry.delete(0, tk.END)

# Create the main Tkinter window
root = tk.Tk()
root.geometry("400x400")
game = HangmanGame(root)
root.mainloop()
