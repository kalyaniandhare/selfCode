class Enscap:
    def __init__(self):
        print("in self")
        self.__secound_test()

    def initial_test(self):
        print(1)

    def __secound_test(self):
        print(2)


a = Enscap()
a.initial_test()
a._Enscap__secound_test()


def my_deco(func):
    
    def inner(a):
        if a==10:
            return "inner"
        return "outer"
    return func()
            


@my_deco
def working():
    print("HELLO")
