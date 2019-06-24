from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myurl="https://www.w3schools.com/xml/simple.xml"

uClient=uReq(myurl)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")

name=page_soup.findAll("name")
price=page_soup.findAll("price")
for i in range (0,len(name)):
    print(name[i].text,end="")
    print(price[i].text)