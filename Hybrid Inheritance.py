class A:
    def m1(self):
        print("Method 1")

class B(A):
    def m2(self):
        print("Method 2")
        
class C(A):
    def m3(self):
        print("Method 3")
        
class D(B, C):
    def m4(self):
        print("Method 4")
# single inheritance
obj1 = B()
obj1.m1()
obj1.m2()

# {multi level, Multiple} Inheritance
obj2 = D()
obj2.m1()
obj2.m2()
obj2.m3()
obj2.m4()
