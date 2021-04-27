# This is how to made a global Variabel. The variabel not in a function anymore
text = 'Global variabel'


def function_global():
    # Initial variabel in global function

    def function_local():
        text = 'Data has been change in local variabel'

        return text

    def function_nonlocal():
        nonlocal text
        text = 'Data has been change non Local Variabel'

        return text

    def function_doglobal():
        global text
        text = 'Global Variabel'

        return text

    # Print first declare variabel
    print(text)

    # Print local variabel in function
    print(function_local())

    # Print nonLocal variabel
    print(function_nonlocal())

    # Print Global vairabel function
    print(function_doglobal())
