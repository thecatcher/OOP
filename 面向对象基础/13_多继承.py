class A:
    def demo(self):
        print("demo form A")

class B:
    def test(self):
        print("test from B")



class C(A,B):
    pass

    def printMRO(self):
        print(C.__mro__)



c = C()
c.demo()
c.test()

c.printMRO()