
def settyperesistances():  # sets all the types a Pokémon is resistant to
    # from the type chart, used the 1/2 tiles

    valid_types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying",
                   "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
    typeresistances = {}
    key = len(typeresistances)

    for ptype in valid_types:
        match ptype:
            case "normal":
                ptype = valid_types[key]
                resistances = []
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "fire":
                ptype = valid_types[key]
                resistances = ["fire", "grass", "ice", "bug", "steel", "fairy"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "water":
                ptype = valid_types[key]
                resistances = ["fire", "water", "ice", "steel"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "grass":
                ptype = valid_types[key]
                resistances = ["water", "grass", "electric", "ground"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "electric":
                ptype = valid_types[key]
                resistances = ["electric", "flying", "steel"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "ice":
                ptype = valid_types[key]
                resistances = ["ice"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "fighting":
                ptype = valid_types[key]
                resistances = ["bug", "rock", "dark"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "poison":
                ptype = valid_types[key]
                resistances = ["grass", "fighting", "poison", "bug", "fairy"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "ground":
                ptype = valid_types[key]
                resistances = ["poison", "rock"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "flying":
                ptype = valid_types[key]
                resistances = ["grass", "fighting", "bug"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "psychic":
                ptype = valid_types[key]
                resistances = ["fighting", "psychic"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "bug":
                ptype = valid_types[key]
                resistances = ["grass", "fighting", "ground"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "rock":
                ptype = valid_types[key]
                resistances = ["normal", "fire", "poison", "flying"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "ghost":
                ptype = valid_types[key]
                resistances = ["poison", "bug"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "dragon":
                ptype = valid_types[key]
                resistances = ["fire", "water", "grass", "electric"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "dark":
                ptype = valid_types[key]
                resistances = ["ghost", "dark"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "steel":
                ptype = valid_types[key]
                resistances = ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "dragon", "steel", "fairy"]
                typeresistances[key] = [ptype, resistances]
                key += 1
                continue
            case "fairy":
                ptype = valid_types[key]
                resistances = ["fighting", "bug", "dark"]
                typeresistances[key] = [ptype, resistances]

    return typeresistances
