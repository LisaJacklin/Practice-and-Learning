##############################################################################
PROJECT: ZOTERO ACEP OLD CITE WEB SCRAPER
ALASKA CENTER FOR ENERGY AND POWER


AUTHOR:LISA JACKLIN
LANGUAGE: PYTHON

OBJECTIVE: 

##############################################################################

#NOTE THAT MUCH OF THESE ARE DONE AND PERFORMED WITHIN THE PYTHON IDE

from urllib.request import urlopen #this allows you to open and import data from a url

url = "insert url here"

page = urlopen(url)

page #run the open url so you can now parse the information required

html_bytes = page.read()

html = hyml_bytes.decode("utf-8")

print(html) #this will display the contents of the pages.


##############################################################################
# EXTRACTING TEXT FROM HTML WITH STRING METHOD

#this will allow withdraw of the title within the html to be searched using .find()
title_index = html.find ("<title>") 
title_index

#since we don't want the index of each tag, and we are trying to find the index of "title" we must justify this 
start_index = title_index + len("<title>")
start_index

#to end the search for the title of the html, which is searching for the html end sign
end_index = html.find("</title>")
end_index

#this means that the title will only go from the beginning to end based on the index we have created
title = html[start_index:end_index]
title

##############################################################################
# REGULAR EXPRESSIONS

#re module which allow regular expressions module to be pulled
import re

#this will show all text with a string that matches the expressions
#here expressions 1 is the regular expression to match
#expression 2 is the string to test...
re.findall (".1.", ".2.")

#note this is all case sensitive upless additional is added
re.findall(".1.", ".2.", re.IGNORECASE)

"
in this format,  "a.c" the period means a signle character in a regular expressions
while in "ab*c" the string must start with a, end with c, and have zero or more instances of b

.  single character
* start, and end with other characters after start for any instance of it
.* any character repeated any number of times

"

##############################################################################
# EXTRACT TEXT FROM HTML WITH REGULAR EXPRESSIONS


##############################################################################
# HTML PARSER FOR WEB SCRAPING IN PY


