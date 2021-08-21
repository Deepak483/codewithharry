try:
    num = int(input("Enter the number :\n"))
except ValueError:
    print("Enter the valid integer value")

l = list(num*i for i in range(1,11))
print(l)
with open("Tables.txt","a") as f:
    f.write(str(l))
    f.write("\n")