import random
correct = 0
def chapter1math():
   if correct !=2:
    print("Time to solve some puzzles")
    puzzle = random.randint(1, 4)
    if puzzle == 1:
        Q1 = int(input("What is 5 + 5: "))
        if Q1 == 10:
            correct == correct + 1
            random.randint(2, 4)
        elif Q1 != 10:
            correct == correct + 0
            random.randint(1, 1)
    elif puzzle == 2:
        Q2 = int(input("What is 10 x 10: "))
        if Q2 == 100:
            correct == correct + 1
            random.randint(3, 4)
        elif Q2 != 100:
            correct == correct + 0
            random.randint(2, 2)
    elif puzzle == 3:
        Q3 = int(input("What is 50 - 17: "))
        if Q3 == 33:
            correct == correct + 1
            random.randint(4,4)
        elif Q3 != 33:
            correct == correct + 0
            random.randint(3, 3)
    elif puzzle == 4:
        Q4 = int(input("What is 2 divided by 2: "))
        if Q4 == 1:
            correct == correct + 1
        if Q4 != 1:
            random.randint(4, 4)
    
        
 