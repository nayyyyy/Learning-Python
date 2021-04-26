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

    del data[0]
    print(data)

    del data[:2]
    print(data)

    del data[:]
    print(data)
