
from setters.SetTypeStrengths import settypestrengths


def getstrengths(ptype):
    typestrengths = settypestrengths()

    if ptype == "none":
        strengths = []
        return strengths

    for item in range(len(typestrengths)):
        itemtype = typestrengths[item][0]
        if itemtype == ptype:
            strengths = typestrengths[item][1]
            return strengths
        else:
            continue

    return []
