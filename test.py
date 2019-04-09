class Test(object):

    def __init__(self):
        self.height = 23
        self.width = 43
        self.calculate()
        
    def calculate(self):
        self.data = self.height * self.width
        print(self.data)

    def outer_function(self):
        global a
        a = 20
        def inner_function():
            global a
            a = 30
            print('a =',a, id(a))
        
        inner_function()
        print('a =',a, id(a))

t = Test()
a = 10
t.outer_function()
print('a =',a, id(a))
