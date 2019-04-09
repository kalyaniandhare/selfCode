class myshape():

    def __init__(self, lent, wid):
        myshape.l = lent
        myshape.wid = wid
        self.l = lent
        self.w = wid

    def calculate_area(self):
        return self.l * self.w

    def printarea(self):
        print("Printing", str(self.calculate_area()))



class square(myshape):

    def __init__(self, side):
        myshape.__init__(self, side, side)

    def calculate_area(self):
        return myshape.calculate_area(self)

    def printing(self):
        print("printing", str(self.calculate_area()))



m = myshape(2,3)
print(m.l, m.wid)
s = square(10)
s.printing()
m.calculate_area()
m.printarea()



