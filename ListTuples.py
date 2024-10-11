# Enter three favourite movies and sort them
movieList=[]

movieList.append(input("Enter movie name: "))
movieList.append(input("Enter movie name: "))
movieList.append(input("Enter movie name: "))

movieList.sort()

print(movieList)

#//////Check the list contains the pallindrome or not

mainList=['m','a','d','a','m']

newList=mainList.copy()

newList.reverse()
if(mainList==newList):
    print("The list is pallindrome ")
else:
    print("The list is not pallindromew")


#////////Count the number of student with the grade 'A' in the following tupple 

studentTup=('C','D','A','A','B','B','A')

print(studentTup.count('A'))


#/////Store the above values in the list and sort them in the order from A to D
studentList=['C','D','A','A','B','B','A']
studentList.sort()
print("List in sorted order: "+ str(studentList))

#/////Store following word meanings in a python dictionary

dictionary={
    'table':['a piece of furniture','list of facts & figurs'],
    'cat':'a small animal'
}

print(dictionary)


#You are given a list of subjects for students.Assumeone classroom is required for 1 subject. How many classrooms are needed by all students
subjectSet={"python","Java","C++","python","JavaScript","Java","Python","Java","C++","C"}

print("Total number of classroom: "+str(len(subjectSet)))


#///Enter marks of 3 subjects from user and store them in a dictionary 
dictionary={}

dictionary["Physics"]=int(input("Enter marks of Physics: "))
dictionary["Chemistry"]=int(input("Enter marks of Chemistry: "))
dictionary["Math"]=int(input("Enter marks of Math: "))

print(dictionary)

#////Figure out a way to store 9 and 9.0 as a separate values in the set
diffValueSet={9,'9.0'}
print(diffValueSet)