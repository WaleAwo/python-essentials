# organise variables and function into a single organised unit
# can either be a single file per class or multiple classes can be contained in one file
import random


# __init__ function
# sets attributes for an object at object creation; *CONSTRUCTOR*
# not required but is generally used to set default state of object when it is created

# __str__ function
# string representation of a class object

# self
# used to reference the object that is constructed by the init method

# creating a class
class Person:
    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.health}, {self.status}"

    def introduce(self):
        print("Hello, my name is {} {}.".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1, 3)
        if emotion == 1:
            print("{} is happy today.".format(self.firstname))
        elif emotion == 2:
            print("{} is sleepy today.".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} feels okay.".format(self.firstname))
        elif self.health >= 50:
            print("{} feels unwell.".format(self.firstname))
        else:
            print("{} goes to the doctor.".format(self.firstname))


# creating an instance of a class
Maria = Person("Maria", "Jones", 90, status=True)
Rey = Person("Rey", "Andrews", 65, status=False)
Lee = Person("Lee", "Jan", 40, status=True)
Lucy = Person("Lucy", "Marks", 72, status=True)

# using instance attributes
print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

# using clss methods
Maria.introduce()
Maria.emote()
Maria.status_change()

# print object
print(Maria)


# Inheritance
# uses the attribute and methods from one class in another class
# use the 'super' method to access attributes from the parent class

class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)  # initialise parent attributes
        self.weapon = weapon  # set unique child attribute

    # overrides parent method
    def introduce(self):
        print("You are my mortal enemy!!!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak!".format(other.firstname))

    def steal(self, other):
        print("Ha, {}, I have your stuff".format(other.firstname))
        if other.status:
            other.status = False


Alex = Enemy('rock', "Alex", "Reid", 67, status=False)  # create a child object
Alex.hurt(Maria)
Alex.insult(Lee)
Alex.steal(Lucy)
