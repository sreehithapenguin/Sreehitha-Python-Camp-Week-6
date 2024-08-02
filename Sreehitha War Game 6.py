'''anything=["penguin",25,False,5.53]

print(anything[1])
anything.append("random")
print(anything)

anything.remove(False)
print(anything)'''

import random

print("Welcome to the number war game")
myHand=[]
compHand=[]

for i in range(10):
    myHand.append(random.randint(1,100))
    compHand.append(random.randint(1,100))

print("Here is your hand: ")
print(myHand)
print("Here is the computers hand: ")
print(compHand)

score=0
cscore=0

for i in range(10):
    print("Here is your updated hand: ")
    print(myHand)
    choice=int(input("Choose a number"))
    while choice not in myHand:
        choice=int(input("Choose a number"))
    print("You played a",choice)
    myHand.remove(choice)
    compChoice=random.choice(compHand)
    compHand.remove(compChoice)
    print("The computer chose",compChoice)
    if choice>compChoice:
        print("You won this round")
        score+=2
    elif choice<compChoice:
        print("You lost this round")
        cscore+=2
    else:
        print("Tie")
        compHand.append(compChoice)
        myHand.append(choice)

if score>cscore:
    print("You won this war.")
else:
    print("Computer won this war.")
        












    
