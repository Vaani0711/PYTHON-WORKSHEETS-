# 1st
n = int(input("Enter a number "))
def diff(n):
  if n<=17:
    return (17-n)
  else:
        return (2*abs(17-n))
print(diff(n))     
   
#2nd 
n = int(input("Enter number :"))
def test_range(n):
    if 100<=n<=1000:
        print("yes it lies between 100 and 1000")
        return 
    elif n==2000:
        print("It lies in the range ")  
        return 
    else: 
        return("not in range ")
print(test_range(n))

#3rd 
def reverse_string(s):
    return s[::-1]

print(reverse_string("robot"))

#4th 
s = str(input("enter"))
def count_case(s):
    counts = {"UPPER": 0, "LOWER": 0}
    for ch in s:
        if ch.isupper():
            counts["UPPER"] += 1
        elif ch.islower():
            counts["LOWER"] += 1
    return counts
print(count_case(s))
#5th
def unique_list(lst):
    return list(set(lst))

print(unique_list([1,2,2,3,4,4,5]))
# 6th
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

print(even_numbers([1,2,3,4,5,6,7,8,9]))
# 7th
def robot():
    def move():
        print("Robot is moving...")
    move()

robot()
# 8th 
def student(name, age, course):
    return f"{name}, {age}, {course}"

print(student.__code__.co_varnames[:student.__code__.co_argcount])

#9th 
def move_robot(x, y, direction):
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return (x, y)

print(move_robot(0, 0, "up"))
print(move_robot(0, 0, "right"))

#10th
temp = float(input("Enter the temp:"))
def classify_temperature(temp):
    if temp < 15:
        return "Cold"
    elif 15 <= temp <= 30:
        return "Moderate"
    else:
        return "Hot"

print(classify_temperature(temp))

#11th 
def is_goal_reached(path):
    x, y = 0, 0
    for move in path:
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
    return (x, y) == (2, 0)

moves = input("Enter moves: ").split()
if is_goal_reached(moves):
    print("Goal Reached  at (2,0)")
else:
    print("Goal NOT Reached ")
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        print(f"ID={self.student_id}, Name={self.student_name}, Class={self.student_class}")



student1 = Student(101, "Alice", "10th")
student2 = Student(102, "Bob", "12th")

student1.display()
student2.display()

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(7)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

class StringHandler:
    def __init__(self):
        self.text = ""

    def get_String(self):
        self.text = input("Enter a string: ")

    def print_String(self):
        print(self.text.upper())


obj = StringHandler()
obj.get_String()
obj.print_String()
class Robot:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        self.battery_level = 100

    def perform_task(self):
        if self.battery_level > 0:
            print(f"{self.name} is performing: {self.task}")
            self.battery_level -= 10
        else:
            print(f"{self.name}'s battery is empty. Please recharge!")

    def recharge(self):
        self.battery_level = 100
        print(f"{self.name} is fully recharged!")

    def status(self):
        print(f"Name: {self.name}, Task: {self.task}, Battery: {self.battery_level}%")



r = Robot("RoboX", "Cleaning")
r.status()
r.perform_task()
r.status()
r.recharge()
r.status()

