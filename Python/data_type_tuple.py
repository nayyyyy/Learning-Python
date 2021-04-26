def tuple_basic():
    # this is example of tuple
    data = ("Nayaka", "Alka", "Ganteng")

    # Want to make sure this is Tuple data
    print(isinstance(data, tuple))

    # This is how to print data on tuples
    for i in range(len(data) - 1):
        print(data[i])

    # Warning !!! You cant change data in tuple like list
    # And also, tuple can be make like a constructor

    data_constructor = tuple(("Apple", "Grapes", "Melon"))
    print(len(data_constructor))

    # Tuples can be initialize without bracket. Trust me
    data = "Apple", "Grapes", "Melon"
    print(data is data_constructor)

    # You know, tuple little bit same like List. You can made Tuple Nested
    data_final = data, data_constructor
    print(data_final)

    # If we want to clear tuple, How?? You just need to clear a bracket like this
    data = ()
    data_final = ()
    data_constructor = ()

    print(data)
    print(data_final)
    print(data_constructor)

    # This is how to make singleton tuple
    singleton_tuple = 3.14, 1112, 6.12
    print(singleton_tuple)
    print(len(singleton_tuple))
