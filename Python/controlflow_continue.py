def continue_basic():
    # How to segment vocal letter and un-vocal letter
    seta = []
    setb = []

    for x in range(20):
        if x // 3 == 1:
            seta.append(x)
            continue

        setb.append(x)

    print(seta)
    print(setb)