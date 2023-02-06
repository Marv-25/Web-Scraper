from bs4 import BeautifulSoup
import requests
import json
import re

pages = ["https://labarrica.com/","https://labarrica.com/vinos/", 
         "https://labarrica.com/licores/"]
page = None
# provide url and basics
for i in pages:
    url = i
    page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# extract urls of each product by tag a and using attribut href,  using shop slug, appending valid urls of products to valid_urls list
tags = soup.find_all("a")
valid_urls = []
for i in tags:
    link = i.get("href")
    url = re.search("^https://labarrica.com/shop/.+/$",link)
    if url:
        valid_urls.append(url.group())
valid_urls = list(set(valid_urls))
## function scrape declared to use to scrape each product info return 
def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # html = soup.find(tag,specifier)
    sku = soup.find("span", class_="sku").text # <span class="sku_wrapper">SKU: <span class="sku">190904</span></span>
    name = soup.find("h1", class_="product_title").text # None # <h1 class="product_title entry-title">Gin Bombay Sapphire 1000ml</h1>
    category = soup.find("span", class_="posted_in").text.split()#None # <span class="posted_in">Categorías: <a href="https://labarrica.com/category/licores/gin/" rel="taglabarrica.com/category/licores/" rel="tag">Licores</a>, <a href="https://labarrica.com/category/li rel="tag">Más Vendidos</a></span>
    category = category[1].replace(",","")
    price = soup.find("span", class_="woocommerce-Price-amount amount").text#None #
    stock = soup.find("p", class_= ["stock in-stock", "stock out-of-stock"]).text  #None # <p class="stock in-stock |stock out-of-stock">Hay existencias</p>
    product = {"Sku": sku, "Name" : name, "Category" : category, "Price": price,"Stock" : stock}
    return product

#list to store all products as dictionaries
complete_list = []
for i in valid_urls:
    try: 
        product = scrape(i)
    except:
        pass
    else:
        complete_list.append(product)


# # json list and/or
json_list = json.dumps(complete_list, indent=2)
print(json_list)