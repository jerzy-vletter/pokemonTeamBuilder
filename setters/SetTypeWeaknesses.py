
def settypeweaknesses():
    valid_types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying",
                   "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
    typeweaknesses = {}
    key = len(typeweaknesses)

    if key == 0:
        ptype = valid_types[0]
        weaknesses = ["fighting"]
        typeweaknesses[key] = [ptype, weaknesses]
    else:
        key = len(typeweaknesses)
        for ptype in valid_types:
            match ptype:
                case "normal":
                    continue
                case "fire":
                    ptype = valid_types[key]
                    weaknesses = ["water", "ground", "rock"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "water":
                    ptype = valid_types[key]
                    weaknesses = ["grass", "electric"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "grass":
                    ptype = valid_types[key]
                    weaknesses = ["fire", "ice", "poison", "flying", "bug"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "electric":
                    ptype = valid_types[key]
                    weaknesses = ["ground"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "ice":
                    ptype = valid_types[key]
                    weaknesses = ["fire", "fighting", "rock", "steel"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "fighting":
                    ptype = valid_types[key]
                    weaknesses = ["flying", "psychic", "fairy"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "poison":
                    ptype = valid_types[key]
                    weaknesses = ["ground", "psychic"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "ground":
                    ptype = valid_types[key]
                    weaknesses = ["water", "grass", "ice"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "flying":
                    ptype = valid_types[key]
                    weaknesses = ["electric", "ice", "rock"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "psychic":
                    ptype = valid_types[key]
                    weaknesses = ["bug", "ghost", "dark"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "bug":
                    ptype = valid_types[key]
                    weaknesses = ["fire", "flying", "rock"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "rock":
                    ptype = valid_types[key]
                    weaknesses = ["water", "grass", "fighting", "ground", "steel"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "ghost":
                    ptype = valid_types[key]
                    weaknesses = ["ghost", "dark"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "dragon":
                    ptype = valid_types[key]
                    weaknesses = ["ice", "dragon", "fairy"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "dark":
                    ptype = valid_types[key]
                    weaknesses = ["fighting", "bug", "fairy"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "steel":
                    ptype = valid_types[key]
                    weaknesses = ["fire", "fighting", "ground"]
                    typeweaknesses[key] = [ptype, weaknesses]
                case "fairy":
                    ptype = valid_types[key]
                    weaknesses = ["poison", "steel"]
                    typeweaknesses[key] = [ptype, weaknesses]

    return typeweaknesses
