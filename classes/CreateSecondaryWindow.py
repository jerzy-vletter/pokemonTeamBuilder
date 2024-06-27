
import tkinter as tk


class CreateSecondaryWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("add pokemon")
        self.attributes('-topmost', True)
        self.frame = tk.Frame(self)
        self.state = False
        self.minsize(300, 400)
