class Vector:

    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        str = ""
        index = 0
        for i in self.vec:
            str+= f"{i}a{index} +"
        return str[:-1]
    
    def __add__(self,vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum+= self.vec[i] * vec2.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)

v1 = Vector([1,2,3])
v2 = Vector([4,5,6])

print(len(v1))
print(len(v2))

