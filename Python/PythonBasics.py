#####################################################
#PythonBasics
#Lisa Jacklin 
# 8/10/2023
#

#Summary:https://www.learnpython.org/en/Basic_Operators
#Basic python rules and programming pieces that can be used as later reference
#all information gathered here is from learnpython.org and python main site.
#note all notes are in python 3 not earlier versions
######################################################

#printing to the screen
#all three versions below work, noting that the syntax for each is slightly different
print()
print("")
print('')

#indentation
#indentation is important in Python and is the replacement for curly braces

#VARIABLES AND TYPES
#since python is object oriented, and not statically typed, DECLARATION OF VARS IS NOT USED

#numbers:
myint = 7

#floats:
myfloat = 7.0
myfloat = float(7)

#strings"
mystring = 'hello'
mystring = "hello"

#also note that with strings, you can do weird addition pieces
hello = "hello"
world = "world"
helloworld = hello + " " + world

#also note the assignment timing can be done somewhat simultaneously
a, b = 3, 4
print(a,b)

#note: mix operations of this simultaneous style is not allowed or supported.

#example code:
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring) #note this formatting here, how %s is in place and % mystring is telling what string to input
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat) #%f is what float to input
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint) %d is what double to input since int is a double...

#LISTS
#example
mylist = [] #first you need to create a list, noting the brackets used here
mylist.append(1) #then just as normal you can add in vars or values in this case 1
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1 #and of course, you can print these out in a form like this
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

#or you can print in a for loop
# prints out 1,2,3
for x in mylist:
    print(x)

#also note that you can set variables to equal part of a vector
second_name = names[1]

#BASIC OPERATORS

#basic arethmetic operators (add, subtract, multiply, and divide) work as normal

#remainder  which follows the form divident % divisor = remainder (if there is any)
reminder = 11 % 3

#power relations
squared = 7 ** 2 #note two multiplies is what results in what would otherwise be a carat

#operators with strings
#strings can be added together to create different concatenating strings, and multipled as well to repeat a sequence.

#operators with lists
#similar to how it works with strings, this also works with lists

print([1,2,3] * 3) #this will result in 123 being printed 3 times
#adding together two lists also works

#exercise
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#STRING FORMATTING
#strings use classic c stle formatting

name = 'john' 
print ('hello, %s' % name)
#if you have more than one variable, a tuple with parenthesis can be used and must be placed in correct order

#other string formating pieces
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)

#BASIC STRING OPERATIONS