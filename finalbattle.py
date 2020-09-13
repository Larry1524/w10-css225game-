import chapter5
import time
x = 0
x == 0
def finalbattle():
    x == int(input("One Question determines your fate!, What did the child that you and your brother helped lose, 1=Milk,2=Money,3=Doll,4=clothes"))
    if x == 3:
        time.sleep(1)
        print("You give the mother monster a good hit and she falls")
        time.sleep(4)
        print("YOU WIN!")
    elif x != 3:
        time.sleep(1)
        print("The mother eats everyone...game over, try again")
        time.sleep(3)
        chapter5.chapter5()
