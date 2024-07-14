from getters.Getweaknesses import getweaknesses
from getters.Getresistances import getresistances


def addnewpokemon(type1, type2):
    # todo return it to a storage space so it can be used against all other pokemon on the team

    # setting arrays grouped by use case
    #   temp storage arrays to be used later (for combining 2 or more arrays /
    #   add to another array with additional info / removing values stored within)
    doubleweak = []
    quadweak = []
    resistances_found = []

    # final arrays used to print / check temp arrays against
    resistance = []
    weaknesses = {}

    key = 0

    weaknesses1 = getweaknesses(type1)
    weaknesses2 = getweaknesses(type2)
    resistance1 = getresistances(type1)
    resistance2 = getresistances(type2)

    for s in resistance1:
        resistance.append(s)
    for s in resistance2:
        if s in resistance:
            continue
        else:
            resistance.append(s)
            continue

    for w in weaknesses1:
        doubleweak.append(w)
        continue
    for w in weaknesses2:
        if w not in doubleweak:
            doubleweak.append(w)
            continue
        else:
            if w not in resistance:
                doubleweak.remove(w)
                quadweak.append(w)
                continue
            else:
                doubleweak.remove(w)
                continue

    for w in doubleweak:
        if w in resistance:
            resistances_found.append(w)

    for r in resistances_found:
        doubleweak.remove(r)

    for weakness in doubleweak:
        weaknesses[key] = [weakness, "x2"]
        key += 1

    for weakness in quadweak:
        weaknesses[key] = [weakness, "x4"]
        key += 1
    print(weaknesses)
