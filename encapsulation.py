class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

# Creating an object of the Person class
person = Person("Alice", 30)
print(person.get_name())
print(person.get_age())
person.set_age(35)
print(person.get_age())
