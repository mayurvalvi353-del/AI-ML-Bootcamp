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

if a > 0 :
    print("Positive number.")
elif a == 0 :
    print("Zero.")
else :
    print("Negative number.")

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
print("Factorial of 5 :", factorial)

#Program to find the greater of two numbers entered by the user.
num1 = int(input("Enter the First number : "))
num2 = int(input("Enter the Second number : "))

if num1 > num2 :
    print("The Largest number is", num1)
else :
    print("The Largest number is", num2)

# Program to find the largest of three numbers.
num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))
num3 = int(input("Enter the Third Number : "))

largest_num = num1

if num2 > num1 :
    largest_num = num2
if num3 > num2 :
    largest_num = num3 

print("The Largest Number : ", largest_num)

#Program to check whether a person is eligible to vote based on age.
age = 22
if age >= 18 :
    print("Eligible!")
else :
    print("Not Eligible!")

#Program to print numbers from 1 to 10 using a while loop.
i = 1
while i <= 10 :
    print(i)
    i += 1

#Program to print all even numbers from 1 to 20 using a while loop.
i = 1
while i <= 20 :
    if i % 2 == 0 :
        print(i)
    i += 1

#Program to display the multiplication table of a number entered by the user.
m = int(input("Enter the number to print the table : "))
i = 1
while i <= 10 :
    print(m,"X",i,"=",m*i)
    i += 1

#Program to check whether a number is divisible by both 3 and 5.
m = int(input("Enter the number : "))
if m % 3 == 0 and m % 5 == 0 :
    print(m,"is divisible by both 3 and 5.")
else :
    print(m,"is not divisible by both 3 and 5.")

#Program to accept five numbers and find their total using a while loop.
i = 1
sum = 0
while i <= 5 :
    m = int(input("Enter the number : "))
    sum += m
    i += 1
print("The Total of numbers :", sum)

#Program to print numbers from 10 down to 1 using a while loop.
i = 10
while i >= 1 :
    print(i)
    i -= 1

num = 76543
result = 0
while num > 0 :
    temp = num % 10
    result = (result*10) + temp
    num //= 10
print(result)

for count in range(100) :
    print(count)

for count in range(1, 10) :
    if count % 2 != 0 :
        print(count)

for count in range(10, 0, -1) :
    print(count)

sum = 0
for count in range(1, 11) :
    sum += count
print(sum)

for count in range(1, 11) :
    print(f"5 X {count} = {5*count}")

for count in range(1, 21):
    if count % 3 == 0 :
        print(count)

factorial = 1
for count in range(1, 6):
    factorial *= count
print(factorial)

#Program to count the number of digits in 98765.
n = 98765
count = 0
while n > 0 :
    count += 1
    n //= 10
print(count)

#Program to calculate the sum of digits of 12345.
n = 12345
sum = 0
while n > 0 :
    temp = n % 10
    sum += temp
    n //= 10
print(sum)

#Program to print numbers from 1 to 10 but stop when the number reaches 7.
n = 1
while n <= 10 :
    print(n)
    if n == 7 :
        break
    n += 1

#Program to print numbers from 1 to 10, skipping multiples of 3.
n = 1
while n <= 10 :
    if n % 3 != 0 :
        print(n)
    n += 1

#Program to calculate the average of 5 numbers using a while loop.
n = 1
sum = 0
while n <= 5 :
    num = float(input("Enter the number : "))
    sum += num
    n += 1
average = sum / 5
print("The Average of the numbers : ",average)

#Program to find the largest number from 5 user inputs using a while loop.
n = 1
largest_number = 0
while n <= 5 :
    num = int(input("Enter the number : "))
    if largest_number == 0 or largest_number < num:
        largest_number = num
    n += 1
print(largest_number)

#Program using a for loop to print numbers from 1 to 5.
for i in range(1, 6) :
    print(i)

#Program to print even numbers from 2 to 10 using a for loop.
for i in range(1, 11) :
    if i % 2 == 0 :
        print(i)

#Program to print odd numbers from 1 to 9 using a for loop.
for i in range(1, 10) :
    if i % 2 != 0 :
        print(i)

#Program to print numbers from 10 down to 1 using a for loop.
for i in range(10, 0, -1) :
    print(i)

#Program to calculate the sum of numbers from 1 to 10 using a for loop.
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

#Program to print the multiplication table of 5 using a for loop.
for i in range(1, 11) :
    print(f"5 X {i} = {5*i}")

#Program to print each item from the list ["Apple", "Banana", "Mango"].
fruits = ["Apple", "Banana", "Mango"]
for i in fruits :
    print(i)

