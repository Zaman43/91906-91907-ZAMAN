import tkinter as tk

class Start:
    def __init__(self, root):  # init is constructor for the class
        self.root = root
        self.root.title("Math Quest: Adventure Begins")
        self.root.geometry("400x350")
        self.root.configure(bg="#3e2f1c")  # Dark brown parchment color
        self.main_menu()

    def main_menu(self):
        title_style = {
            "font": ("Papyrus", 24, "bold"),  # adventure-y font
            "bg": "#8b6e3a",  # golden brown
            "fg": "#fdf6e3",  # parchment white
            "width": 25,
            "pady": 15,
            "relief": "ridge",
            "bd": 5,
        }
        tk.Label(self.root, text="~ Math Quest ~", **title_style).pack(pady=20)

        button_style = {
            "bg": "#6b4c17",  # rustic dark gold
            "fg": "#fdf6e3",  # parchment white
            "font": ("Courier", 14, "bold"),
            "width": 22,
            "relief": "raised",
            "bd": 4,
            "activebackground": "#a67c00",
        }
        exit_button_style = button_style.copy()
        exit_button_style.update({"bg": "#8b1a1a", "activebackground": "#bf3030"})

        tk.Button(self.root, text="Start New Quest", **button_style).pack(pady=7)
        tk.Button(self.root, text="Continue Adventure", **button_style).pack(pady=7)
        tk.Button(self.root, text="View Scrolls (Instructions)", **button_style).pack(pady=7)
        tk.Button(self.root, text="Exit Journey", command=self.root.destroy, **exit_button_style).pack(pady=25)

# Starts the app
root = tk.Tk()
app = Start(root)
root.mainloop()
