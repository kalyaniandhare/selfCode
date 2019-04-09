def test_first(func):
    def inner():
        print("first function")
        func()
    return inner

@test_first
def func_1():
    print("secound func")
    
