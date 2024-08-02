import os
import tkinter as tk
from tkinter import scrolledtext
import json
from difflib import get_close_matches
from tkinter import simpledialog
from tkinter import messagebox

class ChatBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chat Bot")

        self.chat_history = scrolledtext.ScrolledText(master, width=50, height=20)
        self.chat_history.pack(padx=10, pady=10)

        self.user_input = tk.Entry(master, width=40)
        self.user_input.pack(padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

        self.file_path = 'knowledge_base.json'
        self.load_knowledge_base()

    def load_knowledge_base(self):
        try:
            with open(self.file_path, 'r') as file:
                self.knowledge_base = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            self.knowledge_base = {"knowledge": {}}
        except json.JSONDecodeError:
            print(f"Error: Unable to decode JSON from file '{self.file_path}'. Make sure it contains valid JSON syntax.")
            self.knowledge_base = {"knowledge": {}}

    def save_knowledge_base(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.knowledge_base, file, indent=2)

    def send_message(self):
        user_input = self.user_input.get()
        self.user_input.delete(0, tk.END)

        if user_input.lower() == 'quit':
            self.master.quit()
            return

        if user_input in self.knowledge_base.get("knowledge", {}):
            bot_response = self.knowledge_base["knowledge"][user_input]
            self.display_message(f'Bot: {bot_response}')
        else:
            best_match = self.find_best_match(user_input, self.knowledge_base.get("knowledge", {}).keys())

            if best_match:
                response = messagebox.askquestion("Bot", f'Did you mean "{best_match}"?')
                if response == 'yes':
                    bot_response = self.knowledge_base["knowledge"][best_match]
                    self.display_message(f'Bot: {bot_response}')
                    return

            new_answer = simpledialog.askstring("Bot", "I don't know the answer. Can you teach me?")
            if new_answer:
                self.knowledge_base.setdefault("knowledge", {})[user_input] = new_answer
                self.save_knowledge_base()
                self.display_message('Bot: Thank you! I learned something new.')

    def find_best_match(self, user_question, questions):
        matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
        return matches[0] if matches else None

    def display_message(self, message):
        self.chat_history.insert(tk.END, message + '\n')
        self.chat_history.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    chat_bot_gui = ChatBotGUI(root)
    root.mainloop()
