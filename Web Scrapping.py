from bs4 import BeautifulSoup
import requests
url="https://livesql.oracle.com/next/"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
print(soup)
file=open("scrap.txt",'w+',encoding='utf-8')
file.write(soup.get_text())