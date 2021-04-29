def set_basic():
    # Declared SET Variabel
    data_set = {"Apple", "Banana", "Cherry"}

    # Check is it Set Variabel or Not!
    print(isinstance(data_set, set))


def set_methods():
    # Declared SET Variabel
    data_set = {"Apple", "Banana", "Cherry", "Durian"}

    # You can use IN method on SET
    print("Cherry" in data_set)
    print("Grapes" in data_set)

    # You can use LEN to count how much data in SET
    print(len(data_set))

    # You can use ADD to add an item
    data_set.add("Extra")
    data_set.add("Flame")
    print(data_set)

    # You can use REMOVE to remove an item
    data_set.remove("Apple")
    data_set.remove("Durian")
    print(data_set)
    print(len(data_set))

    # Unique thinks you have to know, it also can use artimathic Operator
    a_data = {'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd'}
    b_data = {'m', 'y', 'n', 'a', 'm', 'e', 'n', 'a', 'y', 'a', 'k', 'a'}

    # Minus
    print(a_data - b_data)

    # Letter in a_data or b_data
    print(a_data | b_data)

    # Same letter in a_data and b_data
    print(a_data in b_data)

    # Letter in a_data or b_data but not both
    print(a_data ^ b_data)

    # Comperhansion also support on Set
    letter = {x for x in 'shabrina' if x not in a_data}
    print(letter)
