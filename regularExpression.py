import re

phoneNumber=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumber.search('232-342-3423')
print(mo.group())

MobileRegEx=re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')
mo=MobileRegEx.search('(457)-899-9870')
print(mo.group())

batRegEx=re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegEx.search('Batman is on the TV')
print(mo.group())

mo=batRegEx.search('Batmobile lost the wheel')
print(mo.group())

# Optional part should be keep before ? mark
phoneNumberReEx=re.compile(r'(\d\d\d)? \d\d\d-\d\d\d\d')
mo=phoneNumberReEx.search("My phone number is 345-3455")
print(mo.group())

repetativeRegEx=re.compile(r'(Ha){3}')
mo=repetativeRegEx.search("Morning should start with HaHaHa")
print(mo.group())

repetativeRegEx=re.compile(r'(Ha){3,5}')
mo=repetativeRegEx.search("Morning should start with HaHaHaHa")
print(mo.group())


#/////////////findAll()///////////////////
phoneNumRegEx=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegEx.findall("222-333-4453, 333-444-5433, 342-34-9878")
print(mo)

#/// Return searched list of string
#['222-333-4453', '333-444-5433']

phoneNumRegEx=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegEx.findall("222-333-4453, 333-444-5433, 342-34-9878")
print(mo)
# If the regular expression have paranthesis or group then it will return list of tupils
#[('222', '333-4453'), ('333', '444-5433')]

#//////////////(?) wo ia optional can appear 0 or one time
batRegEx=re.compile(r'Bat(wo)?man')
mo=batRegEx.search('The Advanturs of Batwoman')
print(mo.group())

mo=batRegEx.search('The Advanturs of Batman')
print(mo.group())

#/////////////(*) wo is optonal can appear 0 or more time
batRegEx=re.compile(r'Bat(wo)*man')
mo=batRegEx.search('The Advanturs of Batwowowowoman')
print(mo.group())

mo=batRegEx.search('The Advanturs of Batman')
print(mo.group())

#/////////////(+) wo is not optonal can appear 1 or more time
batRegEx=re.compile(r'Bat(wo)+man')
mo=batRegEx.search('The Advanturs of Batwowowowoman')
print(mo.group())

# mo=batRegEx.search('The Advanturs of Batman')
# print(mo.group())

regEx=re.compile(r'(\+\*\?)+')
mo=regEx.search('I learned +*?+*?+*?+*?+*?  Regular expression')
print(mo.group())

xmasSong='12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
xmassRegex=re.compile(r'\d+\s\w+')
print(xmassRegex.findall(xmasSong))

vovelsRegEx=re.compile(r'[aeiou]') # same as (a|e|i|o|u)
print(vovelsRegEx.findall(xmasSong))
#['u', 'e', 'i', 'e', 'o', 'a', 'i', 'e', 'a', 'i', 'a', 'e', 'e', 'e', 'i', 'i', 'e', 'o', 'e', 'a', 'i', 'e']

vovelsRegEx=re.compile(r'[a-f]') 
print(vovelsRegEx.findall(xmasSong))
#['d', 'e', 'e', 'd', 'a', 'd', 'e', 'a', 'd', 'a', 'e', 'e', 'e', 'b', 'd', 'e', 'd', 'e', 'a', 'd', 'e']

vovelsRegEx=re.compile(r'[airs]{2}') 
print(vovelsRegEx.findall(xmasSong))
#['rs', 'rs', 'ai', 'ri', 'ir', 'ar', 'ri']


vovelsRegEx=re.compile(r'[^aeiou\s\d\,\s]') # same as other than (aeiou\s\d\,\s)
print(vovelsRegEx.findall(xmasSong))
#['u', 'e', 'i', 'e', 'o', 'a', 'i', 'e', 'a', 'i', 'a', 'e', 'e', 'e', 'i', 'i', 'e', 'o', 'e', 'a', 'i', 'e']

#//// Dot-Star and the caret(^)/Doller($) character
beginsWithHelloRegullarEx=re.compile(r'^Hello')
print(beginsWithHelloRegullarEx.search("Hello there!"))
#<re.Match object; span=(0, 5), match='Hello'>

endsWithHelloRegullarEx=re.compile(r'^world$')
print(endsWithHelloRegullarEx.search("Hello there! world"))

startAndEndsWithRegullarEx=re.compile(r'^\d+$')
print(startAndEndsWithRegullarEx.search("273825981"))

startAndEndsWithRegullarEx=re.compile(r'^\w+$')
print(startAndEndsWithRegullarEx.search("jvbjhwbswk"))

atRegExp=re.compile(r'.{1,2}at')
print(atRegExp.findall('fat mat rat flat hat what'))

name='First Name: Smita Last Name:Auti'
nameRegExp=re.compile(r'First Name:(.*) Last Name:(.*)')
print(nameRegExp.findall(name))

#////Greedy and non greedy character
serve='<To serve humans> for dinner.>'
nonGreedyRegex=re.compile(r'<(.*?)>')
print(nonGreedyRegex.findall(serve))
#////////['To serve humans']

greedyRegex=re.compile(r'<(.*)>')
print(greedyRegex.findall(serve))
#['To serve humans> for dinner.']


#///////////////Dotstar with new line 
primeReg='Serve the public trust. \n protect the innocent.\n upload the law'
dotstarRegExp=re.compile(r'.*')
print(dotstarRegExp.findall(primeReg))
# ['Serve the public trust. ', '', ' protect the innocent.', '', ' upload the law', '']
#  .* is not returning the new line character

dotstarRegExp=re.compile(r'.*', re.DOTALL)
print(dotstarRegExp.findall(primeReg))
#  ['Serve the public trust. \n protect the innocent.\n upload the law', '']

xmasSong='12 drUmmers, 11 pipers, 10 lords, 9 ladIes, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hEns, 2 doves, 1 partridge'
vovelsRegEx=re.compile(r'[aeiou]',re.IGNORECASE) 
print(vovelsRegEx.findall(xmasSong))
#['U', 'e', 'i', 'e', 'o', 'a', 'I', 'e', 'a', 'i', 'a', 'e', 'e', 'e', 'i', 'i', 'E', 'o', 'e', 'a', 'i', 'e']

#////RegEx sub() and RegEx Verbose()

nameRegex=re.compile(r'Agent (\w)\w*')
mo=nameRegex.findall('Agent Alice gave the secret document to Agent Bob')
print(mo)

print(nameRegex.sub('Agent \1****', 'Agent Alice gave the secret document to Agent Bob'))

nameRegex=re.compile(r'Agent \w+')
mo=nameRegex.findall('Agent Alice gave the secret document to Agent Bob')
print(mo)