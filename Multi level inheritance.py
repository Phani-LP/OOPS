#Multi level inheritance
class GrandParent:
  def method1(self):
    print("I am Grand Parent")

class Parent(GrandParent):
  def method2(self):
    print("I am Parent")

class Child(Parent):
  def method3(self):
    print("I am Child")

obj = Child()
obj.method3()
obj.method2()
obj.method1()

obj2 = Parent()
obj2.method2()
obj2.method1()
