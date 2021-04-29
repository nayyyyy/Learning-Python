def fizz_buzz(num):
    text = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            text.append('FizzBuzz')
        elif i % 3 == 0:
            text.append('Fizz')
        elif i % 5 == 0:
            text.append('Buzz')
        else:
            text.append(str(i))

    print(text)