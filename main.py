# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. 
# Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        return (f'Name:{self.name}, Marks:{self.marks}')
student1:Student=Student("Iqra Ehsan",96)
student2:Student=Student("Ali Raza",91)
print("Student 1 Details:",student1.display())
print(student1.name,student1.marks)
print("Student 2 Details: ",student2.display())
print(student2.name,student2.marks)

# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count=0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def display_count(cls):
        return f'Total objects created: {cls.count}'
obj1:Counter=Counter()
obj2:Counter=Counter()
obj3:Counter=Counter()
print(Counter.display_count())

# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.

class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print(f"{self.brand} car is starting....")

my_car=Car("Toyota")
print(my_car.brand)
my_car.start()

# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) 
# that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name="State Bank"
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name=name
b1=Bank()
b2=Bank()
print(b1.bank_name)
Bank.change_bank_name("National Bank")
print(b2.bank_name)

# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
     @staticmethod
     def add(a,b):
         return a+b
print(MathUtils.add(5,3))

# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message
#  when it is destroyed (destructor).

class Logger:
    def __init__(self):
         print("Logger object created.")
    def __del__(self):
        print("Logger object destroyed.")

# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn          # private

emp = Employee("Ali", 50000, "123-45-6789")

print(emp.name)          # public
print(emp._salary)        # protected
print(emp._Employee__ssn) # private via name mangling

# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor. 

class Person:
    def __init__(self,name):
        self.name=name
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
t=Teacher("Sara","Math")
print(t.name,t.subject)

# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
r=Rectangle(4,5)
print(r.area())

# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. 
# Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name,bread):
        self.name=name
        self.bread=bread
    def bark(self):
        print(f"{self.name} says Woof!")
d=Dog("Buddy","Labrador")
d.bark()

# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. 
# Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)

# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c*9/5)+32
print(TemperatureConverter.celsius_to_fahrenheit(0))

# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization.
# Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self,engine):
        self.engine=engine
    def start(self):
        self.engine.start()
e=Engine()
c=Car(e)
c.start()

# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by
#  having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

e = Employee("Ayesha")
d = Department(e)
print(d.employee.name)

# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:

# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B,C):
         pass

d=D()
d.show()

# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. 
# Apply it to a function say_hello().

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper
@log_function_call
def say_hello():
     print("Hello!")
say_hello()

# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". 
# Apply it to a class Person.

def add_greeting(cls):
    cls.greet=lambda self: "Hello from Decorator!"
    return cls
@add_greeting
class Person:
    pass
Person =add_greeting(Person)
p=Person()
print(p.greet())

# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter 
# to update it, and @price.deleter to delete it.

class Product:
    def __init__(self,price):
        self._price=price

    @property 
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        self._price=value
    @price.deleter
    def price(self):
        del self._price

p=Product(100)
print(p.price)
p.price=200
print(p.price)
del p.price

# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor.
#  Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self,factor):
        self.factor=factor
    def __call__(self,value):
        return self.factor*value

m=Multiplier(3)
print(callable(m))
print(m(5))

# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18.
#  Handle it with try...except.

class InvalidAgeError (Exception):
    pass 
def check_age(age):
    if age<18:
        raise InvalidAgeError("Age must be 18 or above.")
    else:
        print("Age is valid.")
try:
    check_age(16)
except InvalidAgeError as e:
    print("error:",e)

# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number.
#  Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self,start):
        self.start=start
       
    def __iter__(self):
        self.n=self.start
        return self
    def __next__(self):
        if self.n<0:
            raise StopIteration
        current=self.n
        self.n-=1
        return current
for number in Countdown(5):
    print(number)