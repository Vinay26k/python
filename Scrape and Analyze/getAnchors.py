from bs4 import BeautifulSoup
import requests

url = raw_input("Enter a website to extract the URL's from: ")
#r  = requests.get("http://" +url)
r  = requests.get(url)
data = r.text
print(data)
soup = BeautifulSoup(data,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

#print(soup.get_text())
    
