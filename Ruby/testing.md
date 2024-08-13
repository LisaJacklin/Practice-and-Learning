#Testing Ruby Code

Test driven development provides an easy way to test for problems, find solutions and 
determine if there is any other problems that your soluion might encounter.

Proper test writing is important to help avoid programs from crashing

## Test::Unit

Test::Unit is a standard ruby library for unit testing, so no other dependencies need
to be installed in order to operate properly.

### Example using Test::Unit
``` 
require "test/unit/assertions"
include Test::Unit::Assertions
hello = "Hello world!"
assert_equal "Hello World!", hello, "function should return 'Hello World!'"

 ```
There are many different Assertion functions that can help with testing.
An assetion is simply a pass or fail test

## RSpec

RSpec focuses on behavior driven development which relies on block deugging and issolation.
A unit test here may be based ona function, module, or class.

This foccusses on human-readable descriptions for the software tests.

### Requirements to get RSpec
```
gem install rspec
respec --init #check the install

#expected output
create .rspec
create spec/spec_helper.rb
```
This last warning provides a file where you can include/exclude directories or files
that should be run while the spec_helper.rb will be the decider on how RSpec will behave 
run.

### Writing a RSpec Test
1. first specify what you want to test
2. create a test file and place in the spec directory
3. run the test.

```
#test goes onto this code block
class Greetings 
	def self.say_hello
		'Hello!'
	end
end

#how to create the test file
require_relative '../hello'

RSpec.describe Greetings do
	context :#greetings" do
		it { expect (Greetings.say_hello).to eql 'Hello!'}
	end
end

#then of course to run it
respec hello_spec.rb
```


## Minitest

more notes to come soon here....
