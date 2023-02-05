from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import re

pages = ["https://labarrica.com/vinos/", 
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
    
## function scrape declared to use to scrape each product info return 
def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # html = soup.find(tag,specifier)
    sku = soup.find("span", class_="sku") # <span class="sku_wrapper">SKU: <span class="sku">190904</span></span>
    name = soup.find("h1", class_="product_title") # None # <h1 class="product_title entry-title">Gin Bombay Sapphire 1000ml</h1>
    category = soup.find("a", attrs="taglabarrica.com/category")#None # <span class="posted_in">Categorías: <a href="https://labarrica.com/category/licores/gin/" rel="taglabarrica.com/category/licores/" rel="tag">Licores</a>, <a href="https://labarrica.com/category/li rel="tag">Más Vendidos</a></span>
    price = soup.find("span", class_="woocomer-Price")#None # 
    stock = soup.find("p", class_="stock") #None # <p class="stock in-stock |stock out-of-stock">Hay existencias</p>
    product = {"sku": sku, "name" : name, "category" : category, "price": price,"stock" : stock}
    return product

#list to store all products as dictionaries
complete_list = []
for i in valid_urls:
    product = scrape(i)
    complete_list.append(product)
    
print(complete_list)
    

# list to store products as html
# products_html = []
# # loop to iterate over the urls and append the product as html 
# for i in range(1):
#     result = scrape(valid_urls[i],"div","summary entry-summary") ## --------------------------------------------
#     products_html.append(result)
    

# # loop to get details for each product as a dictionary
# for i in range(1):
#     print(products_html)
    # soup = BeautifulSoup(products_html[i], "html.parser")
    # ## parent <div class="summary entry-summary">
    # complete_list.append(product)
# # json list


# json_list = json.dumps(complete_list, indent=2)

# csv list 

#------------------------------------------------------------------------------------------
# vinos = []
# licores = []
# canastas_y_otros = []
# deli = []
# # full list of products 
# complete_list = vinos + licores + canastas_y_otros + deli
# # json list and/or csv
# json_list = json.dumps(complete_list, indent=2)
