# Object-oriented programing (OOP)

# Everything in OOP is an object and objects are modled against real life objects.

#Classes are the templates we use to create objects
# Classes are a way of bringing both data and funcionality of our code together

#create a class

class Dog:

    animal_kind = "canine" #class variable

    def bark(self): #method
        return "woof"

# self-"im reffering to the current class."

# print(Dog.animal_kind)
# # print(Dog.bark())

# Instianiation of a class (make an object)

fido = Dog()
lassie = Dog()

print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())

# fido.animal_kind ="Turltle"
Dog.animal_kind = "Dolphin"  #Instance variable

print(fido.animal_kind)
print(lassie.animal_kind)



print(fido.animal_kind) # Now outputs Dolphin

# the dogs can still access their methods
print(fido.bark())