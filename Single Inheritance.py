# Single Inheritance Example
class Parent:
   def method1(self):
       print("I'm Parent")

class Child(Parent):
    def method2(self):
        print("I'm a Child")
     
# Creating a object to Child class and Accessing it's parent's method.   
obj = Child()
obj.method1()
obj.method2()