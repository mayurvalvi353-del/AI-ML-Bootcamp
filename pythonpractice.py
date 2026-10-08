'''print("Hello World")
print("How are you ?"); print("Hii")

print("Line test"); print("No this will not work")

print("This is demo of print", end="***")
print("\n \tThis", "is", "the", "demo", "of", "print", sep=" ")
print("House-"*5)
print("*"*20)

name = "Mayur"
profession = "Python Developer"
experience = 3
print("Hello, My Name is", name, ". I am a", profession, "professionally and I have around", experience, "months experience in it.")

x = 5
print("x :", x)
print("Type of x :", type(x))
x = "Hello World"
print("x :", x)
print("Type of x :", type(x))
x = 20.5
print("x :", x)
print("Type of x :", type(x))
x = 1j
print("x :", x)
print("Type of x :", type(x))
x = ["apple", "banana", "cherry"]
print("x :", x)
print("Type of x :", type(x))
x = ("apple", "banana", "cherry")
print("x :", x)
print("Type of x :", type(x))
x = {"name" : "John", "age" : 36}
print("x :", x)
print("Type of x :", type(x))
x = {"apple", "banana", "cherry"}
print("x :", x)
print("Type of x :", type(x))
x = frozenset({"apple", "banana", "cherry"})
print("x :", x)
print("Type of x :", type(x))
x = True
print("x :", x)
print("Type of x :", type(x))
x = b"Hello"
print("x :", x)
print("Type of x :", type(x))
x = bytearray(5)
print("x :", x)
print("Type of x :", type(x))
x = memoryview(bytes(5))
print("x :", x)
print("Type of x :", type(x))
x = None
print("x :", x)
print("Type of x :", type(x))

x = 10
y = 14

z = x + y
print(z)

z = x - y
print(z)

z = x * y
print(z)

z = x / y
print(z)

z = y / z
print(z)

z = y // x
print(z)

z = y % x
print(z)

print(5 ** 2)
print(3 ** 5)

a = 10
b = 15

print("a == b :", a == b)
print("a < b :", a < b)
print("a > b :", a > b)
print("a <= b :", a <= b)
print("a >= b :", a >= b)

a = 10
b = 12
c = 14

print(a is 10)
print(a is 12)
print(a is not 10)
print(a is not 12)

name = input("Please enter your name : ")
print("Hello,", name)

x = int(input("Enter first value for sum : "))
y = int(input("Enter second value for sum : "))
z = x + y
print("Sum :", z)

x = input("Enter first value for sum : ")
y = input("Enter second value for sum : ")
z = int(x) + int(y)
print("Sum :", z)

x = input("Enter first value : ")
# a variable is assigned as x for storing the first value which will taken as input.
y = input("Enter second value : ")
# same a variable as y is assigned for storing the second value which will taken as input. 
z = int(x) * int(y)
# a variable z is assigned to store the result of multiplication & int is written to perform type conversion in both the values.
print("Product :", z)
# displays the result of multiplication

print("2 == 2 :", 2==2)
print("2 == 2. :", 2==2.)
print("'abc' == 'abc' :", 'abc' == 'abc')
abc = 2
print('abc' == abc)
print(2 == abc)
print(1 == abc)
abc = 0
print(1 == abc)

age = int(input("Enter the Age : "))
if age >= 21 :
    print("Eligible for Marriage!"

num = -5
if num > 0 :
    print("The number is positive.")
elif num == 0 :
    print("The number is Zero.")
else :
    print("The number is negative.")

num = 5
if num % 2 == 0 :
    print("The number is even.")
else : 
    print("The number is odd.")

marks = 45
if marks >= 40 :
    print("Pass")
else :
    print("Fail")

a = 25
b = 20

if a > b :
    print("10 is larger number.")
elif a == b :
    print("Both the numbers are equal.")
else :
    print("20 is larger number.")

a = 25
if a % 3 == 0 and a % 5 == 0 :
    print("The number is divisible by both 3 & 5.")
else : 
     print("The number is not divisible by both 3 & 5.")

marks = int(input("Enter the marks :"))
if marks >= 90 :
    print("A grade")
elif 75<=marks<=89 :
    print("B grade")
elif 50<=marks<=74 :
    print("C grade")
else :
    print("F grade")


num = 1

while num <= 5:
    print(num)
    num += 1

num = 2

while num <= 10 :
    if num % 2 == 0 :
        print(num)
    num += 1

while num <= 10 :
    print(num)
    num += 2

num = 1
while num <= 9 :
    if num % 2 != 0 :
        print(num)
    num += 1

num = 10
while num >= 1 :
    print(num)
    num -= 1

sum = 0
num = 1
while num <= 10 :
    sum += num
    num += 1
print("Sum :", sum)

num = 1
while num <= 10 :
    print(num * 5)
    num += 1

num = 1
while num <= 10 :
    if num > 5 :
        print(num)
    num += 1

num = 1
while num <= 20 :
    if num % 3 == 0 :
        print(num)
    num += 1

factorial = 1
num = 5
while num >= 1 :
    factorial *= num
    num -= 1
print("Factorial of 5 :", factorial)'''
