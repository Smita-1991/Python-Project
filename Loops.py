#////Print number from 1 to 100
i=1
while(i<=100):
    print(i)
    i+=1

print("/////////////////////////////")
#////Print number from 100 to 1

i=100
while(i>=1):
    print(i)
    i-=1

#//////Print the multiplication table of number n

nthTable=int(input("Enter the table number: "))

i=1
while(i<=10):
    mul=i*nthTable
    i+=1
    print(mul)

#////Print the element of the following list using loop
#[1,4,9,16,25,36,49,64,81,100]

randomList=[1,4,9,16,25,36,49,64,81,100]

totalNumberOfElement=len(randomList)
i=0

while(i<totalNumberOfElement):
    print(str(randomList[i]))
    i+=1
    
#////Search for a number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]

randomTup=(1,4,9,16,25,36,49,64,81,100)
num=int(input("Enter the you want to search: "))

i=0
while(i< len(randomTup)):
    if(num==randomTup[i]):
        print("searched number is: "+str(num))
        break
    else:
        i+=1
        if(i==len(randomTup)):
            print("number is not found in the tupple")
        

#////Print the element of the following list using for loop
#[1,4,9,16,25,36,49,64,81,100]

randomList=[1,4,9,16,25,36,49,64,81,100]

for val in randomTup:
    print(val)
    
    
#////Search for a number x in this tuple using for loop
#[1,4,9,16,25,36,49,64,81,100]

randomTup=(1,4,9,16,25,36,49,64,81,100,4)
num=int(input("Enter the you want to search: "))

index=0
for val in randomTup:
    if(val==num):
        print("Number is found in tuple at index "+str(index))
    index+=1


#////Print the number from 1 to 100

for num in range(1,101):
    print(num)

#////Print number from 100 to 1

for num in range(100, 0, -1):
    print(num)


#////Print the multiplication table of number n

n=int(input("Enter number: "))
lastNumber=n*10
for num in range(n,lastNumber+n ,n):
    print(num)

n=int(input("Enter number: "))
i=1
for num in range(i, i*10+1):
    print(n*i)
    i+=1

#////Find sum of first n number using while

n= int(input("Enter the number: "))

i=1
sum=0
while(i<=n):
    sum=sum+i
    i+=1
print(sum)


#////Find factorial of first n number using for

n=int(input("Enter the number"))
i=1
fact=1
for num in range(i,n+1):
    fact=fact*i
    i+=1
print(fact)

