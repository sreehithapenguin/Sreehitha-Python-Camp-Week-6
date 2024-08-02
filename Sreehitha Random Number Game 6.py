
import random

#for i in range(10,20,2):
#    print(i)


#for i in range(20):
#    print(random.randint(1,100))

'''print("Welcome to the fortune teller")
print("Your fortune is...")
random=random.randint(1,3)

if random==1:
    print("You will win a million dollars.")
elif random==2:
    print("You will get a pet cat.")
elif random==3:
    print("You will travel to a different country.")'''


password="penguin"

guess=input("Guess the password: ")

while guess!=password:
    guess=input("Guess again: ")

print("Welcome to the Random Number Guessing Game")
number=random.randint(1,100)
score=1

guess=int(input("Guess the number 1-100: "))

while guess!=number:
    score=score+1
    print("Incorrect")
    if guess>number:
        print("You guessed too high")
    elif guess<number:
        print("You guessed too low.")
    guess=int(input("Guess again"))

print("Good job you got it. The number was",number)
print("It took you",score,"tries. Good job!")

    

















    
