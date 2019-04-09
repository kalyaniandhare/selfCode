import time

def timing_function(some_function):
    print("1", some_function)
    def wraper():

        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wraper

@timing_function
def my_function():
    print("2")
    numList = []
    for num in range(0, 10):
        numList.append(num)
        print("\nSum of all the numbers: " + str((sum(numList))))

print(my_function())
    
