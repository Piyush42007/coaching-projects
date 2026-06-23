"""
 
============================================================
 QUESTIONS
============================================================
"""
"""
----- Part A - Write the Code -----
 
Q1. Write a class Robot with a class attribute kind = "machine"
    and a method greet(self) that prints "Beep boop!". Create an
    instance and call greet().
"""
class Robot:
    kind = "machine"
    
    def greet(self):
        print("Beep boop!")

robot = Robot()
robot.greet()



"""
Q2. Write a class Book whose __init__ takes title, author, and
    pages, storing each on self. Add a summary() method printing
    "<title> by <author>, <pages> pages". Create one book and
    call summary().
"""
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")

book1 = Book("Automate the Boring Stuff with Python", "Al Sweigart", 500)
book1.summary()



"""
Q3. Write a class Rectangle whose __init__ takes width and height
    with height defaulting to 10. Add an area() method. Create one
    rectangle using the default and print its area.
"""
class Rectangle:
    def __init__(self, width, height = 10):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rec1 = Rectangle(10)
print(rec1.area())



"""
Q4. Write a class Student that keeps a shared count of how many
    students have been created. After creating three students,
    print the total.
"""
class Student:
    count = 0

    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        Student.count += 1

std1 = Student("std1", 21, 70)
std2 = Student("std2", 22, 80)
std3 = Student("std3", 23, 90)
print(Student.count)


""" 
Q5. Write a class Temperature with a class attribute
    unit = "Celsius" and an __init__ taking degrees. Add a
    describe() method that prints "<degrees> <unit>".
"""
class Temperature:
    unit = "Celsius"

    def __init__(self, degrees ):
        self.degrees = degrees
    
    def describe(self):
        print(f"{self.degrees}° {Temperature.unit}")

temp = Temperature(37)
temp.describe()


"""
----- Part B - Predict the Output -----
 
Q6.
    class Car:
        def __init__(self, year):
            self.year = year
 
    a = Car(2022)
    b = Car(2024)
    a.year = 2023
    print(a.year, b.year)
 
    What prints? --> 2023 2024
 
Q7.
    # class Employee:
    #     company = "TechCorp"
 
    # e1 = Employee()
    # e2 = Employee()
    # Employee.company = "NewTech"
    # print(e1.company, e2.company)
 
    What prints? --> NewTech NewTech
 
Q8.
    class Employee:
        company = "TechCorp"
 
    e1 = Employee()
    e2 = Employee()
    e1.company = "Freelance"
    print(e1.company, e2.company)
    print(Employee.company)
 
    What prints? --> Freelance TechCorp
                     TechCorp
 
Q9.
    class Config:
        def __init__(self, host, port):
            self.host = host
            self.port = port
 
    cfg = Config("localhost", 8080)
    for attr in ["host", "timeout"]:
        if hasattr(cfg, attr):
            print(attr, "=", getattr(cfg, attr))
        else:
            print(attr, "= (not set)")
 
    What prints? --> host = localhost
                     timeout = (not set)
 
Q10.
    class Team:
        members = []      # class variable (shared!)

        def add(self, name):
            self.members.append(name)

    t1 = Team()
    t2 = Team()
    t1.add("Alice")
    t2.add("Bob")
    print(t1.members)
    print(t2.members)

    What prints, and why might it surprise you? --> ['Alice', 'Bob']
                                                    ['Alice', 'Bob'] 
"""


"""
----- Part C - Fix the Bug -----
 
Q11.
    class Circle:
        def __init__(self, radius):
            radius = radius      # bug
 
        def area(self):
            return 3.14159 * self.radius ** 2
 
    Why does Circle(5).area() fail, and how do you fix it?
"""
class Circle:
        def __init__(self, radius):
            self.radius = radius
 
        def area(self):
            return 3.14159 * self.radius ** 2
        

"""
Q12.
    class Greeter:
        def hello():
            print("Hi!")
 
    g = Greeter()
    g.hello()
 
    What error occurs and how do you fix it?
"""
# method 1
class Greeter:
    def hello(self):
        print("Hi!")
 
g = Greeter()
# g.hello()

# method 2
class Greeter:
    @staticmethod
    def hello():
        print("Hi!")
 
g = Greeter()
g.hello()

"""
Q13.
    class Config:
        def __init__(self, host, port, debug):
            self.akshat = host    # bug: should be self.host
            self.port = port
            self.debug = debug
 
    cfg = Config("localhost", 8080, True)
    print(cfg.host)
 
    Why does the last line fail, and what is the fix?
"""
class Config:
    def __init__(self, host, port, debug):
        self.host = host 
        self.port = port
        self.debug = debug
 
cfg = Config("localhost", 8080, True)
print(cfg.host)





"""
----- Part D - Build It: Bank Account -----
 
Q14. Write a BankAccount class with __init__(self, owner, balance=0).
     Add deposit(amount) that rejects non-positive amounts, and
     withdraw(amount) that rejects non-positive amounts and refuses
     to overdraw (printing "Insufficient funds."). Demonstrate a
     successful deposit, a successful withdrawal, and a failed
     overdraw.
"""
"""
Q15. Extend BankAccount with a class variable interest_rate = 0.03
     and a private-by-convention list self._history. Add
     apply_interest() that adds interest to the balance and logs it,
     and a print_statement() that prints every history entry and the
     final balance. Show that changing BankAccount.interest_rate
     affects all accounts.
 
"""
class BankAccount:
    interest_rate = 0.03

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self._histry = []

    def deposit(self, amount):
        if amount < 0:
            print("amount should be positive")
            return
        self.balance += amount
        self._histry.append(f"Deposit: {amount}, Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount < 0:
            print("amount should be positive")
            return
        
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        self._histry.append(f"Withdraw: {amount}, Balance: {self.balance}")

    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate
        self._histry.append(f"Interest applied: {BankAccount.interest_rate}, Balance: {self.balance}")

    def print_statement(self):
        for entry in self._histry:
            print(entry)


acc1 = BankAccount("Piyush", 1000)
acc1.deposit(100)
acc1.withdraw(100)
acc1.withdraw(5000)
acc1.apply_interest()
acc1.apply_interest()
acc1.apply_interest()
acc1.print_statement()

            


