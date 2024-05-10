class Student:
    def getStudentDetails(self):
        self.rollno=int(input("Enter roll number: "))
        self.name=input("Enter your name:")
        self.ds=int(input("Enter DS marks:"))
        self.os=int(input("Enter 05 marks:"))
        self.se=int(input("Enter SE marks:"))
    def printResult(self):
        self.percentage=(int)((self.ds+self.os+self.se)/300*100)
        print(self.rollno,self.name, self.percentage, "%")

S1=Student()
S1.getStudentDetails()

print("Result:")
S1.printResult()

S1.ds+=9
print("Result after adding grac marks:")
S1.printResult()