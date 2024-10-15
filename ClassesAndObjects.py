# class StudentInfo:
            
#         #//Constructor   
#         def __init__(self,name,marks):
#             self.name=name
#             self.marks=marks
    
#         #//Method
#         def newStudent(self,name,surName):
#             print("New student information: "+name+ " "+surName)
            
#         def studentAddress(self,studentAddress):
#             return studentAddress
            
    
# studentObj=StudentInfo("Smita","100")
# print(studentObj.name)
# print(studentObj.marks)

# studentObj.newStudent("Vinod","Kanawade")
# print("Student address is :"+studentObj.studentAddress("Sangamner"))


# class Student:
    
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def average(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
    
#         print("Hi "+self.name+" Your average score is :"+ str(int(sum/3)))
    
# obj=Student("Smita",[100,89,97])
# obj.average()

# # Create the account class with 2 attribute- balance and account number
# # Create method for debit credit and printing the balance

# class Account:
    
#     def __init__(self, balance,accNo):
#         self.balance=balance
#         self.accNo=accNo
        
#     def debit(self,amount):
#         self.balance=self.balance-amount
#         print(str(amount) +" is debited from account "+str(self.accNo))
        
#     def credit(self,amount):
#         self.balance=self.balance+amount
#         print(str(amount) +" is creadited to account "+str(self.accNo))

#     def getBalance(self):
#         return self.balance
    
# accObj=Account(30000,46764874683653)
# accObj.debit(4000)
# accObj.credit(5000)
# print("Total balance is :"+str(accObj.getBalance()))

#////How to use @property 

class Student:
    def __init__(self,Math,Phy,Chem):
        self.Math=Math
        self.Phy=Phy
        self.Chem=Chem
        
    @property
    def percentage(self):
        return str(int((self.Math+self.Chem+self.Phy)/3))+" %"
        
studentObj=Student(98,76,98)
print(studentObj.percentage)   #//// we can call like attribute to precentage 

studentObj.Math=100
print(studentObj.percentage)

