import copy
#/////////////////// List ////////////////////////
state=['Maharashtra','Karnataka','Delhi','Andhra']
state.append('Gujarat')
print("States in India : ", list(state))
state.reverse()
print("States in India : ", list(state))
newState=state
print("States in India : ", list(newState))
print("States in India : ", list(state))
state.insert(1,'Tamilnadu')
print("States in India : ", list(state))
state.remove('Delhi')
print("States in India : ", list(state))
print("States in India : ", list(state))
newList=copy.deepcopy(state)
newList.append('Kerla')
print("States in India : ", list(newList))
print("States in India : ", list(state))



# /////////////// Dictinary //////////////////////
capitalOfStates={'Maharashtra':'Mumbai','Gujrat':'Gandhinagar','Bihar':'Patana','Goa':'Panji','Tamil Nadu':'Chennai'}
for i in capitalOfStates.keys():
    print("Capital of states is: ",i)
for i in capitalOfStates.values():
    print("Capital of states is: ",i)
for i in capitalOfStates.items():
    print("Capital of states is: ",i)
print(capitalOfStates.get('Bihar'))
print(capitalOfStates.get('Bihar',0))
print(capitalOfStates.get('Delhi',0))
capitalOfStates.setdefault('Delhi','new')
print(capitalOfStates)



