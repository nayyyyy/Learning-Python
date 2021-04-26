def dictionary_basic():
    # Declare new Dictionary. Remember, you cant include same index at first
    data_dict = {
        2001: 'Nayaka',
        2000: 'Shabrina'
    }

    # Check is it Corret
    print(isinstance(data_dict, dict))

    # You can get element by key
    print(data_dict[2001])
    print(data_dict[2000])

    # You can check is there any data on your dictionary
    print(2001 in data_dict)
    print(2004 not in data_dict)

    # Change data in dictionary
    data_dict[2001] = 'Kanaka'
    print(data_dict[2001])

    # Add new key in dictionary
    data_dict[1112] = 'Birthday'
    print(data_dict[1112])

    # Convert from dictionary to list
    print(list(data_dict))

    # Using sort if you want sort it
    print(sorted(data_dict))

    # It also can delete dictionary data
    del data_dict[2000]

    # Comperhansion method can made a dictionary
    data_dict.clear()
    data_dict = {x: x**4 for x in (2, 4, 5)}
    print(data_dict)

    # You can make a dictionary like this
    data_dict.clear()
    data_dict = dict(nayaka=2001, shabrina=2000)
    print(data_dict)