#Program to print each character of the string "Python" using a for loop.
text = 'Python'
for i in text :
    print(i)

#Program to print numbers from 1 to 20 that are divisible by 3.
for i in range(1, 21) :
    if i % 3 == 0 :
        print(i)

#Program to find the factorial of 5 using a for loop.
factorial = 1
for i in range(1, 6):
    factorial *= i
print(factorial)

#Program to count the number of vowels in the string "programming".
string = 'programming'
vowels_count = 0
for i in string :
    if i == 'a' :
        vowels_count += 1
    elif i == 'e' :
        vowels_count += 1
    elif i == 'i' :
        vowels_count += 1
    elif i == 'o' :
        vowels_count += 1
    elif i == 'u' :
        vowels_count += 1
    else :
        continue
print("number of vowels in the string programming :", vowels_count)

#Program to print only positive numbers from [-3, 5, -1, 8, 0, 4].
num = [-3, 5, -1, 8, 0, 4]
for i in num :
    if i > 0 :
        print(i)

#Program to print numbers from 1 to 10 but skip multiples of 3 using continue.
for i in range(1, 11) :
    if i % 3 == 0 :
        continue
    print(i)

#Program to calculate the average of [70, 80, 90, 60, 100] using a for loop.
num = [70, 80, 90, 60, 100]
sum = 0
for i in num :
    sum += i

average = sum/(len(num))
print(average)

num = 0
while num < 10 :
    num += 1
    if num == 5 :
        continue
    else :
        print(num)

i = 1
while i <= 10 :
    if i % 7 == 0 :
        break
    else :
        print(i)
    i += 1

i = 0
while i < 10 :
    i += 1
    if i % 2 == 0 :
        continue
    else :
        print(i)

#Program to print numbers from 1 to 10 and stop the loop when the number reaches 6 using break.
i = 1
while i <= 10 :
    if i == 6 :
        break
    else :
        print(i)
    i += 1

#Program to print numbers from 1 to 10 but skip number 5 using continue.
i = 0
while i < 10 :
    i += 1
    if i == 5 :
        continue
    else :
        print(i)

#Program to print numbers from 1 to 10 and stop when the number is divisible by 7.
i = 1
while i <= 10 :
    if i % 7 == 0 :
        break
    else :
        print(i)
    i += 1
#Program to print numbers from 1 to 10, skipping all even numbers.
i = 0 
while i < 10 :
    i += 1
    if i % 2 == 0 :
        continue
    else :
        print(i)

#Program to search for the number 8 in a list and stop when it is found.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num :
    if i == 8 :
        break
    else :
        print(i)

#Program to print only positive numbers and skip negative numbers.
num = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 10, -10]
for i in num :
    if i < 0 :
        continue
    else : 
        print(i)

#Program to print numbers from 1 to 20 but skip multiples of 3.
for i in range(1, 21) :
    if i % 3 == 0 :
        continue
    else :
        print(i)

#Program to stop searching when the first negative number is found.
num = [1, 2, 3, 4, 5, -5, 6, -6, 7, 8, 9, 10]
for i in num :
    if i < 0 :
        break
    else :
        print(i)

#Program to print all numbers except 0 from a list.
num = [1, 3, 5, 2, 4, 6, 0, 10, 8, 12, 11, 13, 14, 16, 20]
for i in num :
    if i == 0 :
        continue
    else :
        print(i)

numbers = [10, 20, 30 , 40, 50]
print(numbers)
print(type(numbers))

print("First element of numbers :", numbers[0])
print("Second element of numbers :", numbers[1])
print("Third element of numbers :", numbers[2])
print("Fourth element of numbers :", numbers[3])
print("Fifth element of numbers :", numbers[4])

numbers[1] = 100
print(numbers)
print(f'second element : {numbers[1]}')

numbers[0] = numbers[2]
print(f"First element : {numbers[0]}")
print(len(numbers))

myList = ['One', 2, 3.5, True, False, [1, 2, 3]]
print(len(myList))
print(myList)
myList[0] = 1
print(myList)
print(type(myList))

print(len(myList))
del myList[0]
print(len(myList))

print(myList[0])
print(myList[3])

del myList
print(myList)

print(myList[-1])

print(myList[-2])

list = [1, 2, 3, 4, 5]
print(list)
print(len(list))

list.append(6)

print(list)
print(len(list))

list.insert(0, 0)

print(list)
print(len(list))

list = [1, 2, 3, 4, 5]

for i in range(len(list)) :
    print("Element :", list[i])

for i in range(len(list)) :
    print(f'list[{i}] -> {list[i]}')

my_list = []

for count in range(1, 11) :
    my_list.append(count)
print(my_list)

