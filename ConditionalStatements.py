marks=85

if(marks>=90):
    print("Grade='A'")
elif(marks>=80 & marks<90):
    print("Grade='B'")
elif(marks<80 & marks>=70):
    print("Grade='C'")
elif(marks>70):
    print("Grade='D'")

#///////find odd or even number

Number=int(input("Enter your number: "))
if(Number%2==0):
    print("Number is even")
else:
    print("Number is odd")
    
#//////Find the greatest among 3 numbers

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if(num1>num2):
    print(str(num1) +": is the gretest number")
elif(num2>num3):
    print(str(num2)+ ": is the greast number")
else:
    print(str(num3)+": is the greast number")
    
#/////Check if number is multiple of 7 or not

num=int(input("Enter number"))

if(num%7==0):
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")