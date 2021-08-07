def percentage(marks):
    p = (sum(marks)/400)*100
    return p

marks1 = [45,78,86,77]
p1 = percentage(marks1)

marks2 = [54,87,96,40] 
p2 = percentage(marks2)
# printing the both percentage
print(p1,p2)