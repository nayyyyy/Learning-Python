def if_basic():
    x = 14
    text = ''

    if x < 0:
        text = 'Number less then 0'
    elif x == 0:
        text = 'Number equal 0'
    else:
        text = 'Number more then 0'

    print(text)