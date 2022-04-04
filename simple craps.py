import random

co = 1

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)

rollone = (d1 + d2)

if rollone == 2 or rollone == 3 or rollone == 12:
    print("CRAP!!!")
    co = 0

if rollone == 7 or rollone == 11:
    print("Win!!!")
    co = 0

if co == 1:
    print("Roll Again")
    print(rollone)



#There you have it!!! A simple version of the dice game "Craps"


