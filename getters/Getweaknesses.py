
from setters.SetTypeWeaknesses import settypeweaknesses


def getweaknesses(ptype):
    typeweaknesses = settypeweaknesses()

    if ptype == "none":
        weaknesses = []
        return weaknesses

    for item in range(len(typeweaknesses)):
        itemtype = typeweaknesses[item][0]
        if itemtype == ptype:
            weaknesses = typeweaknesses[item][1]
            return weaknesses
        else:
            continue

    return []
