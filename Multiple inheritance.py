class GrandParent:
  def method1(self):
    prinit("I am Grand Parent")

class Parent(GrandParent):
  def method2(self):
    print("I am Parent")

class Child:
  def method3(self):
    print("I am Child")
