class P:
    def __init__(self):
        print "This is parent class"
    def parent(self):
        print "parent method"
class C(P):
    def __init__(self):
        print "This is a child class"
obj1=C()


