# initialisation

# Initialisation --> realtes to setting a particular data for an instance of a class
# iNSTANTIATION => IS THE CREATION OF AN INSTANCE OF THAT OBJECT

class Dog:


    def __init__(self, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()
    def bark(self):
        return "woof"

fido = Dog("Fido", "Brown")

print(fido.name)
print(fido.colour)


# initialising a class with class variables is good practice. it is posible to set variables but it is not advised.