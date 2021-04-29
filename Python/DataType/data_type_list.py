def list_Sample():
    # Sample List
    data = [1, 2, 3, 4]
    print(data)
    print(isinstance(data, list))

    # List can be slicing like string
    print(data[0])
    print(data[-2])
    print(data[:-3])

    # Print all list
    print(data[:])

    # Addition another list
    x = [5, 6, 7]
    print(data + x)

    # Replace List
    data[0] = 10
    print(data)

    # Include new data at the end of list
    data.append(100)
    data.append(8 ** 3)
    print(data)

    # Slicing a List
    print(data[1:3])
    print(data[3:-2])

    # Slicing and Replace
    data[0:2] = [10, 20, 30]
    print(data)

    # Slicing and Remove
    data[0:2] = []
    print(data)

    # Empty List
    data[:] = []
    print(data)

    # count length of list
    data = ['N', 'A', 'Y', 'A', 'K', 'A']
    print(len(data))

    # Make a list contain another list
    x = [1, 1, 1, 2]
    mix = [data, x]
    print(mix[1])
    print(mix[1][1])
    print(mix)


def list_Method():
    # Declared a new list
    car = ['BMW', 'Mercedes', 'Volvo', 'Volkswagen', 'Honda', 'Mitsubishi']
    print(car)

    # .append() has a function to add new data at end of list
    car.append('Porsche')
    print(car)

    # .remove(a) has a function to remove data 'a'
    car.append('BMW')
    print(car)

    # .insert(a, b) has a function add new data 'b' at index 'a'
    car.insert(0, 'BMW')
    print(car)

    # .count(a) has a function to count data 'a'
    print(car.count('BMW'))
    print(car.count('Porsce'))

    # .copy() has a function to copy list to the other variabel
    new_car = car.copy()
    print(new_car)

    # .reverse() has a function to reverese element in list
    car.reverse()
    print(car)

    # .sort() has a function to short data
    print(car.sort())

    # .pop() has a function to delete last data in list
    car.pop()
    print(car)

    # .clear() has a function to empty list
    car.clear()
    print(car)


def list_DelState():
    data = [1, 2.34, -3.14, 112, 12e3, 4]

    # Del has function to delete a data in List
    del data[0]
    print(data)

    del data[:2]
    print(data)

    del data[:]
    print(data)


def list_Comprehension():
    data = []

    # Addition data on List
    for number in range(10):
        data.append(number ** 2 / 3)

    print(data)

    # Another way to in arithmetic data
    data = list(map(lambda x: x ** 2 / 3, range(10)))
    print(data)

    # Equivalent with on the top one
    data = [x ** 2 / 3 for x in range(10)]
    print(data)
    del data

    # This is how to count combination
    combination = [(x, y) for x in [5, 2, 3] for y in [3, 1, 4] if x != y]
    print(combination)
    print(len(combination))

    # it's equivalent to:
    combination.clear()
    combination = []
    for a in [5, 2, 3]:
        for b in [3, 1, 4]:
            if a != b:
                combination.append((a, b))

    print(combination)

    # Some example operation in list
    del combination
    data = [5, -4, 3, -2, 1]
    new_data = [x * -1 for x in data]
    print(new_data)

    # Filter data in list
    print([x for x in data if x <= 0])

    # Apply function in list
    print(abs(x) for x in data[1:3])

    # Call method in all list
    data.clear()
    new_data.clear()
    data = [' Ice Cream', ' B A K S O', 'Aku Suka Susunya']
    new_data = [x.strip for x in data]
    print(new_data)

    # make a list of 2 tuples like (number, number * 2)
    data.clear()
    data = [(x, x * 2) for x in range(8)]
    print(data)

    # Flatting the list of 2 tuples
    new_data.clear()
    new_data = [x for y in data for x in y]
    print(new_data)


def list_nested_comprehensif():
    # Declare a variabel contains matrix 4 x 4
    matrix = [
        (1, 1, 1, 2),
        (2, 0, 0, 1),
        (0, 5, 1, 1),
        (2, 0, 0, 0),
        (1, 2, 3, 4)
    ]

    # This is how to transpose matrix in Python
    transpose = [[row[i] for row in matrix] for i in range(len(matrix) - 1)]
    print(transpose)

    # This is a manual method to transpose a matrix in Python
    transpose.clear()
    for i in range(len(matrix) - 1):
        transpose.append([row[i] for row in matrix])

    print(transpose)

    # Which means, it's same with this
    transpose.clear()
    for i in range (len(matrix)-1):
        transpose_row = []
        for row in matrix:
            transpose_row.append(row[i])
    transpose.append(transpose_row)

    print(transpose)

    # And this is a simple way to transform matrix
    print(list(zip(*matrix)))