import random

def gameWin(comp,user):
    
    if comp == user:
        return None
    
    elif comp == 's':
        if user == 'g':
            return True
        elif user == 'w':
            return False

    elif comp == 'w':
        if user == 's':
            return True
        elif user == 'g':
            return False

    elif comp == 'g':
        if user == 'w':
            return True
        elif user == 's':
            return False


print("Computer Turn: Snake(s),Water(w),Gun(g)?")
randNo = random.randint(1,2)


if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

user = input("Your Turn: Snake(s),Water(w),Gun(g)?: ")

a = gameWin(comp,user)

print("******************")
print(f"Comp Choose ({comp})")
print(f"You Choose ({user})")
print("******************")

if a == None:
    print("Game Tie!!")
elif a == True:
    print("You Win!!")
else:
    print("Computer Win!!")


