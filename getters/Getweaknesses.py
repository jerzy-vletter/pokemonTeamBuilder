
from setters.SetTypeWeaknesses import settypeweaknesses


def getweaknesses(ptype):
    typeweaknesses = settypeweaknesses()

    for item in range(len(typeweaknesses)):
        itemtype = typeweaknesses[item][0]
        if itemtype == ptype:
            weaknesses = typeweaknesses[item][1]
        else:
            continue
    # noinspection PyUnboundLocalVariable
    return weaknesses  # warning suppression needed because it warns for something that is not going to be a problem
