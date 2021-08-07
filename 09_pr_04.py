class Sample:
    a = "harry"

    @staticmethod
    def greet():
        print("Hello World!!")

obj = Sample()
obj.a = "Vicky"
Sample.a = "Deepak"

print(obj.a)
print(Sample.a)
print(obj.a)

obj.greet()

