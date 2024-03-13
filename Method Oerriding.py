
"""Same method in super class and subclass with same parameters and 
we access the method in the subclass without accessing the super class
method this is nothing but method overriding.
"""
"""Rules for method overriding: 
1). Inheritance should be there.
2). Same method and same parameters must be there in the super and sub class.
3). Logic must be different in methods of super and subclass.
"""

class Parent:
    def sample(self):
        print("I am a parent")

class Child(Parent):
    def sample(self):
        print("I am a child")

obj1 = Child()
obj1.sample()

# output: I am a child ## The child method named: sample executed rather than parent's sample method. 

"""
How can you access the parent's sample method from child class?
"""  
class Parent:
    def sample(self):
        print("I am a parent")

class Child(Parent):
    def sample(self):
        Parent.sample(self) #include arguments if exists
        #2nd way: super().sample(self, arguments)
        print("I am a child")

obj1 = Child()
obj1.sample()
