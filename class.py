class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person('Waqar', 21)
p1.age = 23
# del p1.name # to delete the instance
print(p1)
