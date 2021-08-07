t = open("poems.txt",'r')
data = t.read()
if 'twinkle' in data:
    print("Twinkle is present ")
else:
    print("Twinkle is not present")
t.close()