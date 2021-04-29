def break_basic():
    # lets see how to use break

    found = 50
    count = 0

    for num in range(100):
        if num == found:
            break
        else:
            count += 1

    print(count)