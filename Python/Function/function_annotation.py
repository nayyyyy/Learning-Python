def eat(food: str, drink: str) -> str:
    """
    This function has food arg, drink arg, and return value final
    """
    return food + ' and ' + drink


def check_annotation():
    return eat.__annotations__
