import os
import shutil

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

#To delete the file
# os.unlink("C:\\Users\\kanaw\\Downloads\\Document.pdf")

#To delete the folder
# os.rmdir("C:\\Users\\kanaw\\Downloads\\New folder")

#send2trash.send2Trash() will send a file or folder to the recycle bin

print(os.walk("C:\\Users\\kanaw\\Downloads"))

for folderName,subFolderName,fileName in os.walk("C:\\Users\\kanaw\\Downloads\\qwe"):
        print("folder name is: "+str(folderName))
        print("sub folder name is: "+str(subFolderName))
        print("file name is: "+str(fileName))

