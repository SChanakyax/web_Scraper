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
#print(len(containers))  #no of products on the web page

#print(soup.prettify(containers[0]))

container = containers[0]
#print(container.div.img["alt"])

#price = container.findAll("div", {"class":"s-item__detail s-item__detail--primary"})
#print(price[0].text)

#rating = container.find_all('span', {'class': 's-item__reviews-count'})
#print(rating[0].text)
#for span in rating:
   # print(span.text.replace('shipping', '').strip())

#shipping = container.find_all('span', {'class': 's-item__shipping s-item__logisticsCost'})
#print(shipping[0].text)
#for span in shipping:
   # print(span.text.replace('shipping', '').strip())

filename = "ebay.csv"
f = open(filename, "w")

headers = "ProductName,Price,Shipping\n"
f.write(headers)

for container in containers:
    productname = container.div.img["alt"]

    pricecontainer = container.findAll("div", {"class":"s-item__detail s-item__detail--primary"})
    price = pricecontainer[0].text.strip()

    #ratingcontainer = container.find_all('span', {'class': 's-item__reviews-count'})
   # rating = ratingcontainer[0].text

    shippingcontainer =  container.find_all('span', {'class': 's-item__shipping s-item__logisticsCost'})
    shipping = shippingcontainer[0].text.replace('shipping', '').strip()

    #print(productname + "," + price + "," + shipping + "\n")
    #print(soup.prettify().encode('cp1252', errors='ignore'))
    f.write(productname.replace(",", "|") + "," + price + "," + shipping + "\n")

f.close()


'''
    print("productName: " + productname)
    print("price: " + price)
    print("shipping: " + shipping + "\n\n")
   # print("rating; " + rating)
'''
'''
ERROR::
Traceback (most recent call last):
  File "C:/Users/SC/Documents/PythonProj/WebScrapper_1/main.py", line 52, in <module>
    f.write(productname.replace(",", "|") + "," + price + "," + shipping + "\n")
  File "C:\Program Files\Python38\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u2705' in position 0: character maps to <undefined>

'''
'''
Solution : 
The error is caused by the print call. Somewhere in you text, you have a ZERO WIDTH SPACE character (Unicode U+200B), and if you print to a Windows console, the string is internally encoded into the Windows console code page (cp1252 here). And the ZERO WIDTH SPACE is not represented in that code page. BTW the default console is not really unicode friendly in Windows.

There is little to do in a Windows console. I would advise you to try one of these workarounds:

do not print to the console but write to a (utf8) file. You will then be able to read it with a utf8 enabled text editor like notepad++

manually encode anything before printing it, with errors='ignore' or errors='replace'. That way, possibly offending characters will be ignored and no error will arise

  print(soup.prettify().encode('cp1252', errors='ignore'))
'''