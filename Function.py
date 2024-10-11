# #print element of list 
# def functionList(randomList):
#     print(len(randomList))
    
# functionList([2,3,4,5,3])

# #print element of list in single line
# def functionList(randomList):
#     i=0
#     while(i<len(randomList)):
#         print(str(randomList[i]),end=" ")
#         i+=1
    
# functionList([2,3,4,5,3])

# #///Find the factorial of n

# def factoria(num):
#     i=1
#     fact=1
#     while(i<=num):
#         fact=fact*i
#         i+=1
#     return fact

# fact=factoria(5)
# print(fact)


# //////Factorial
# Calculate the sum of first n natural number

def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) + n 
    
sum=cal_sum(7)
print(sum)

#/////Print all element in a list

def print_List(list,index):
        if(index==len(list)):
            return
        else:
            print(list[index])
        print_List(list, index+1)

print_List([2,3,4,5,6],0)