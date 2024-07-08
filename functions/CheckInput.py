

def checkinput(type1, type2):
    valid_types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying",
                   "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
    valid_exception = "none"

    if type1 not in valid_types:
        return False

    if type2 not in valid_types or type2 != valid_exception:
        return False
