try:
    a = int(input("Enter the number: \n"))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please enter the valid number")
except ZeroDivisionError as e:
    print("Infinite",e)

