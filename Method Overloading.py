# We can't directly use method overloading in python. To use it we have to install "multipledispatch" package.
#To use multipledispatch, you need to install the package first. You can do this using a package manager like pip:  pip install multipledispatch
# Features of method overloading: Flexibility, Readability, Program Complexity decrease.
import multipledispatch
class MethodOverLoading:
    @multipledispatch.dispatch(int,int)
    def add(self,a,b):
        return a+b
    @multipledispatch.dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c
    @multipledispatch.dispatch(str,str)
    def add(self,a,b):
        return a+b

obj = MethodOverLoading()
print(obj.add(9,3))
print(obj.add(12,8,3))
print(obj.add('Naga',' Phanindra'))
