import chapter3
import random
def battle1():
    print("The monster begins its attack, to win you must solve the following problems")
    attack = random.randint(1, 4)
    if puzzle == 1:
        Q1 = int(input("What is 500 + 500: "))
        if Q1 == 1000:
            print("you make hit")
            puzzle = random.randint(2, 4)
        elif Q1 != 1000:
            print("you get hit")
            puzzle = random.randint(2, 4)
    if puzzle == 2:
        Q2 = int(input("What is 10 + (500 x 3): "))
        if Q2 == 1510:
            print("you make hit")
            puzzle = random.randint(3, 4)
        elif Q2 != 1510:
            print("you get hit")
            puzzle = random.randint(3, 4)
    if puzzle == 3:
        Q3 = int(input("What is 500 - 170: "))
        if Q3 == 330:
            print("you make hit")
            puzzle = random.randint(4,4)
        elif Q3 != 330:
            print("you get hit")
            puzzle = random.randint(3, 3)
    if puzzle == 4:
        Q4 = int(input("What is 525 + 75: "))
        if Q4 == 600:
            print("you make a hit")
            puzzle = random.randint(1, 4)
        elif Q4 != 600:
            print("you get hit")
            puzzle = random.randint(4, 4)
 



