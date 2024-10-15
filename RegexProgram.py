import re

# 333-443-3322, 555-0786, (635) -748-2735, 555-0000 ext 12345, ext. 12345, x12345

#Create regular expression for phone number
phoneRegExpression=re.compile(r'''
(((\d\d\d)|(\(\d\d\d\)))?
(\s|-)
\d\d\d
-
\d\d\d\d)
''',re.VERBOSE) 

#Create regular expression for email address
emailRegExpression=re.compile(r'''
[a-zA-Z0-9.]+    #name part
@                  # @symbol
[a-zA-Z0-9.]+ 
''',re.VERBOSE)

extractedPhone=phoneRegExpression.findall("Jessie Mckay jmckay67@aol.com (479)-205-4877 Tom Jordan tjordan@msn.com 678-560-3485 Clayton Cross ccross20@gmail.com 770-900-2986 ")
print(extractedPhone)

allPhoneNumber=[]
for phone in extractedPhone:
    allPhoneNumber.append(phone[0])

print(allPhoneNumber)

extractedEmail=emailRegExpression.findall("Jessie Mckay jmckay67@aol.com 479-205-4874 Tom Jordan tjordan@msn.com 678-560-3485 Clayton Cross ccross20@gmail.com 724-900-2986 ")
print(extractedEmail)