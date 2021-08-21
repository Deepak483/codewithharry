from functools import reduce
l = [1,2,4,5,7]
add = lambda x,y: x + y
print("Addition of the number is :"+str(reduce(add,l)))