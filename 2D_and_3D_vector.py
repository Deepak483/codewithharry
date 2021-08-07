class TwoD_vector:

    def __init__(self,i,j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class ThreeD_vector(TwoD_vector):
    
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = TwoD_vector(4,5)
v3d = ThreeD_vector(9,10,17)
print(v2d)
print(v3d)


