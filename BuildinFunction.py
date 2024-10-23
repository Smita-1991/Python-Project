import random
print('Hello, What is your name')
name=input()
secretNumber=random.randint(1,20)
print("Well "+name+" I am thinking of a number between 1 and 20")
guessTaken=""
guess=""
for guessTaken in range(1,6):
    print("take a gues")
    guess=int(input())
    if guess<secretNumber:
        print("Your guess is too low")
    elif guess>secretNumber:
        print("Your guess is too high")
    else:
        break
if guess==secretNumber:
    print("Good job "+name+" you guess my number in "+ str(guessTaken) +" guess")
else:
    print("Nope the number i was thinking was "+str(secretNumber))