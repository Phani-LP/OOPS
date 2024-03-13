# {single, multi level, multiple, hierarchical, hybrid} inheritance
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