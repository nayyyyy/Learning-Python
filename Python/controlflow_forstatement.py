def for_basic():
    # Declared a sample variabel
    data = [1, 5, 2, 4]
    data_text = "Hello World"
    extract = []
    count = 0

    # This is how we get all data in list using FOR syntax
    for data in data:
        count += data

    print(count)

    for data_text in data_text:
        extract.append([data_text])

    print(extract)

    # How to combine IF with FOR Statement
    data = ['Ice Cream', 'MC Donald', 'Pizza Hut', 'Hehe']
    for a in data[:]:
        if len(a) >= 8:
            data.insert(0, a)

    print(data)

    # How to make iteration
    number = []
    for x in range(11):
        number.append(x)

    print(number)

    # Make a list being a text
    data.clear()
    data = ["My", "name", "is", "Nayaka"]
    text = ""

    for data in data:
        text += data + ' '

    print(text)

    # How to segment data in Dictionary
    del data
    data = {"Nayaka": 2001, "Shabrina": 2000, "Risky": 2000}
    name = []
    year = []

    for x, y in data.items():
        name.append(x)
        year.append(y)

    print(name)
    print(year)

    del name, year, data, text

    # get Coresponding Index & Value in Dictionaries
    index = []
    text = []

    for x, y in enumerate(['nay', 'ice', 'hot']):
        index.append(x)
        text.append(y)

    print(index, "&", text)

    # get data from list and return to sets
    del index, text

    name = ["nayaka", "shabrina", "risky"]
    year = [2001, 2000, 2000]
    combine = []

    for x, y in zip(name, year):
        combine.append("My name is {0}. I was born on {1}".format(x, y))

    print(combine)


def for_range():
    # this is how to made iteration more fast without for. All you need do is type RANGE
    data = list(range(10))
    print(data)

    data = list(range(5, 10))
    print(data)

    '''
        this is how to made Arithmetic Progression using range.
        range(x, y, z)
        x = First range Number
        y = Last range number
        z = Difference data
    '''
    data = list(range(10, 100, 4))
    print(data)
