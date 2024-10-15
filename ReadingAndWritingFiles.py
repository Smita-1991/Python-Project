import os

filePath=os.path.join('Users','kanaw','OneDrive','Desktop','Smita','Python','Python-Project')
print(filePath)

myFiles=["DateTime.py","FirstProgram.py","Function.py"]

for fileName in myFiles:
    print(os.path.join(filePath,fileName))
    
#Print curent working directory
print(os.getcwd())

# for change directory os.chdir() is getting used

#create a new directory
# os.makedirs(filePath+"/newfolder")

print(os.path.isabs("C:\\Users\\kanaw"))
print(os.path.isdir("C:\\Users\\kanaw"))
print(os.path.relpath("C:\\Users\\kanaw"))

print(os.path.basename(filePath))

print(os.path.dirname(filePath))

print(filePath.split(os.path.sep))


