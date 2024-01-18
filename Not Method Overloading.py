# The following code can do the same as mentioned in method overloading.py file, but it is not method overloading.
class NotMethodOverLoading:
  def add(self,*args):
    if args:
      output = type(args[0])()
      for i in args:
        output += i
      return output
obj = NotMethodOverLoading()
print(obj.add(29,34))
print(obj.add(3,8,34))
print(obj.add('Naga','Phanindra'))
print(obj.add(12.7,3.3,16))
