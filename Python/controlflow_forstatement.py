def for_basic():
    # Declared a sample variabel
    data = [1, 5, 2, 4]
    count = 0

    # This is how we get all data in list using FOR syntax
    for data in data:
        count += data

    print(count)

    # How to combine IF with FOR Statement
    data.clear()
    data = ['Ice Cream', 'MC Donald', 'Pizza Hut', 'Hehe']
    for a in data[:]:
        if len(a) >= 8:
            data.insert(0, a)

    print(data)

    # How to make iteration
    number = []
    for x in range(5):
        number.append(x)

    print(number)

    #