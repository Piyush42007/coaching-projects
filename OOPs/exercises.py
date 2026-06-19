"""
1. Build a simple class.
Create a class Book with a class attribute format = "Paperback" 
and an instance method read(self) that prints "Reading...". 
Create an instance and call read(), 
then print the class attribute both via the class and via the instance.
"""

class Book:
    Format = "Paperbook"

    def read(self):
        print("Reading...")

book1 = Book()
book1.read()
print(book1.Format)
print(Book.Format)


"""
2. Constructor with attributes.
Create a class Student whose _init_ takes name and grade.
Add a method summary() that prints "<name> is in grade <grade>".
Make two different students and print each summary.
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def summary(self):
        return f"{self.name} is in grade {self.grade}"
    
student1 = Student("alice", 5)
student2 = Student("john", 9)
print(student1.summary())
print(student2.summary())



"""
3. Default argument in _init_.
Create a class Rectangle whose _init_ takes width and height,
with height defaulting to 1. Add an area() method.
Create one rectangle with both dimensions and one using the default height, and print both areas.
"""

class Rectangle:
    def __init__(self, width, height = 1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rec1 = Rectangle(5, 10)
rec2 = Rectangle(10)
print(rec1.area())
print(rec2.area())



"""
4. Independent instances.
Create a class Box with an instance attribute items set to 0 in _init_.
Make two boxes, increment items on the first box only, and print both boxes' items to show they are independent.
"""

class Box:
    def __init__(self,items = 0):
        self.items = items

box1 = Box()
box2 = Box()
box1.items += 5
print(box1.items)
print(box2.items)



"""
5. Counting instances with a class variable.
Create a class Player that keeps a class variable total_players starting at 0,
incremented in _init_. Create three players and print the total.
"""

class Player:
    total_players = 0
    def __init__(self, name):
        self.name = name
        Player.total_players += 1
        

player1 = Player("player1")
player2 = Player("player2")
player3 = Player("player3")
print(Player.total_players)


"""
6. hasattr / getattr.
Create a class Settings with instance attributes theme="dark" and volume=70.
Loop over the list ["theme", "volume", "brightness"] and print each attribute's value, or "(not set)" if it doesn't exist.
"""

class Settings:
    def __init__(self, theme="dark", volume=70):
        self.theme = theme
        self.volume = volume

settings = Settings()

for i in ["theme", "volume", "brightness"]:
    if hasattr(settings,i):
        print(getattr(settings,i))
    else:
        print(i,"(not set)")

"""
7. Instance shadowing a class variable.
Create a class Device with class variable os = "Linux".
Make two devices d1 and d2. Set d1.os = "Windows" on the instance only.
Print d1.os and d2.os and explain (in a comment) why they differ.
"""

class Device:
    os = "Linux"

d1 = Device()
d2 = Device()
d1.os = "Windows"

print(d1.os)
print(d2.os)
# it happens because instence variable take more priority than class variable. so d1.os prints Windows and d2.os prints 
