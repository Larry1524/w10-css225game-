import random
import battle1
import time
def chapter3():
    time.sleep(1)
    print("*you set out to look on your own*")
    time.sleep(1)
    print("You come across two roads, You see claw scratches on one and the other has shredded fabric. which do you follow?")    
    road = int(input("Type 1 for claw road, Type 2 for fabric road:  "))
    if road == 1:
        print("You walk down the road and see a huge monster and the older villagers! but you don't see dave.")
        time.sleep(4)
        print("you slowly back up but it notices you...")
        time.sleep(2)
        print("Monster: where are you going? You shouldn't have came here kid, now you'll pay")
        time.sleep(1)
        print("You try to run but the monster jumps over you and in front of you")
        battle1.battle1()
    elif road == 2:
        print("you walk down the road and see a small bow with a few arrows, you pick them up")
        time.sleep(4)
        print("There are no signs of your brother anywhere...")
        time.sleep(2)
        print("A giant monster approaches you from behind")
        time.sleep(2)
        print("Monster: Another meal...I'm elated")
        time.sleep(1)
        print("You try to run but the monster jumps over you and in front of you")
        battle1.battle1()
    print("just as you're about to be defeated your brother shows up with the rest of the elders and knocks the monster out")

    
    
        