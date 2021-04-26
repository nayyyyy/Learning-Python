from builtins import isinstance


def aritmatika():
    print('Operasi perhitungan Aritmatika')

    # Declare Variabel
    a = 5
    b = 3

    # Penjumlahan
    print(a + b)

    # Pengurangan
    print(a - b)

    # Perkalian
    print(a * b)
    print(isinstance(a * b, int))

    # Pembagian
    # Pembagian selalu menghasilkan tipe data Float
    print(a / b)
    print(isinstance(a / b, float))

    # Modulus
    print(a % b)

    # Eksponen
    print(a ** 3)
    print(b ** 2)

    # Floor
    print(a // 3)
    print(8 // 3)
    print(9 // 3)
    print(isinstance(a // 3, int))


def bitwise():
    print("Operasi Perhitungan Bitwise")

    # AND
    # 6 = 0b0110
    # 2 = 0b0010
    # Hasil = 2 -> 0b0010
    print(6 & 2)

    # OR
    # 6 = 0b0110
    # 2 = 0b0010
    # Hasil = 6 -> 0b0110
    print(6 | 2)

    # NOT
    # 6 = 0b0101
    # Hasil = -7 -> 0b1001 ( -(6) - 1 )
    print(~6)

    # XOR
    # 6 = 0b0110
    # 2 = 0b0010
    # Hasil = 9 -> 0b0101
    print(6 ^ 2)

    # Signed Right Shift
    # 6 = 0b0110
    print(6 >> 1)  # Hasil 3 = 0b0011
    print(6 >> 2)  # Hasil 1 = 0b0001

    # Signed Left Shift
    # 6 = 0b0110
    print(6 << 1)  # Hasil 12 = 0b1100
    print(6 << 2)  # Hasil 24 = 0b11000


def assignment():
    # Declare Variabel
    a = 6

    # Penjumlahan
    a += 3
    print(a)  # 9

    # Pengurangan
    a -= 2
    print(a)  # 7

    # Perkalian
    a *= 2
    print(a)  # 14

    # Pembagian
    a /= 2
    print(a)  # 7

    # Modulus
    a %= 4
    print(a)  # 3

    # Floor
    a //= 2
    print(a)  # 1

    # Eksponen
    a **= 2
    print(a)  # 1

    a = 1

    # And
    a &= 2
    print(a)  # 0

    # Or
    a |= 8
    print(a)  # 8

    # Shift Right
    a >>= 1
    print(a)  # 4

    # Shift Left
    a <<= 1
    print(a)  # 8

    # XOR
    a ^= 5
    print(a)  # 13


def comparison():
    # Declared Variabel
    number = 5
    x = 8

    # Equal
    print(number == x)

    # Not Equal
    print(number != x)

    # Greater Then
    print(number > x)

    # Less Then
    print(number < x)

    # Greater then or equal
    print(number >= 5)
    print(number >= x)

    # Less then or equal
    print(number <= 5)
    print(number <= x)


def logical():
    x = 5
    y = 8

    # Logical And
    print(x > 8 and y == 8)

    # Logical Or
    print(x < 4 or y >= 8)

    # Not
    print(x != y)
    print(not x == y)


def identity():
    Data1 = ["Apple", "Grape", "Melon"]
    Data2 = ["Grape", "Melon", "Banana"]

    # Is (Identity Same)
    print(Data1 is Data2)

    # Is Not (Identity not Same)
    print(Data1 is not Data2)


def membership():
    Data_List = ["Apple", "Grape", "Melon"]
    Data = "Grape"

    # In (Once of data in List)
    print(Data in Data_List)

    # Not in (Data not in List)
    print(Data not in Data_List)
