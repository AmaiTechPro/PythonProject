#Class  -Is a blueprint of an object
#An Object - Is an instance of a class i.e to create an object, you must create it outside the class

#1. Object Oriented Programm (OOP) When Having One Object:

class Student:

    #Attributes/Variables
    name = "John"
    gender ="Male"
    age = 23
    course ="Web Development"

    #Behaviour/Method/Function
    def study(self):
        print("Student is studying")

    def eat(self):
        print("Student is eating")


#Creating an object
student1 = Student()
print(student1.name,student1.gender,student1.course,student1.age)
student1.study()
student1.eat()

student2 = Student()

student3 = Student()

student4 = Student()












































































































