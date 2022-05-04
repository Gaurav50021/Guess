from random import random


import random
er=random.randint(0,5)
nr=random.randint(0,10)
hr=random.randint(0,50)
i=1


print("------------Guessing Game------------")
print("---------welcome to Guess Me---------")
space=input("---------Enter C to continue---------")
if space=='c'or space=="C":
    print("\n\nPlease Choose the difficulty")
    difficulty=input("Enter 'E' for Easy Mode\nEnter 'N' for Normal Mode\nEnter 'H' for Hard Mode\n")
    if difficulty=='E' or difficulty=='e':
        print("You choose Easy Mode")
        print("You will get 3 chances to guess")
        while i<=3:
            guess=int(input("Guess a number between 0 to 5: "))
            if guess==er:
                print("you win!!")
                i=4
            else:
                i=i+1
        if guess!=er:
            print("You loooose!!")



    elif difficulty=='N' or difficulty=='n':
        print("You choose Normal Mode")
        print("You will get 3 chances to guess")
        while i<=3:
            guess=int(input("Guess a number between 0 to 10: "))
            if guess==nr:
                print("you win!!")
                i=4
            else:
                i=i+1
        if guess!=nr:
            print("You loooose!!")



    elif difficulty=='H' or difficulty=='h':
        print("You choose Hard Mode")
        print("You will get 3 chances to guess")
        while i<=3:
            guess=int(input("Guess a number between 0 to 50: "))
            if guess==er:
                print("you win!!")
                i=4
            else:
                i=i+1
        if guess!=hr:
            print("You loooose!!")


    else:
        print("Invalid choice")