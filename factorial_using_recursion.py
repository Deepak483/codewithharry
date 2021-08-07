def fact_recursive(n):
    if n == 1 :
        return n
    else:
        return n * fact_recursive(n-1)

n = int(input("Enter the number to find the factorial: \n"))
if n<0:
    print("factorial of negative number not exist")
elif n == 0:
    print("factorial of 0 is 1")
else:
    print(f"factorial of {n} is {fact_recursive(n)}")
