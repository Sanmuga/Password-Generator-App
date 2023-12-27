import tkinter as tk
from tkinter import ttk
import secrets
import string
import pyperclip
from ttkthemes import ThemedTk

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("300x200")  # Set initial window size

        # Apply a themed style
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Set up the main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create and place widgets
        self.label_length = ttk.Label(self.main_frame, text="Password Length:")
        self.label_length.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))

        self.entry_length = ttk.Entry(self.main_frame, width=5)
        self.entry_length.grid(row=0, column=1, sticky=tk.W, pady=(0, 10))

        self.button_generate = ttk.Button(self.main_frame, text="Generate Password", command=self.generate_password)
        self.button_generate.grid(row=1, column=0, columnspan=2, pady=(10, 0))
        self.button_generate.bind("<Enter>", self.on_enter_generate)
        self.button_generate.bind("<Leave>", self.on_leave_generate)

        self.label_result = ttk.Label(self.main_frame, text="")
        self.label_result.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        self.button_copy = ttk.Button(self.main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.button_copy.grid(row=3, column=0, columnspan=2, pady=(10, 0))
        self.button_copy.bind("<Enter>", self.on_enter_copy)
        self.button_copy.bind("<Leave>", self.on_leave_copy)

        # Configure some basic styling
        self.root.option_add('*TButton*Font', 'Helvetica 10 bold')
        self.root.option_add('*TLabel*Font', 'Helvetica 10')
        self.root.option_add('*TEntry*Font', 'Helvetica 10')

    def generate_password(self):
        try:
            length = int(self.entry_length.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            
            password = self.generate_random_password(length)
            self.label_result.config(text=f"Generated Password: {password}")
        except ValueError as e:
            self.label_result.config(text=f"Error: {e}")

    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

    def copy_to_clipboard(self):
        password = self.label_result.cget("text")
        password = password.split(":")[1].strip()  # Extract the password from the label text
        pyperclip.copy(password)

    def on_enter_generate(self, event):
        self.button_generate.configure(style="Hover.TButton")

    def on_leave_generate(self, event):
        self.button_generate.configure(style="TButton")

    def on_enter_copy(self, event):
        self.button_copy.configure(style="Hover.TButton")

    def on_leave_copy(self, event):
        self.button_copy.configure(style="TButton")

if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # You can change the theme (e.g., "scidblue", "equilux", "arc", etc.)
    app = PasswordGeneratorApp(root)
    root.mainloop()
