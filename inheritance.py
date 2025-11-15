#Inheritance  - Is the process of a child class acquiring the
#  members (i.e Attributes and Behaviour)
# of the parent 
# class

       #CREATING CLASSES;

#Parent Class/Super Class/Base Class  -Class that the child class is borrowing its members
class Animal:
    #Attribute
    isMammal =True

    #Behaviour
    def sound(self):
        print("Animal is making a sound")


#Clild Class/Sub-Class/Derive Class  -Class that borrows members from the parent class
class Duck(Animal):
    #Attribute
    hasFeathers = True

    #Behaviour
    def swim(self):
        print("Duck is swimming")

class Horse(Duck):
    #Attribute
    isWild =True

    #Behaviour
    def movement(self):
        print("Horse is galloping")


          #CREATING OBJECTS;
a = Animal()
print(a.isMammal)
a.sound()

b = Duck()
print(b.hasFeathers,b.isMammal)
b.sound()
b.swim()

c = Horse()
print(c.isWild,c.isMammal,c.hasFeathers,c.isWild)
c.movement()
c.sound()
c.swim()























