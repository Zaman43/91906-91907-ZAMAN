import tkinter as tk

class Start:
    def __init__(self, root):#init is used as constructor for class
        self.root = root
        self.root.title("Math Quest")
        self.root.geometry("300x300")
        self.root.configure(bg="#2e4a2b")#dark green
        self.main_menu()

    def main_menu(self):
        tk.Label(
            self.root,
            text="Math Quest",
            font=("Arial", 18, "bold"),
            bg="#7d7d7d",#stone gray 
            fg="#d4af37",#gold 
            width=20
        ).pack(pady=20)

        button_style = {
            "bg": "#7b1414",#burgundy 
            "fg": "#d4af37",#gold 
            "font": ("Arial", 11, "bold"),
            "width": 20
        }
        exit_button_style = {
            "bg": "#5a0f0f",#burgundy 
            "fg": "#d4af37",#gold 
            "font": ("Arial", 11, "bold"),
            "width": 20
        }

        tk.Button(self.root, text="Start New Game", **button_style).pack(pady=5)
        tk.Button(self.root, text="Continue Progress", **button_style).pack(pady=5)
        tk.Button(self.root, text="View Instructions", **button_style).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.destroy, **exit_button_style).pack(pady=20) #destroy will close window completely

# Starts my app
root = tk.Tk()
app = Start(root)
root.mainloop()
