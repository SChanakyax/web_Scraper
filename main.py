import spans as spans
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as urlReq
#https://www.youtube.com/watch?v=mKxFfjNyj3c
urlx = 'https://www.ebay.com/b/iPhone-X-Phones/9355/bn_86757102?rt=nc&_dmd=1'

urlClient = urlReq(urlx)
html = urlClient.read()
urlClient.close()
page_soup = soup(html, "html.parser")

containers = page_soup.findAll("div", {"class": "s-item__wrapper clearfix"})
print(len(containers))  #no of products on the web page

#print(soup.prettify(containers[0]))

container = containers[0]
print(container.div.img["alt"])

price = container.findAll("div", {"class":"s-item__detail s-item__detail--primary"})
print(price[0].text)

rating = container.find_all('span', {'class': 's-item__reviews-count'})
print(rating[0].text)
#for span in rating:
   # print(span.text.replace('shipping', '').strip())

shipping = container.find_all('span', {'class': 's-item__shipping s-item__logisticsCost'})
print(shipping[0].text)
for span in shipping:
    print(span.text.replace('shipping', '').strip())

