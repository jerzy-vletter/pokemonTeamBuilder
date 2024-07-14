
from setters.SetTypeResistances import settyperesistances


def getresistances(ptype):
    typeresistances = settyperesistances()

    if ptype == "none":
        resistances = []
        return resistances

    for item in range(len(typeresistances)):
        itemtype = typeresistances[item][0]
        if itemtype == ptype:
            resistances = typeresistances[item][1]
            return resistances
        else:
            continue

    return []
