class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.bark())
print(f"{dog1.name} is {dog1.age} years old.")
