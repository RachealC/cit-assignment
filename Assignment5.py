# create a credit card class with the following attributes:
# card number, expiration date, and security code. 
# Create a method that will print out the card number, expiration date, and security code. 
# Create an instance of the class and call the method.

class Credit_card:
    def _init_(self, card_number, expiration_date, security_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code

    def withdraw(self):
        return(f"Your credit card is {self.card_number} with a an access code {self.security_code} that expires on {self.expiration_date}.")

card = Credit_card('10331000782', 9-10-2024, 52368)
print(card.withdraw())

#  No2.create Animal class and Dog class. Make the Dog class inherit from the Animal class. 
#  Add a bark method to the Dog class. Create an instance of the Dog class and call the bark method.

class Animal:
    def __init__(self, age = 0, weight = 0, animal_is_alive = True):
        # instance attributes
        self.age = age
        self.weight = weight
        self.animal_is_alive = animal_is_alive
    def eat(self,food=None):
        if food==None:
            print('\nThere is nothing to eat :-{{ \n'.format(food))
        else:
            print('\nEating {}...yum yum yum...\n'.format(food))

class Dog(Animal):

    def __init__( self, age = 0, weight = 0, animal_is_alive = True, bark_sound = "hop" ):
        self.bark_sound = bark_sound
        Animal.__init__(self, age, weight, animal_is_alive)
    def bark(self,thisManyTimes=3):
        print('\n')
        for i in range(thisManyTimes):
            print('{}'.format(self.bark_sound), end=' ')
        print('\n')
		

# 3. create a class called Queue. The class should have the following methods: enqueue, dequeue, and size. The enqueue method should add an item to the queue. 
# The dequeue method should remove an item from the queue. The size method should return the size of the queue.

class Queue:
    def __init__(self):
        self.queue = list()

    # check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # add an element to the queue
    def enqueue(self, data):
        # insert method to add element
        self.queue.insert(0, data)
        return True

    # remove an element from the queue
    def dequeue(self):
        if self.isEmpty():
            return ("Queue is empty!")
        return self.queue.pop()

    # get the size of the queue
    def size(self):
        return len(self.queue)

    # display the queue
    def display(self):
        return self.queue

# create a Queue object
q = Queue()

# insert elements to the queue
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)

# display the queue
print(q.display())

# remove an element from the queue
print(q.dequeue())

# display the queue
print(q.display())

# check the size of the queue
print(q.size())

# check if the queue is empty
print(q.isEmpty())

# 4. create a class called Stack. The class should have the following methods: push, pop, and size. The push method should add an item to the stack. 
# The pop method should remove an item from the stack. The size method should return the size of the stack.

class Stack:
    def __init__(self):
        self.stack = list()

    # check if the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        # push element on the stack
        self.stack.append(data)

    # Use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]

    def pop(self):
        # pop element from the stack
        if self.isEmpty():
            return ("Stack is empty. Stack Underflow :(")
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack
# if __name__ == '__main__':
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.show())
print(s.pop())
print(s.show())
print(s.peek())
print(s.size())

# 5. create a class called Person. The class should have the following attributes: name, age, and address. 
# The class should have the following methods: eat, sleep, and work. The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working".

class Person:
  def __init__(self,name,age,address):
    self.Name=name
    self.Age=age
    self.address=address
   
  def eat(self):
    print("{} is eating".format(self.Name))
  
  def sleep(self):
    print("{} is sleeping".format(self.Name))

  def work(self):
    print("{} is working".format(self.Name))

p1 = Person(' Racheal ', 18, 'Bukwo')
p2 = Person(' Ssali', 19, 'Nairobi')
p1.eat()
p1.sleep()
p1.work()

p2.eat()
p2.sleep()
p2.work()

