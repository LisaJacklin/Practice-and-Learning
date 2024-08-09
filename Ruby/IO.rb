#File IO notes

#Creating a File
test_file = File.new ("test.txt", "w+")
#note that file is a built in class
# also note that w+ sets the mode to read and write access
# and of course the name and type of the file.

#=begin
	There are several different modes for different files:
	r: default mode in Ruby for read only access
	r+: starts at the beginning of the file, provides read and write access
	w: provides write only access
	w+: provide read and write access
	a: write only with appending to end of file
	a+: provide both read and write access with append to end
#=end

#to read from the file, a simple call can be done
File.read("test.txt")

#this only read or load the file and WILL NOT display the content to the console

#you can write to files using puts or write
test_file = File.open("test.txt","w+")
test_file.puts("We're writing some text to file")
test_file.close #when not using a code block you need to close the file

#to use a code block you can use a style like this:
File.open("test.txt","w+") {
	|file| file.puts("This text was added using code block")

}

#now to read the file again to see if this really prints the outputs
puts File.read("test.txt")


#now how about reading from the console?
puts "What is your name?"
#now to get the user input
name=gets
puts "Hello #{name}"

#HTTP Requests

#now into something I haven't done yet! There are times were rather than working 
#with local files, website/remote API info may also need to be worked with.

#Ruby comes with a built in HTTP client
require 'net/http'
http_response = Net::HTP.get_response('www.example.com', '/')

#how to see the progress, you can print the code
puts http_response.code
#here it should provide the value 200. This means its successful!


#Now onto parsing Http response

puts http_response.body

#this response wouldn't make any human sense...so theres ore that needs to occur!

require ' net/http'
require 'uri'
require 'json'

uri = URL('http://www.example.com/sample.json')
response = Net::HTTP.get(uri)
json_response = JSON(response)

#note that uri stands for:Uniform resource Identifiers

#Receiving HTTP requests
#in order to begin doing this, you have to be able to listen for requests
# on the network port. (53...?)

# there are various ways to rwite a http server through the ruby toolbox, but for
#the example, WEBrick is used.

require 'webrick'

#now to specify the port to listen to HTTP requests
http_server = WEBrick:HTTPServer.new(:Port => 3000)

#how this server has to inherty some functionalities
class MyHTTPServlet < WEBrick::HTTPServlet::AbstractServlet
	#this will output the requested path
	def do_GET(http_request, http_response)
		http_response.body = "You requested ' #{http_request.path}'"
	end
end

http_server.mount {'', MyHTTPServlet}
#now to stop th eserver use control C with the followig command
trap ('INT') {http_server.shutdown}
http_server.start

#with the server running you can make some requests:
curl localhost:3000
#this requests '/'
