def integer_Data():
    # Integer Data
    a = 1
    b = -2352
    c = 24524314131

    print(isinstance(a, int))
    print(isinstance(b, int))
    print(isinstance(c, int))


def float_Data():
    # Float Data
    a = 3.14
    b = float(3)
    c = -3.14

    # Float can also be scientific number
    d = 35e3
    e = 31e4

    print(isinstance(a, float))
    print(isinstance(b, float))
    print(isinstance(c, float))
    print(d)
    print(e)


def bool_Data():
    # Boolean Data
    a = True
    b = False
    print(isinstance(a, bool))
    print(isinstance(b, bool))


def complex_Data():
    # Complex Data
    a = 5 + 2j
    b = 2 + 8j
    print(a + b)
    print(isinstance(a + b, complex))
