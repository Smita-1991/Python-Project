import encodings
import json

# with open("data.json","r") as f:
#         data=f.read()
# print(data)

# data=json.load(open("data.json"))
# print(data)

word=input("Enter the word you want to search")
print(word)
print(word.title())


jsonData=json.load(open("data.json"))

def translate(word):
    if word in jsonData:
        return jsonData[word]
    elif word.title() in jsonData:
        return jsonData[word]
    elif word.upper() in jsonData:
        return jsonData[word]    
    else:
        print("You have enter wrong word")
        
output=translate(word)
print(output)