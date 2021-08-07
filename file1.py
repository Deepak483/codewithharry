def game():
    return 483

score = int(game())
with open("hiScore.txt","r") as f:
    hiScoreStr = f.read()

if hiScoreStr == "" :
    with open("hiScore.txt","w") as f:
        f.write(str(score))

elif hiScoreStr<score :
    with open("hiScore.txt","w") as f:
        f.write(str(score))