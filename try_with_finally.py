try:
    a = int(input("Enter the number"))
    c = 1/a
    print(c)
except ZeroDivisionError:
    print("Division by zero")
    exit()
except ValueError:
    print("Enter the valid input")

finally:
    if a>6:
        print("The number is greater than 6")
    else:
        print("The number is less than 6")