# 6. create a class called Employee. The class should have the following attributes: name, age, and salary. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working". 
# Create a subclass of Employee called Programmer. The Programmer class should have the following attributes: name, age, salary, and programming language.
#  The Programmer class should have the following methods: eat, sleep, work, and code. 
# The code method should print out the name of the person and the word "is coding in" and the programming language.
#  Create an instance of the Programmer class and call all the methods.

class Employee:
  def __init__(self,name,age,salary):
    self.name=name
    self.age=age
    self.salary=salary
   
  def eat(self):
    print("{} is eating".format(self.name))
  
  def sleep(self):
    print("{} is sleeping".format(self.name))

  def work(self):
    print("{} is working".format(self.name))

class Programmer:
    def __init__(self,name,age, salary, programming_language):
        super()._init_(name, age, salary)
        self.programming_language=programming_language
    def start(self):
        print("{} is coding in".format(self.name))
        
  
# 7. create a class called Vehicle. The class should have the following attributes: make, model, and year. The class should have the following methods: start, stop, and drive. The start method should print out the make, model, and year of the vehicle and the word "is starting". The stop method should print out the make, model, and year of the vehicle and the word "is stopping". The drive method should print out the make, model, and year of the vehicle and the word "is driving". Create a subclass of Vehicle called Car. The Car class should have the following attributes: make, model, year, and color. The Car class should have the following methods: start, stop, drive, and park. The park method should print out the make, model, year, and color of the car and the word "is parking". Create an instance of the Car class and call all the methods.

