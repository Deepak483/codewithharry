class Animals:
    AnimalsType = "Mammal"

class Pets(Animals):
    Color = "Multicolor"

class Dogs(Pets):

    @staticmethod
    def barks():
        print("Bow Bow!!")

d = Dogs()
d.barks()
d.barks()


