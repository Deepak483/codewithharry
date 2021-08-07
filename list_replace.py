list = ["donkey","kaddu","shit","mote"]

with open("sample.txt") as f:
    content = f.read()


for word in list:
    content = content.replace(word,"%$&#@^$#")
    with open("sample.txt","w") as f:
        f.write(content)