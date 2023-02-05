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

# extract urls of each product
# # list_of_links = soup.find_all("div", class_= "image") 
tags = soup.find_all("a")
valid_urls = []
for i in tags:
    link = i.get("href")
    url = re.search("^https://labarrica.com/shop/.+/$",link)
    if url:
        valid_urls.append(url.group())
    
def scrape(url,tag,specifier):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    html = soup.find_all(tag,specifier)
    return html

products_html = []
for i in valid_urls:
    result = scrape(i,"div","summary entry-summary")
    products_html.append(result)
    
for i in range(5):
    print(products_html[i])
    
# name, sku, stock, category, 
        



# filtered_urls = []
# for i in list_links:
#     if shop_url in i:
#         filtered_urls.append(i)

# print(filtered_urls)

        
        
    
    
    
## declare the dictionary to store urls from products 

# urls_to_visit = [] 















#------------------------------------------------------------------------------------------
# vinos = []
# licores = []
# canastas_y_otros = []
# deli = []
# # full list of products 
# complete_list = vinos + licores + canastas_y_otros + deli
# # json list and/or csv
# json_list = json.dumps(complete_list, indent=2)
