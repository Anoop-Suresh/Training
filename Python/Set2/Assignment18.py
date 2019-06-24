from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myurl="https://www.flipkart.com/search?q=iphone%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
uClient=uReq(myurl)
page_html=uClient.read()
uClient.close()

page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"_3O0U0u"})
price=page_soup.findAll("div",{"class":"col col-5-12 _2o7WAb"})
rate=page_soup.findAll("div",{"class":"hGSR34"})


# print(soup.prettify(containers[0]))
for i in range(0,len(containers)):
    print(containers[i].div.img["alt"])
    # print(price[0].text)
    print(rate[i].text)