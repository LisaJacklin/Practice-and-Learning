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



