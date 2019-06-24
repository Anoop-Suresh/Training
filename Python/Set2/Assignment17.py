from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myurl="http://example.webscraping.com"
uClient=uReq(myurl)
page_html=uClient.read()
uClient.close()

page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll('td')

for i in range (0,len(containers)):
    print(containers[i].a.text)
    print(containers[i].img)

