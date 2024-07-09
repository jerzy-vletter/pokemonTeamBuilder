from tkinter import messagebox
from functions.CheckInput import checkinput
from getters.Getweaknesses import getweaknesses


def addnewpokemon(type1, type2):
    # todo return it to a storage space so it can be used against all other pokemon on the team

    doubleweak = []
    quadweak = []
    weaknesses = {}
    key = 0

    weaknesses1 = getweaknesses(type1)
    weaknesses2 = getweaknesses(type2)

    for w in weaknesses1:
        doubleweak.append(w)
    for w in weaknesses2:
        if w in doubleweak:
            doubleweak.remove(w)
            quadweak.append(w)
        else:
            doubleweak.append(w)

    for weakness in doubleweak:
        weaknesses[key] = [weakness, "x2"]
        key += 1
    for weakness in quadweak:
        weaknesses[key] = [weakness, "x4"]
        key += 1
    print(weaknesses)
