def increment_function(num):
    return lambda x: x + num

def pairs():
    data = [(2001, 'nayaka'), (2000, 'shabrina'), (2000, 'risky')]

    data.sort(key=lambda pair: pair[1])
    return pairs