import random
import time

run = True
li = ["s", "w", "g"]

print("Welcome to the game 'Snake-Water-Gun'.\nWanna play? Type Y or N")
b = input()
if b == "N" or b=="n":
    run = False
    print("Ok bubyeee! See you later")
elif b=="Y" or b=="y":
    print("There will be 10 matches and the one who won max matches will win Let's start")

i=0
w=0
l=0
while run and i<10:
    c = random.choice(li)
    a = input("Type s for snake,w for water or g for gun: ")

    if a==c:
        print("Game draws.Play again")
        i+=1
        print(f"{10-i} matches left")

    elif a=="s" and c=="g":
        print(f"It's Snake v/s Gun You lose!")
        i+=1
        l+=1
        print(f"{10-i} matches left")
    elif a=="s" and c=="w":
        print(f"It's Snake v/s Water. You won")
        i += 1
        w += 1 
        print(f"{10-i} matches left")

    elif a=="w" and c=="s":
        print(f"It's Water v/s Snake You lose!")
        i+=1
        l+=1
        print(f"{10-i} matches left")
    elif a=="w" and c=="g":
        print(f"It's Water v/s Gun. You won")
        i += 1
        w += 1
        print(f"{10-i} matches left")

    elif a=="g" and c=="w":
        print(f"It's Gun v/s Water You lose!")
        i+=1
        l+=1
        print(f"{10-i} matches left")
    elif a=="g" and c=="s":
        print(f"It's Gun v/s Snake. You won")
        i += 1
        w += 1
        print(f"{10-i} matches left")

    else:
        print("Wrong input")

if run == True:
    print(f"You won {w} times and computer won {l} times.Final result is...")
    time.sleep(5)
    if w>=4:
        print("Woooh!!!!!!! Congratulations you won")
    elif l==w:
        print("Game draws!!!!!!!")
    else:
        print("You lose!!!.Better luck next time")



