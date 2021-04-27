def function_unpackingauto(*data):
    return list(range(*data))

def function_unpackingmanual(*data):
    return list(data)

def function_unpackdict(first, second):
    return first + ", " + second