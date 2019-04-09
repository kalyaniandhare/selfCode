class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):
    def show(self):
        return 'show pdf'


class Word(Document):
    def show(self):
        return 'word doc'


class my_test(Document):
    def test(self):
        print("WIN")
        

df = [Pdf('document'), Pdf('document2'), Word('test')]
for i in df:
    print(i.name, i.show())
d = Pdf('document1_pdf')
c = my_test('kalyani')
print(c.name)
c.test()
print(d.show())
        
