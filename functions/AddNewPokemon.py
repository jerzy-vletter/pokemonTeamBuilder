from tkinter import messagebox
from CheckInput import checkinput
from getters.Getweaknesses import getweaknesses


def addnewpokemon(type1, type2):  # todo add functionality for both the weaknesses,
    # todo combine both weaknesses are compare them against each other to see if it is a 2x or 4x weakness
    # todo return it to a storage space so it can be used against all other pokemon on the team

    inputvalid = checkinput(type1, type2)

    if inputvalid:
        weaknesses1 = getweaknesses(type1)
        weaknesses2 = getweaknesses(type2)
    else:
        messagebox.showinfo("WARNING", "One or more of the inputted types don't exist")
