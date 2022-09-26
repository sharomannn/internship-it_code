# Fundamentals in Python

''' x // y - Получение целой части от деления
x%y - Остаток от деления
abs(x) - Модуль числа

'''

# number = input()
# print(number)
#
# x = 50
# y = 13
# integer = x // y
# remainder = x % y
# print(x, ' / ', y, ' = ', integer, ' целая часть')
# print(x, ' / ', y, ' = ', remainder, ' остаток')
#
# myNumber = int(input("Enter a number: "))
# if (myNumber % 2 == 0) and myNumber != 0:
#     print("The number is even.")
# elif myNumber == 0:
#     print('Error 0')
# else:
#     print("The number is odd.")


# Cycle while
count = 1
while count <= 5:
    print(count)
    # if count == 4:
    #     break
    #     continue
    count = count + 1


# Cycle for
words = ['hello','world','hi']
for word in words:
      print(word)

for i in range(3):
    print('hello')


# range
numbers = list(range(10))
numbers = list(range(3,10))
numbers = list(range(3,10,2))
print(numbers)


# Functions
def greetings():
    print('Hey')
    print('Hellooooo')
greetings()


# Functions can take arguments
def add(x,y):
    print(x+y)
add(5,8)


# Certain functions return
def max(x,y):
    if x>=y:
        return x
    else:
        return y
z=max(8,5)
print(z)


# get the letters of a string separately
print('Python'[0])
print('Python'[0:2])


# Splitting a String
sentence = "Pythonista Planet"
words = sentence.split()
print(words)


# Lists in Python
words= ['Hello','world','how','are','you']
print(words[0])

things= ['mango',0,[1,2],4.56]
print(things[2][1])


# List functions
numbers= [1,2,3]
numbers.append(4)
print(numbers)

words = ['python','fun']
words.insert(1,'is')     # (position,item)
# words.remove('python')
words.pop('-1')
print(words)

numbers= [1,2,3,4,5]
print(len(numbers))

max(list)               #To find the maximum value from a list
min(list)               #To find the minimum value from a list
list.remove('python')   #(item)	To remove an item from a list
list.reverse()          #To reverse a list
list.pop(-1)


# Modules in Python
import random
for i in range(5):
    value= random.randint(90,99)
    print(value)


# only certain methods or values from a module
from math import sqrt,pi
from math import sqrt as square_root


# Dictionaries in Python
phone_book = {
              'John' : '8592000000',
              'Bob' : '7994000000',
              'Elisa' : '9749777777'
            }
print(phone_book['John'])

phone_book[ 'Adam' ] = '9567974800'  # Adding a new item into the dictionary
phone_book[ 'John' ] = '1567933400'  # Update our dictionary

# Looping through a dictionary
for k,v in phone_book.items():
    print(k, ":", v)


# Tuples in Python
exam_register_numbers = ('15001147' , '15001148' )
print(exam_register_numbers[0])

numbers = (0,1,2,3,4,5)
numbers[0]
numbers[1:4]
numbers[:]    #all elements
numbers[::2]



# Sets in Python
groceries = {'apple', 'mango', 'apple'}
print(groceries)

A = {2,3}
B = {1,2}
print(A|B)
print(A&B)
print(A-B)


# try-except
try:
    mango = " juice "
    print(mango/0)
except:
    print("Error")