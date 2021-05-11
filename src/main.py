def classes_basic():
    class Basic:
        def __init__(self):
            self.name = None

        def say_hello(self):
            return 'Hello' + self.name

        def say_ohaiyo(self):
            return 'Ohaiyo' + self.name

    data1 = Basic

    data1.name = 'Haloha'
    print(data1.say_ohaiyo())
