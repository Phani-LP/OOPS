# Hierarchical Inheritance
class Parent:
    def method1(self):
        print("I am Parent")

class Child1(Parent):
    def method2(self):
        print("I am First Child")
        
class Child2(Parent):
    def method3(self):
        print("I am Second Child")

obj1 = Child1()
obj1.method1()
obj1.method2()

obj2 = Child2()
obj2.method1()
obj2.method3()