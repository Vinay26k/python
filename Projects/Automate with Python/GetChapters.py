import requests
from bs4 import BeautifulSoup

url = r'https://automatetheboringstuff.com'
r = requests.get(url).text
soup = BeautifulSoup(r,'html.parser')
f = open('chapters.txt','w')
#print soup
for x in soup.find_all('li'):
    for y in x.find_all('a'):
        a,b = y.get_text().encode('utf-8'),y['href'].encode('utf-8')
        print a,b
        f.write(a+' [->] '+b+'\n')
f.close()
