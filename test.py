import re
urls = []
url = "https://labarrica.com/shop/espumante-sin-alcohol-eva-sabor-melocoton-750ml/"
x = re.search(r"^https://labarrica.com/shop/.*/", url).group()
print(x)