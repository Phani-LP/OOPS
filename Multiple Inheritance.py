# Multiple Inheritance Example
class Parent1:
   def method1(self):
       print("I'm Parent one.")

class Parent2:
   def method2(self):
       print("I'm Parent two.")

class Child(Parent1, Parent2):
    def method3(self):
        print("I'm a Child.")

# Creating a object to Child class and Accessing it's parent's methods.   
obj = Child()
obj.method1()
obj.method2()
obj.method3()
