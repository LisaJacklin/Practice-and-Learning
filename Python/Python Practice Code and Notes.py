#Python Practice Code and Notes
#Lisa Jacklin
#8/4/2023
#

#note that some of the examples that I am basing these coding notes on come from codedex.io 
#which is starred in my github for later uses.

#HELLO-WORLD
#either format works with python, single or double quotes so long as they are the same on both ends of the phrases.
print('')
print("")

#VARIABLES
#variables do not require any ending clause and follow the same mathematical formatting as any other language that I have messed with
temp_f = 56
temp_c = (temp_f - 32) /1.8


#for mathematical multiplication, two ** means an exponent so height ^2 essentially. carat is two astrixs
weight = 92.3
height = 1.86
bmi = weight / (height**2)


#in a more direct way, you can ask the user for input that can be used mathematically.

a = int (input("Enter a: ")) #note that input here will take what ever ends this piece and turn it into an int which will represent a
b = int(input("Enter b: "))

c = (a**2 + b**2)**0.5

#note that the format above works for many different inputs that are required, but works best for integers.

#CONTROL FLOW

#just like any other language, there are libraries that you can use!
import random

#this library will allow you to create a random number essentially based on the random library

num = random.randint(0,1) #num is a random integer that ranges from 0 or 1.
#note that randint is a function of the random library that requires two inputs a low and a high for it to randomize.

if num >0.5:
	print('heads')
else:
	print('tails')

#notice the way this if statement is situated.
#at the end of each if/else there is : rather than curly brackets.


#SOMETHING MORE DIFFICULT....
import random

#as I mentioned above, you can use input as truly anything with something mentioned before to prompt or no prompt at all.
question = input()

#you must give a random range for this to work
random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2: #notice the elif which is else if but in python!
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Question:      ' + question) 
print('Magic 8 Ball:  ' + answer)
