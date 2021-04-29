def function_fibbonaciex(limit):
    # Make a fibbonaci
    data = []
    a, b = 1, 1
    while b < limit:
        a += b
        a, b = b, a
        data.append(a)

    return data


def function_message(name):
    # Make a messageA with function return
    return 'Hello ' + name


def function_messageb(name):
    # Make a messageB with function return
    return name + " from Indonesia"


def function_compose(name):
    # Combine message A & B
    return function_message(name) + function_messageb(name)


def function_returnfunction(name):
    # return function in function
    def get_message():
        return "Hello world!"

    return get_message()
