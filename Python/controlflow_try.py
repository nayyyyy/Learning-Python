def try_basic():
    # This is a simple way to make a try exception

    cond = False

    try:
        print(x)
    except NameError:
        cond = True

    print("Variabel was not declare: ",cond)

    # Make some modification with Throw Exception
    x = ''

    try:
        x += "Variabel Declare."
    except NameError:
        x += "Variabel was not declared"
    else:
        x += " Nothing Wrong"

    print(x)

    # Or you can make like this
    x = ''

    try:
        x += "Variabel Declare. "
    except NameError:
        x += "Variabel not declare"
    finally:
        x += "Check Success"

    print(x)