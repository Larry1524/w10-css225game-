import random
correct = 0
correct == 0
def helpkids():
  correct = 0
  correct == 0
  print("Help the kids!")
  kid = random.randint(1, 4)
  if kid == 1:
        kid1 = int(input("Oh no! one of the kids is hanging from a tree! do you get a ladder or stick, 1=ladder, 2=stick: "))
        if kid1 == 1:
            correct = correct + 1
            print("move foward")
            random.randint(2, 4)
        elif kid1 != 1:
            correct = correct + 0
            print("He's ok!")
            random.randint(1, 1)
  if kid == 2:
        kid2 = int(input("One of the kids is going to drown! do you get a raft or bucket? 1=raft, 2=bucket: "))
        if kid2 == 1:
            correct = correct + 1
            print("she didn't drown!")
            random.randint(3, 4)
        elif kid2 != 1:
            correct = correct + 0
            print("oh no")
            random.randint(2, 2)
  if kid == 3:
        kid3 = int(input("The kid hurt himslef and is cut, How will you treat the wound? 1=water,2=ice,3=bandaid,4=ointment: "))
        if kid3 == 3:
            correct = correct + 1
            print("he stops crying")
            random.randint(4,4)
        elif kid3 != 3:
            correct = correct + 0
            print("Oh no")
            random.randint(3, 3)
  if kid == 4:
        kid4 = int(input("a girl is angry because her dairy free milk has spilled and she is thirsty, what do you give her? 1=Dairy Milk,2=almond milk: "))
        if kid4 == 1:
            correct = correct + 1
        if kid4 != 1:
            print("oh no")
            random.randint(4, 4)
  