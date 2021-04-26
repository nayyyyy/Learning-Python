def string_Type():
    # String with single Quotes
    name = 'Hello'
    print(name)

    # String with Double Quotes
    name = "Hello"
    print(name)

    # \ can be used to escape quotes or using a double quotes String
    text = "Hello my name's Nayaka"
    print(text)

    # \n means new line
    text = "Hello.\nMy name is Nayaka"
    print(text)

    # String can be indexed. Cause string is List of Char
    print(name[0])  # H
    print(name[1])  # e
    print(name[2])  # l
    print(name[3])  # l
    print(name[4])  # o
    print(isinstance(name[3], str))

    # You can slicing string like this
    print(name[2:4])  # llo
    print(name[4:1])  # olle

    # Or you can slicing a string like this
    print(name[:1] + name[3:])
    print(name[:2] + name[2:])

    # If you want slicing from 0 - ... Using this
    print(name[:4])
    print(name[2:])
    print(name[-3])

    # One way to remember how slices work is to think of the indices as
    # pointing between characters, with the left edge of the first character
    # numbered 0. Then the right edge of the last character of a string of n
    # characters has index n, for example:
    #
    # +---+---+---+---+---+
    #  | H | e | l | l | o |
    #  +---+---+---+---+---+
    #  0   1   2   3   4   5
    # -5  -4  -3  -2  -1

    # you can also addition the other string like this
    example = 'A' + name[1:]
    print(example)

    # You can count a length from string like this
    example = len(name)
    print(example)

    # And, if you feel the string was to long. You can type multiline like this once
    example = '''\
        Hello my name
        is Nayaka
    '''
    print(example)


def string_Operator():
    # This is some example of String operator
    a = 3 * 'you' + 'haha'
    b = 'He''llo'
    print(a)
    print(b)

    # You can also make a text using string addition operator
    text = (
        "put some text in here"
        "And voila, it's gonna be a text"
    )
    print(text)

    # You can also addition a string in a variabel
    a = 'Haha'
    b = ' Xixi'
    print(a + b)


def string_Method():
    text = " This is my First time learn, Python"

    # strip() has function to remove any whitespaces in text
    print(text.strip())

    # len() has function to count char in text include whitespace
    print(len(text))

    # lower() has function to return all string to lowercase
    print(text.lower())

    # upper() has function to return all string to UPPERCASE
    print(text.upper())

    # replace(a, b) has function to replace all Char 'a' to 'b'
    print(text.replace('i', 'e'))

    # split(a) has function to split text if there's contain 'a'
    print(text.split(','))

    # capitalize() Change first string to be Capitalize
    print(text.capitalize())

    # count(a) has function to count how much 'a' char
    print(text.count('i'))

    # find(a) has function to find start index from 'a' string
    print(text.find('is'))

    # title() has function to change all string being Capitalize
    print(text.title())

    # replace('a', 'b') has function to replace 'a' to 'b'
    print(text.replace('Python', 'Hython'))

    # join() has function to combine all string in a tuple
    data = ['Apple', 'Banana', 'Carrot']
    print(','.join(data))

    # isUpper() has function to return True if string was UPPERCASE
    text = 'NAYAKA'
    print(text.isupper())

    # isLower() has function to return True if string was lowercase
    print(text.islower())

    # isAlpha() has function to return True if all char was Alphabetic
    print(text.isalpha())

    # isdecimal() has function to return True if all char was Decimal
    text = '11122001'
    print(text.isdecimal())


def string_Formatting():
    year = 2001
    event = 'Birthday'

    # This is how to include variabel in Print
    print(f"This is formatting {year} {event}")

    # Other knowledge how to use Formatting
    yes = 11_12_2001
    no = 10_12_2001
    percen = yes / (yes + no)
    print('{:8} NO Votes {:2.2%}'.format(no, percen))

    # This is how to Representing a String
    text = 'Hello, World'
    a = 3.14
    b = 2000
    print(str(text))
    print(repr(text))
    print(str(1 / 2))

    # Repr() can be use in any Variabel
    print(repr((a, b, ('Nay', 'Cerdas'))))

    # Formating Decimal into string
    phi = 3.14159
    data = 16.3424323
    print(f'value of Phi is {phi:.3f}')
    print(f'value of data is {data:.5f}')

    # Make a table list data
    data_Base = {'Nayaka': 2001, 'Shabrina': 2000}
    sdata = ""

    for name, year in data_Base.items():
        sdata += f'{name:10}==>{year:7d}'
    print(sdata)

    # Also we can include text using format
    print("My name is {} and i'm from {}".format('Nayaka', 'Indonesia'))

    # We can include text using format, and choose what text we want to format first
    print("This is {0} and {1}".format('Ice Cream', 'Meatball'))

    # This is another way to formatting a string
    data_Format = 'Welcome to {name}, there is {count} menu'.format(
        name='Food Complex',
        count='10'
    )
    print(data_Format)

    # or you can do formating like this
    data_Format = '''\
    Welcome to {0}, there is {1} menu.
    Favourite menu in here is {food}.
    '''.format(
        'Food Complex',
        '100',
        food='Ikigai Chicken Mentai'
    )
    print(data_Format)

    # You can include data form tuple with Formatting
    data_Format = "Nayaka: {0[Nayaka]:d}, Shabrina: {0[Shabrina]:d}".format(data_Base)
    print(data_Format)

    # or you can do like this
    data_Format = "Nayaka: {Nayaka:d}, Shabrina: {Shabrina:d}".format(**data_Base)
    print(data_Format)
