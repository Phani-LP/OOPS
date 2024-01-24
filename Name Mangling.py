# Name Mangling can be used to access private data in objects, subclass & subclass objects.
# Rule: Min 2 underscores before and maximum one underscore after the name of data or method. 
# Ex: __data_, __data, ___data, ect.,
class A:
    __a = 10
    def method1(self):
        print(self.__a)
class B(A):
    def method2(self):
        b = self._A__a + 10
        print(b)
        print(self._A__a)
obj1 = B()
obj1.method2() #output: 20 10
obj1.method1() #output: 10
print(obj1._A__a) #output: 10

"""
class A:
    __a = 10
    def method1(self):
        print(self.__a)

obj = A()
obj.method() #output: 10
print(obj.__a) #output: AttributeError
"""