for index in range(len(my_list)) :
    my_list[index] = my_list[index] + 10
print(my_list)

a = 10
b = 20

#1 ----------
#b = a + b
#a = b - a
#b = b - a 

#2 ----------
#c = b
#b = a
#a = c

#3 ----------
#b = a * b
#a = b // a
#b = b // a

a, b = b, a

print(a)
print(b)

#
# list = [8, 10, 6, 2, 4]
list = [2, 4, 8, 6, 10]
count = 0
swapped = True
for index1 in range(len(list)-1) :
    swapped = False
    for index in range(len(list)-(index1 + 1)) :
        count += 1
        if list[index] > list[index + 1] :
            list[index], list[index + 1] = list[index + 1], list[index]
    if swapped == False :
        break
print(list)
print(f"Loop ran for {count} times.")

while swapped :
    swapped = False
    for i in range(len(list) - 1) :
        count += 1
        if list[i] > list[i + 1] :
            swapped = True
            list[i], list[i + 1] = list[i + 1], list[i]

print(list)
print(f"Loop ran for {count} times.")

#Program to create a list of numbers and create a new list containing only the numbers greater than 10.
numbers = [1, 2, 3, 5, 10, 12, 13, 11, 18, 20, 22]
num = []
for i in range(len(numbers)) :
    if numbers[i] > 10 :
        num.append(numbers[i])
print(num)

#Program to create a list of student marks and calculate the average marks.
marks = [22, 39, 42, 25, 55, 34, 47, 49, 30]
sum = 0
for i in marks :
    sum += i
average = sum/(len(marks))

print(average)

#Program to create a list of numbers and count how many numbers are greater than 50.
num = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 102, 113, 124, 135, 146, 150]
count = 0
for i in num :
    if i > 50 :
        count += 1
print(count)

#Program to create a list of numbers and reverse the list using reverse().
my_list = ['n', 'o', 'h', 't', 'y', 'P']
my_list.reverse()
print(my_list)

#Program to create a list of numbers and calculate their sum using sum().
num = [1, 2, 3, 4, 5]
total = sum(num)
print(total)

#Program to create a list of numbers and find the smallest number using min().
num = [1, 2, 3, 4, 5]
smallest = min(num)
print(smallest)

#Program to create a list and remove the last element using pop().
num = [1, 2, 3, 4, 5]
num.pop()
print(num)

#Program to create a list of numbers and find the largest number using max().
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maximum = max(num)
print(maximum)

#Bubble Sort
my_list = [8, 10, 6, 2, 4]
for i in range(len(my_list) - 1) :
    for index in range(len(my_list) - 1) :
        if my_list[index] > my_list[index + 1] :
            my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
print(my_list)

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

list = []
for i in range(0, 500) :
    list.append(i + 1)

#175 - 450
new_list = list[174:450]
print(new_list)

my_list = [10, 8, 6, 4, 2]
my_list1 = my_list[:]
print("21 in my_list :", 21 in my_list)
print("2 in my_list :", 2 in my_list)

print(my_list1)
my_list1[2] = 18
print("21 in my_list :", 21 in my_list)
print("2 in my_list :", 2 in my_list)
print("18 in my_list :", 18 in my_list)

row = []
for i in range(8) :
    row.append("WHITE_PAWN")
print(row)
print(len(row))

row = ["WHITE_PAWN1" for i in range(8)]
print(row)
print(len(row))

squares = [x**2 for x in range(10)]
print(squares)

squares = [x**2 for x in range(11)]
print(squares)

squares = [x**2 for x in range(1, 11)]
print(squares)

twos = [2**i for i in range(11)]
print(twos)

squares = [x**2 for x in range(11)]

odds = [x for x in squares if x % 2 != 0]
print(odds)

for element in squares :
    print(element)

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list[0][0])
print(list[0][1])
print(list[2][1])
print(list[3][3])

board = []
for i in range(8) :
    row = ["EMPTY" for i in range(8)]
    board.append(row)

#print(board)

board[0][0] = "ROOKS"
board[0][7] = "ROOKS"
board[7][0] = "ROOKS"
board[7][7] = "ROOKS"

board[0][1] = "KNIGHT"
board[0][6] = "KNIGHT"
board[7][1] = "KNIGHT"
board[7][6] = "KNIGHT"

print(board)

temps = [[h for h in range(24)] for d in range(31)]
print(temps) 
sum = 0

for i in range(len(temps)) :
    sum += temps[i][11]
average = sum / len(temps)
print(average)

greater = -9999999

for row in range(len(temps)) :
    for col in range(24) :
        if greater < temps[row][col] :
            greater = temps[row][col]
print(greater)'''
