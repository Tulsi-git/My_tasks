class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly")

# Creating objects of Sparrow and Ostrich classes
sparrow = Sparrow()
ostrich = Ostrich()
sparrow.fly()
ostrich.fly()
