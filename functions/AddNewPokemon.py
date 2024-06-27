
from tkinter import messagebox
from CheckInput import checkinput


def addnewpokemon():  # todo add what happens if the input was valid

    inputvalid = checkinput()

    if inputvalid:
        ...
    else:
        messagebox.showinfo("WARNING", "Values inputted where non valid")
