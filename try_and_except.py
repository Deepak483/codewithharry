while(True):
    print("Press q to quit the game")
    a =  input("Enter the Number:")
    if a == 'q':
        break
    try:
        print("Trying...")
        a = int(a)
        if a>6:
            print("you entered a number greater  than 6")
        else:
            print("you entered less than 6")
    except Exception as e:
        print(f"Your resulted in an error:{e}")

print("Thanks for playing the game")