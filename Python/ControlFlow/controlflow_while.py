def while_basic():
    x = 4
    y = 3

    num = 1

    while x > 0:
        num *= y
        x -= 1

    print(num)