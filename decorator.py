def foo(bar):
        return bar + 1

#print(foo)
#print(foo(2))
#print(type(foo))


def call_foo_with_arg(foo, arg):
    return foo(arg)

#print(call_foo_with_arg(foo, 3))

def parent(num):
    #print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    #print(first_child())
    #print(second_child())

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child

foo = parent(10)
bar = parent(11)

#print(foo)
#print(bar)

#print(foo())
#print(bar())
#parent()
#first_child()




def my_decorator(some_function):
    
    def wrapper():

        num = 10

        if num == 10:
            print('yes')
        else:
            print('no')
        print("Something is happening before some_function() is called.")
        
        some_function()
        
        print("Something is happening after some_function() is called.")
        
    return wrapper

@my_decorator
def just_some_function():
    print("Wheee!")


# if __name__ == "__main__":
#     my_decorator(just_some_function
#     )
# just_some_functions = my_decorator(just_some_function)
# print(just_some_functions)
just_some_function()
