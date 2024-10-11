#//// Read mode
f=open(r"C:/Users/kanaw/OneDrive/Desktop/Smita/Demo.txt","r")
data=f.read()
print(data)
f.close()

#////Write mode
f=open(r"C:/Users/kanaw/OneDrive/Desktop/Smita/Sample.txt","w")
f.write("I want to learn javascript tomorrow \n")
f.close()


#/////Append mode add at the end
f=open(r"C:/Users/kanaw/OneDrive/Desktop/Smita/Demo.txt","a")
f.write("I want to learn Python tomorrow")
f=open(r"C:/Users/kanaw/OneDrive/Desktop/Smita/Demo.txt","r")
dada=f.read()
print(data)
f.close()

#////Delete file

import os

os.remove("C:/Users/kanaw/OneDrive/Desktop/Smita/Sample.txt")


#/////Create new file practice.text using python add the following data in it
# Hi everyone
# We are learing file I/O
# using python
# I like programming in python

f= open("C:/Users/kanaw/OneDrive/Desktop/Smita/Sample.txt","w")
f.write("Hi everyone \nWe are learning file I/O\nusing python \nI like programming in python")

with open("C:/Users/kanaw/OneDrive/Desktop/Smita/Sample.txt","w") as f:
    f.write("Hi everyone \nWe are learning file I/O\nusing Python \nI like programming in Python")

#///Replace all occurances of python with java in above file

with open("C:/Users/kanaw/OneDrive/Desktop/Smita/Sample.txt","r") as f:
    data=f.read()
    
new_data=data.replace("Python","Java")
print(new_data)

with open("C:/Users/kanaw/OneDrive/Desktop/Smita/Sample.txt","w") as f:
    f.write(new_data)    

#///Search word learning is exist in the file or not

def checkForWord():
    with open("C:/Users/kanaw/OneDrive/Desktop/Smita/Sample.txt","r") as f:
        data=f.read()
    
        if(data.find("learning") != -1):
            print("found")
        else:
            print("not found")

checkForWord()

#////Find in which line of the file does the word learning occur first print 1 if word not  found

def checkForLine():
        word="learning"
        data =True
        lineNum=1
        with open("C:/Users/kanaw/OneDrive/Desktop/Smita/Sample.txt","r") as f:
            while data:
                data=f.readline()   
                if(word in data):
                    print(lineNum)
                    return
                lineNum+=1
                
        return-1

checkForLine()

#////From a file containing numbers separeted by comma, print the count of even numbers

def printEvenNumber():
    with open("C:/Users/kanaw/OneDrive/Desktop/Smita/SampleNew.txt","w") as f:
        f.write("1,2,3,4,5,6,7,12,56,34,78,86,33,45")
    with open("C:/Users/kanaw/OneDrive/Desktop/Smita/SampleNew.txt","r") as f:
        data=f.read()
        print(data)

        newData=data.split(',')
        print(newData)
        i=0
        count=0
        for val in newData:
            if(int(val)%2==0):
                count+=1                
    
        print("Total number of even numbers are "+str(count))

        # while(i<len(newData)):
        #     if(int(newData[i]) % 2==0):
        #         print("Number is even: "+newData[i])
        #     else:
        #         print("Number is odd: "+newData[i])
        #     i+=1

printEvenNumber()