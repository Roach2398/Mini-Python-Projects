import random

user = input("Type 1 for rock, 2 for paper, or 3 for scissors: ")
cp = random.randint(1,3)
wc = 0

cc = "Invalid"
uc = "Invalid"

if cp == 1 and user == "2":
    print("You Win!!!")
    wc = 1

if cp == 2 and user == "3":
    print("You Win!!!")
    wc = 1

if cp == 3 and user == "1":
    print("You Win!!!")
    wc = 1

if cp == 2 and user == "1":
    print("You Lose...")
    wc = 1

if cp == 3 and user == "2":
    print("You Lose...")
    wc = 1

if cp == 1 and user == "3":
    print("You Lose...")
    wc = 1


if cp == 1 and user == "1":
    print("It's a tie...")
    wc = 1

if cp == 2 and user == "2":
    print("It's a tie...")
    wc = 1

if cp == 3 and user == "3":
    print("It's a tie...")
    wc = 1


if cp == 1:
    cc = "Rock"
elif cp == 2:
    cc = "Paper"
else:
    cc = "Scissors"

if user == "1":
    uc = "Rock"
elif user == "2":
    uc = "Paper"
else:
    uc = "Scissors"


if wc == 1:
    print("You chose", uc, "and the computer chose", cc)



if user != "1" and user != "2" and user != "3":
    print("Error, Invalid Input")
    print("You said...", user)


