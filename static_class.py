class A(object):
    def foo(self, x):
        print "executing foo(%s, %s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s, %s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x

class B(A):
    def __init__(self, v):
        super().__init__(self, v)
        print("IN B")
a = A()
b = B(2)
#b.foo(2)
a.foo(1)
a.static_foo(23)