class Vehicle:
    def _init_(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return(f"The release of the {self.make} {self.model} {self.year} model is starting later this year.")

    def stop(self):
        return(f"The release of the {self.make} {self.model} {self.year} model is stopping later this month.")
    
    def drive(self):
        return(f"The Company CEO is driving a {self.make} {self.model} {self.year} model.")

class Car(Vehicle):
    def _init_(self, make, model, year, color):
        super()._init_(make, model, year)
        self.color = color

    def start(self):
        return(f"Start the engine of the {self.color} {self.make} {self.model} {self.year} model right before you.")

    def stop(self):
        return(f"Stop the engine of the {self.color} {self.make} {self.model} {self.year}model right before you.")

    def drive(self):
        return(f"I took my {self.color} {self.make} {self.model} {self.year} model for a test drive around my yard.")

    def park(self):
        return(f"The chauffer is parking the boss' {self.color} {self.make} {self.model} {self.year} vehicle in the VIP parking area.")

vehicle = Vehicle("Range Rover", "Sport", "2018")
print(vehicle.start())
print(vehicle.stop())
print(vehicle.drive())

car = Car("Toyota", "Fortuner", "2020", "Silver")
print(car.start())
print(car.stop())
print(car.drive())
print(car.park())

# 8. create a class called Animal. The class should have the following attributes: name, color, and age. 
# The class should have the following methods: eat, sleep, and make_sound.
#  The eat method should print out the name of the animal and the word "is eating".
#   The sleep method should print out the name of the animal and the word "is sleeping". 
#   The make_sound method should print out the name of the animal and the word "is making a sound". 
#   Create a subclass of Animal called Dog. The Dog class should have the following attributes: name, color, age, and breed. 
#   The Dog class should have the following methods: eat, sleep, make_sound, and bark. 
# The bark method should print out the name of the dog and the word "is barking". Create an instance of the Dog class and call all the methods.

class Animal:
    def __init__(self, name, color, age):
        self.name=name
        self.color=color
        self.age=age

    def _repr_(self):
        return (f"<Animal {self.name} {self.age} {self.color}.")
    def eat(self):
         print("{}is eating".format(self.Name))

    def sleep(self):
        return(f"is sleeping".format(self.Name))
    
    def sound(self):
        return(f"is making a sound".format(self.Name))
class Animal(Dog):
    def _init_(self, name, color, age, breed):
        super()._init_(name, color, age)
        self.breed = breed
    def eat(self):
        return(f"is eating {self.name} {self.age} {self.color}.")

    def sleep(self):
        return(f"is sleeping {self.name} {self.age} {self.color}.")

    def sound(self):
        return(f"is making a sound {self.name} {self.age} {self.color}.")

    def bark(self):
        return(f"is bark {self.name} {self.age} {self.color}.")

animal = Animal("Rexus", "20", "grey")
print(animal.eat())
print(animal.sleep())
print(animal.sound())

dog = Dog("Ravom", "5", "white", "whooaaa")
print(dog.start())
print(dog.stop())
print(dog.drive())
print(dog.park())

    
# 9. create a class of your choice. It should have at least 3 attributes and 3 methods where one of the methods is a static method. 
# Implement polymorphism, encapsulation, and inheritance.

# The parent class
class Space:
  def _init_(self, is_running):
    self.is_running = is_running
  def set_is_running(self, currently_running):
      self.is_running = currently_running
      print(f"{self} is running: {self.is_running}")
# Children classes. We first use the _init_ method to add properties to the class, and the super()._init_ method to inherit all of the parents class functionality
class Air(Space):
  def _init_(self, is_running, cubic_feet):
    self.cubic_feet = cubic_feet
    super()._init_(is_running)
def _str_(self):
    return (f"<{self._class.name_}: {self.cubic_feet}/cuft of air>")
class Electricity(Space):
  def _init_(self, is_running, watts):
    self.watts = watts
    super()._init_(is_running)
  
  def _str_(self):
    return (f"<{self._class.name_}: {self.watts}/watts of electricity>")
class Water(Space):
  def _init_(self, is_running, gallons):
    self.gallons = gallons
    super()._init_(is_running)
def _str_(self):
      return (f"<{self._class.name_}: {self.gallons}/gallons of water>")
# Driver Code
g = Air(False, 236)
e = Electricity(False, 104.2)
w = Water(True, 16)
g.set_is_running(True)
g.set_is_running(False)
e.set_is_running(True)
e.set_is_running(False)
w.set_is_running(True)
w.set_is_running(False)

# Abstraction in Python is the process of hiding the real implementation of an application from the user 
# and emphasizing only how to use the application. 
# Let’s look at examples of abstract classes in Python:

# We import ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod
# Amenity becomes our abstract base class (ABC)
class Space(ABC):
    def turn_on(self):
        pass
# We extend our ABC to three new child classes
class Electricity(Space):
    def turn_on(self):
        print("You flipped the light switch!")
class Water(Space):
    def turn_on(self):
        print("You pressed the faucet up!")
class Air(Space):
    def turn_on(self):
        print("You turned the knob on the stovefront!")
# Driver code
W = Electricity()
W.turn_on()
E = Water()
E.turn_on()
G = Air()
G.turn_on()

# Polymorphism
# The word polymorphism means having many forms. In programming, polymorphism means the same function name is used for different types. 
# When we previously used inheritance, we explicitly linked parent classes to child classes to write reusable code. 
# Polymorphism is achieving the same outcome of shared properties and methods but there is no link between the code; 
# instead, we write the properties and methods to operate in similar 
# and logical ways, allowing us to freely swap classes and methods and being able to expect a similar output.

# Define two classes that have similar implementation and therefore can be mixed and matched in an iteration.
class Air:
    def _init_(self, price, unit):
        self.price = price
        self.unit = unit
    def info(self):
      print(f"I am gas. My price is {self.price}, measured in {self.unit}.")
    def make_sound(self):
      print(f"psssssssssssssss")
class Water:
    def _init_(self, price, unit):
        self.price = price
        self.unit = unit
    def info(self):
      print(f"I am water. My price is {self.price}, measured in {self.unit}.")
    def make_sound(self):
      print("whooooooosh")
# Driver Code
g = Air(0.89, 'cu/ft')
w = Water(0.79, 'gallons')
for space in (g, w):
    space.make_sound()
    space.info()