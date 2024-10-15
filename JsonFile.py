import json

# x={"name":"alex","age":120,"job":"Automation Tester"} #//Dictionary

# #//Converting dictionary into json
# y=json.dumps(x)

# print(y)

# #///converting json y into the python file

# z=json.loads(y)
# print(z,": ",z["name"])

# dict={1:True,2:False,3:True}
# print(json.dumps(dict))


import json

dog_data = {
    "name": "Frieda",
    "is_dog": True,
    "hobbies": ["eating", "sleeping", "barking",],
    "age": 8,
    "address": {
    "work": None,
    "home": ("Berlin", "Germany",),
    },
        "friends": [
        {
            "name": "Philipp",
            "hobbies": ["eating", "sleeping", "reading",],
        },
        {
            "name": "Mitch",
            "hobbies": ["running", "snacking",],
        },
    ],
}

with open("hello_frieda.json", mode="w", encoding="utf-8") as write_file:
    json.dump(dog_data, write_file)

with open("hello_frieda.json", mode="r", encoding="utf-8") as read_file:
    fileInPython=json.load(read_file)

print(type(fileInPython))
print(fileInPython)
print(fileInPython["name"])