# class: Class is a blueprint used to store variables, methods, constructor functions, ect.,
# "class" keyward is used to create a class. ClassName follows Pascalcase Naming Convention
class BankAccount:
    def __init__(self, accNum, accUserName, balance):
        # We can use any name for self.Ex: Phani.accountNum = accNum
        # Self is used to store the current object. 
        # Without self we can't store and modify the attributes using object.
        self.accountNumber = accNum
        self.accountUserName = accUserName 
        self.balance = balance
    
    def checkBalance(self):#def keyward is used to create a method.
        print("Account Balance:",self.balance)
        
    def deposit(self,amount):
        self.balance += amount
        print("Account Balance:",self.balance)
    
    def withdraw(self,amount):
        self.balance -= amount
        print("Account Balance:",self.balance)

# creating an object named obj1
# An Object is an instance of a class means "AN OBJECT IS A PRODUCT OF CLASS". Objects have Attributes and Methods
obj1 = BankAccount(12345678910,'Naga Phanindra',10000)
obj1.deposit(10000)
obj1.withdraw(1000)