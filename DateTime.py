import datetime

x=datetime.datetime.now()
print(x)
print(x.date)
print(x.month)
print(x.year)
print(x.day)

print(x.strftime("%B"))  #//October
print(x.strftime("%A"))  #//Friday
print(x.strftime("%a"))  #//Fri
print(x.strftime("%p"))  #//PM
print(x.strftime("%w"))  #//5 -time


