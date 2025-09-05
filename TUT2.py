#1 que 
L= [11,12,13,14]

'''L.append(50)
L.append(60 )
print("new list" , l )'''

'''L.remove(11)
L.remove(13)
print(l)'''

L.sort()
print("ASc",L)

L.sort(reverse=True)
print("Descending:", L)


print("13 in list?", 13 in L)


print("Count:", len(L))


print("Sum:", sum(L))


print("Odd Sum:", sum(x for x in L if x % 2 != 0))


print("Even Sum:", sum(x for x in L if x % 2 == 0))


def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

print("Prime Sum:", sum(x for x in L if is_prime(x)))

L.clear()
print("After clear:", L)

del L

#2nd que 
L = [1, 2, 3, 4, 5]
total = 0
for x in L:
    total += x
print("Sum:", total)

#3rd que
l=[ 1,2,3,4,5]
product = 1 
for x in l:
    product *= x
print("Product " , product)

#4th que 
array = [[['*']*6 for j in range (4)]for i in range(3)]
print(array)

#5th que 
D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D[8]=8.8
print(D)
D.pop(2)
print(D)
print("6 is present" , 6 in D)
print(len(D))
D[3]= 7.7
print(D)
total =0
for x in D.values():
    total+=x
print("sum is :" , total)    

D.clear()
print(D)

#6th que 
S1= {10, 20, 30, 40, 50, 60}
S2= {40, 50, 60, 70, 80, 90}
S1.add(55)
S1.add(66)

S1.remove(10)
S1.remove(30)

print(S1)
print("is 40 in S1" , 40 in S1)
print("UNion", S1|S2)
print("intersection" , S1& S2)
print("Difference", S1- S2)

#7th que 

#8th que

for n in range(600, 801):
    if all(n % i != 0 for i in range(2, int(n**0.5)+1)):
        print(n, end=" \n")
        
#9th que lcm le lenge 7 and 9 ka which is 63 
for n in range(100 , 1001):
    if n%63 ==0:
        print(n , end=" ")
    
#10th que  
exam_st_date = (11, 12, 2025)
print("The examination will start from: %i / %i / %i" % exam_st_date)

# 11th que 
numbers = [10, 23, 45, 66, 75, 90, 12, 50]
for n in numbers:
    if n % 5 == 0:
        print(n)

#12th que 
n = int(input("Enter a number: "))
is_even = (n % 2 == 0)
print("Even" if is_even else "Odd")

#13th que 
text = "Emma is good. Emma loves coding. Emma is a student."
print("Emma appears:", text.count("Emma"), "times")
#14th que 
list1 = [10, 21, 32, 43, 54, 65]
list2 = [11, 22, 33, 44, 55, 66]

new_list = [x for x in list1 if x % 2 != 0] + [y for y in list2 if y % 2 == 0]
print("New List:", new_list)
#15th que 
commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
commands_executed = {"MOVE", "TURN_LEFT", "STOP"}

not_executed = commands_received - commands_executed
print("Not executed:", not_executed)
