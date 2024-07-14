
def settypestrengths():  # sets all the types a Pokémon is strong against
    
    valid_types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying",
                   "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
    typestrengths = {}
    key = len(typestrengths)

    for ptype in valid_types:
        match ptype:
            case "normal":
                ptype = valid_types[key]
                strengths = []
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "fire":
                ptype = valid_types[key]
                strengths = ["grass", "ice", "bug", "steel"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "water":
                ptype = valid_types[key]
                strengths = ["fire", "ground", "rock"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "grass":
                ptype = valid_types[key]
                strengths = ["water", "ground", "rock"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "electric":
                ptype = valid_types[key]
                strengths = ["water", "flying"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "ice":
                ptype = valid_types[key]
                strengths = ["grass", "ground", "flying", "dragon"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "fighting":
                ptype = valid_types[key]
                strengths = ["normal", "ice", "rock", "dark", "steel"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "poison":
                ptype = valid_types[key]
                strengths = ["grass", "fairy"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "ground":
                ptype = valid_types[key]
                strengths = ["fire", "electric", "poison", "rock", "steel"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "flying":
                ptype = valid_types[key]
                strengths = ["grass", "fighting", "bug"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "psychic":
                ptype = valid_types[key]
                strengths = ["fighting", "poison"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "bug":
                ptype = valid_types[key]
                strengths = ["grass", "psychic", "dark"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "rock":
                ptype = valid_types[key]
                strengths = ["fire", "ice", "flying", "bug"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "ghost":
                ptype = valid_types[key]
                strengths = ["psychic", "ghost"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "dragon":
                ptype = valid_types[key]
                strengths = ["dragon"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "dark":
                ptype = valid_types[key]
                strengths = ["psychic", "ghost"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "steel":
                ptype = valid_types[key]
                strengths = ["rock", "fairy"]
                typestrengths[key] = [ptype, strengths]
                key += 1
                continue
            case "fairy":
                ptype = valid_types[key]
                strengths = ["fighting", "dragon", "dark"]
                typestrengths[key] = [ptype, strengths]

    return typestrengths
