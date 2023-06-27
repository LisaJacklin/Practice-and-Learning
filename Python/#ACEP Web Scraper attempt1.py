#ACEP Web Scraper attempt1

#note that i'm having difficulty with getting the website to scrape off of wayback...

from bs4 import BeautifulSoup as bs
import requests
import urllib

#this webpae is the wayback ACEP webpage
url = ‘https://web.archive.org/web/20210728131026/https://acep.uaf.edu/publications/resource-overview.aspx'
response = requests.get(url)

#this will take the html link apart and separate them into different classes
soup = bs(response.text,’html.parser’)

a=soup.findAll(‘a’,{‘class’:’pdf’})
for element in a:
 print(l)
 name = element[‘href’].split(‘/’)[4]
 link = element[‘href’]
 directory = ‘address/to/directory’
 
 print(‘saving : ‘,name)
 pdfFile = urllib.request.urlopen(link)
 file = open(directory+name, ‘wb’)
 file.write(pdfFile.read())
 file.close()
grid_box = soup.findAll('div',{'class':'grid-box'})
for i in range(1,len(grid_box)):
    # stripping topic heading name from the grid-box   
    dirname = grid_box[i].h2.text.strip()
    print('creating folder for : ',dirname)
    
    # Creating a directory with same name as topic heading (replacing
    #spaces with underscore as spaces can create problem in creating folder)   
    #ADJUST THIS SO IT SAVES SOMEWHERE I CAN ACCESS

    dirname = 'address/to/directory'+dirname.replace(' ','_')
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
links = (grid_box[i].findAll('a'))
    for f in links:
        html_link = (f['href'])
        html_name = f.text.replace(' ','_').strip()
        html_res = requests.get(html_link)
        
    # creating files with same name as name in html link 
        filename =  dirname+'/'+html_name+'.pdf'
        
        if not os.path.isfile(filename):
            pdf = pdfkit.from_url(html_link,filename)
            print('created_file : '+dirname+'/'+html_name+'.pdf'+' successfully')