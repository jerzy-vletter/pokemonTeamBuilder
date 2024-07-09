
from tkinter import messagebox


def checkinput(type1, type2):
    valid_types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying",
                   "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
    valid_exception = "none"

    if type1 == type2:
        messagebox.showinfo("WARNING", "Both types cannot be the same type")
        return "quit"

    if type1 not in valid_types and type1 != valid_exception:
        return False
    elif type2 not in valid_types and type2 != valid_exception:
        return False
    else:
        return True
