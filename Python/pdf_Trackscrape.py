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
