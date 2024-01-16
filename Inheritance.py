# {single, multi level, multiple, hierarchical, hybrid} inheritance
# one class is derived from another class - Single inheritance
# Derived class is created from more than one parent class - Multi level inheritance
# when a class is derived from another derived class - Multiple inheritance
# when a parent is derived in more than one child - Hierarchical inheritance
# Using morethan one inheritance - Hybrid inheritance
# The method resolution order (MRO) is a mechanism employed in oop to determine the sequence in which methods should be executed -
# when multiple classes share the same method names, ensuring a systematic resolution of method conflicts.
class Member:
    def __init__(self, fname, lname, email, memberId, address, mobileNumber, dateJoined):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.memberId = memberId
        self.address = address
        self.mobileNumber = mobileNumber
        self.dateJoined = dateJoined
    
    def getFullName(self):
        self.fullName = self.fname + self.lname
        
    def chnageAddress(self, newAddress):
        self.address = newAddress
        print("Address changed successfully")
        
    def chnageNumber(self, newNumber):
        self.mobileNumber = newNumber
        print("Number changed successfully")
    
class Faculty(Member):
    def __init__(self, fname, lname, email, memberId, address, mobileNumber, dateJoined, SubjectsTeaching, salary):
        self.SubjectsTeaching = SubjectsTeaching
        self.salary = salary
        Member.__init__(self, fname, lname, email, memberId, address, mobileNumber, dateJoined)
        
class Student(Member):
    def __init__(self, fname, lname, email, memberId, address, mobileNumber, dateJoined, SubjectsLearned, GPA):
        self.SubjectsLearned = SubjectsLearned
        self.GPA = GPA
        Member.__init__(self, fname, lname, email, memberId, address, mobileNumber, dateJoined)
