# A game where you must guess the number the computer is thinking of. The number will be between 1 and 10 and you will have 3 guesses. Every time you make an incorrect guess the computer will tell you if the number it is thinking of is greater or less than your guess. HAVE FUN!!!
import random

t = 3
i = 0

print("You have three tries to guess a number between 1 and 10. Every incorrect attempt will tell you that the number is either lower or higher. Good Luck!!!")
print("...")

cgn = random.randint(1, 10)

guess = input("What is your guess? : ")
t = 2

if guess == "1":
    guess = 1
elif guess == "2":
    guess = 2
elif guess == "3":
    guess = 3
elif guess == "4":
    guess = 4
elif guess == "5":
    guess = 5
elif guess == "6":
    guess = 6
elif guess == "7":
    guess = 7
elif guess == "8":
    guess = 8
elif guess == "9":
    guess = 9
elif guess == "10":
    guess = 10
else:
    print("invalid guess")
    print("play again and make a valid guess")
    i = 1

if i == 0:
    if guess == cgn:
        print("YOU WIN!!! The number was", cgn)
        i = 1
    elif guess < cgn:
        print("The Number is Greater than that guess... only", t, "tries left!")
    elif guess > cgn:
        print("The Number is Less than that guess... only", t, "tries left!")
    else:
        print("WTF was ur guess lmao")


if i == 0:
    guess = input("What is your guess? : ")
t = 1

if guess == "1":
    guess = 1
elif guess == "2":
    guess = 2
elif guess == "3":
    guess = 3
elif guess == "4":
    guess = 4
elif guess == "5":
    guess = 5
elif guess == "6":
    guess = 6
elif guess == "7":
    guess = 7
elif guess == "8":
    guess = 8
elif guess == "9":
    guess = 9
elif guess == "10":
    guess = 10
else:
    if i == 0:
        print("invalid guess")
        print("play again and make a valid guess")
        i = 1




if i == 0:
    if guess == cgn:
        print("YOU WIN!!! The number was", cgn)
        i = 1
    elif guess < cgn:
        print("The Number is Greater than that guess... only", t, "tries left!")
    elif guess > cgn:
        print("The Number is Less than that guess... only", t, "tries left!")
    else:
        print("WTF was ur guess lmao")


if i == 0:
    guess = input("What is your guess? : ")
t = 0

if guess == "1":
    guess = 1
elif guess == "2":
    guess = 2
elif guess == "3":
    guess = 3
elif guess == "4":
    guess = 4
elif guess == "5":
    guess = 5
elif guess == "6":
    guess = 6
elif guess == "7":
    guess = 7
elif guess == "8":
    guess = 8
elif guess == "9":
    guess = 9
elif guess == "10":
    guess = 10
else:
    if i == 0:
        print("invalid guess")
        print("play again and make a valid guess")
        i = 1


if i == 0:
    if guess == cgn:
        print("YOU WIN!!! The number was", cgn)
    elif guess < cgn:
        print("YOU LOSE!!! The number was", cgn, "LOL!", t, "tries left!")
    elif guess > cgn:
        print("YOU LOSE!!! The number was", cgn, "LOL!", t, "tries left!")
    else:
        print("WTF was ur guess lmao")


