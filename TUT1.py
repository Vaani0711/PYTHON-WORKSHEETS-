print("Twinkle , Twinkle little star")
print("  How I wonder what you are ! ")
print("  Up above the world so high, ")
print("  Like a diamond in the sky ")
print("Twinkle , Twinkle little star")
print("  How I wonder what you are ! ")

first = input ("Enter your first name:")
last = input ("Enter your last name :")
print(last , first)

radius = int (input ("Enter the radius :"))
area = 3.14*radius*radius 
print("Area: " , area)

color_list =["red ", " green", "white","black "]
print(color_list[0] , color_list[3])

N = int(input("Enter a number :"))
result = int(N) + int(2*N) +int(3*N)
print("Result:" , result)

values = input("Enter a number :")
nums = values.split(",")
print("Lists" , nums)
print("Tuples", tuple(nums))

c = float(input("Enter :"))
f = (c * (9/5)) + 32 
print( "Farheniet :" , f)

a = int(input("Enter a number :"))
b= int(input("Enter a number :"))
a = a+b 
b = a-b
a = a-b 
print("Swapped values: a =", a, ", b =", b)

a = int(input("Enter a number :"))
if a%2==0:
    print("Its an Even number ")
else:
    print("Odd")
    
year = int(input("Enter the year "))
if (year%4 ==0 and year %100 != 0):
    print("Its a leap year")
else :
    print("Its not a leap year ")
    
import math
x1, y1 = map(float, input("Enter x1 and y1: ").split())
x2, y2 = map(float, input("Enter x2 and y2: ").split())
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", distance)   

a= float(input("enter first anagle :"))
b = float (input("enter second angle :"))
c = float (input("enter third angle :"))
if a+b+c == 180  and a>0 and  b> 0 and  c>0 :
    print("Can form a triangle ")
else :
    print("cant ") 

P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

A = P * (1 + R / 100) ** T
CI = A - P

print("Compound Interest =", CI)
print("Total Amount =", A)

N = int(input("Enter a number: "))
if N > 1:
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print(N, "is NOT a Prime Number")
            break
    else:
        print(N, "is a Prime Number")
else:
    print(N, "is NOT a Prime Number")
    

N = int(input("Enter a positive integer N: "))

sum_squares = (N * (N + 1) * (2 * N + 1)) // 6

print("Sum of squares =", sum_squares)
    
       
    