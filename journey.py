import chapter4 
import time
problems = 4
problems == 4
def journey():
   problems = 4
   problems == 4    
   time.sleep(1)
   print("You traverse the wilds and come across multiple problems")
   time.sleep(1)
   x = int(input("The bridge is broken, solve the problem to find out how much wood you need, 12 x 12 x 12=: "))
   if x == 1728:
        time.sleep(1)
        print("Good Job! move foward")
        problems = problems - 1
   elif x != 1728:
        time.sleep(1)
        print("move foward")
        problems = problems
   y = int(input("The villagers are thirsty, solve the problem to find out how much water is needed, 20 x 10 + 20=: "))
   if y == 220:
        time.sleep(1)
        print("Good Job! move foward")
        problems = problems - 1
   elif y != 220:
        time.sleep(1)
        print("move foward")
        problems = problems
   z = int(input("It's super hot outside the villagers need shade to rest, solve the problem to find out what size tree to rest under, 10 x 7 + 230=:"))
   if z == 300:
        time.sleep(1)
        print("Good Job! move foward")
        problems = problems - 1
   elif z != 300:
        print("some villagers pass out, you wake them up but the day is passing fast")
        problems = problems
   a = int(input("The villagers are hungry, solve this problem to see how many berries to pick, 10 berries per bush, there are 20 villagers, each villager eats two berries. How many bushes do you pick from?= "))
   if a == 4:
        time.sleep(1)
        print("Good Job! move foward")
        problems = problems - 1
   if a != 4:
        time.sleep(1)
        print("wrong, start over")
        chapter4.chapter4()
        problems = problems
   

