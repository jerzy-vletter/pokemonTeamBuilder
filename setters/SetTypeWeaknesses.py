
def settypeweaknesses():
    valid_types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying",
                   "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
    typeweaknesses = {}
    key = len(typeweaknesses)

    for ptype in valid_types:
        match ptype:
            case "normal":
                ptype = valid_types[key]
                weaknesses = ["fighting"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "fire":
                ptype = valid_types[key]
                weaknesses = ["water", "ground", "rock"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "water":
                ptype = valid_types[key]
                weaknesses = ["grass", "electric"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "grass":
                ptype = valid_types[key]
                weaknesses = ["fire", "ice", "poison", "flying", "bug"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "electric":
                ptype = valid_types[key]
                weaknesses = ["ground"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "ice":
                ptype = valid_types[key]
                weaknesses = ["fire", "fighting", "rock", "steel"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "fighting":
                ptype = valid_types[key]
                weaknesses = ["flying", "psychic", "fairy"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "poison":
                ptype = valid_types[key]
                weaknesses = ["ground", "psychic"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "ground":
                ptype = valid_types[key]
                weaknesses = ["water", "grass", "ice"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "flying":
                ptype = valid_types[key]
                weaknesses = ["electric", "ice", "rock"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "psychic":
                ptype = valid_types[key]
                weaknesses = ["bug", "ghost", "dark"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "bug":
                ptype = valid_types[key]
                weaknesses = ["fire", "flying", "rock"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "rock":
                ptype = valid_types[key]
                weaknesses = ["water", "grass", "fighting", "ground", "steel"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "ghost":
                ptype = valid_types[key]
                weaknesses = ["ghost", "dark"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "dragon":
                ptype = valid_types[key]
                weaknesses = ["ice", "dragon", "fairy"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "dark":
                ptype = valid_types[key]
                weaknesses = ["fighting", "bug", "fairy"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "steel":
                ptype = valid_types[key]
                weaknesses = ["fire", "fighting", "ground"]
                typeweaknesses[key] = [ptype, weaknesses]
                key += 1
                continue
            case "fairy":
                ptype = valid_types[key]
                weaknesses = ["poison", "steel"]
                typeweaknesses[key] = [ptype, weaknesses]

    return typeweaknesses
