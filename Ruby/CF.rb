# Classes and Functions Notes

#=begin
	More details on the use of classes and functions within ruby.
#=end

# defining a function

#def is the keyword for a function
def greetings
	puts "Hello!"
end

#just as any other function, you can call them
greetings
#this should provide the output defined above in the function greetings

#just as you can do with any other language, functions can have arguments as below
#or they can have no arguments as above

def greetings_name(name="Em")
	puts "Hello #{name}"
end

greetings_name

#there is the option of having various arguments which would be separated by a comma

#you can also perform an overide of the default values:
greeting_name("Er")

#there is a section on implicit and explicit...these are fairly self explanitory so I did not 
#include any notes on it here

#Blocks and Yields

learn = ["blocks", "yields", "functions"] #here is an array

learn.each do [item]
	puts "I am learning #{item}"
end

#the do loop above wraps a defined block
#so what is yield?

#to test yield, a new function will be defined
def yielding_test
	puts "we are now in the method"
	yield
	puts " we're back in the method"
end

#how to call this method with the block
yielding_test {puts "the method has yieled to the block"}

#I can almost think about this like priority on the stack..because I am saying that whatever is taken
#within the function here is to be yielded to, I can simply call the yield and it will place this output
# between whatever is within the actual block of the function.

#take a look at how this yield handles multiple parameters....
def yield_greet(name)
	puts "we're now in the method"
	yield ("Em")
	puts "in between the yields"
	yield(name)
	puts "we're back in method"
end

#how the call...look at the variable placement here
yield_greet("Erick") {|n| puts "Hello #{n}."}

#=begin
Here is the output to the function above:

we're now in the method
hello Em
in between the yields
hello Erick
we're back in method

#=end

# Classes

#the rules for creating classes isn't unlike the rules for classes in C

class MyClass
end

#within these classes objects can be created
class Car
	def initialize
		puts "the object has now been created"
	end
end

#now that the objects are constructed, you can build more
car = Car.new
#just like you would with most other programs.

#instance variables



