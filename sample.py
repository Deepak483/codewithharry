#filter function
def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

l = [2,4,8,9,10,22,3,7]
filter_object = list(filter(greater_than_5,l))
for item in filter_object:
    print(item)
# print(filter_object)