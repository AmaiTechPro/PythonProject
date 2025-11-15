#Object Oriented Program(OOP) when having more than one object i.e 5 Students
class Dog:
    #Attributes/Variables/Details 
    def __init__(self, name, breed, age):
        self.name =name
        self.breed = breed
        self.age = age



#Creating Objects
dog1 =Dog("Tito","German Shepherd", 3)
print(dog1.name,dog1.breed,dog1.age)


dog2 = Dog("Bob","Chihuahua", 5)
print(dog2.name,dog2.breed,dog2.age)


dog3 =Dog("Jane", "Siberian Husky", 4)
print(dog3.name,dog3.breed,dog3.age)


#Example 2

#Create Class

class Employee:

    #Attributes/Variables/Details
    name = "Amai"
    gender ="Male"
    age = 21
    grade = "A"
    salary = 300,000
    maritalstatus = "Married"


#Behaviour/Functions/Method
def work(self):
    print("The employee is working smart")


#Create the object

Employee1 =Employee()
print(Employee1.name,Employee1.gender,Employee1.age,Employee1.salary,Employee1.maritalstatus,Employee1.salary)

Employee1.work()













































