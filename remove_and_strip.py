this = "   DeepaK  is bad boy.  DEEPak is good and  this and conditional"
def remove_and_strip(string,word):
    newStr1 = string.lower()
    newStr = newStr1.replace(word," ")
    return newStr.strip()

n = remove_and_strip(this," deepak")
print(n)
