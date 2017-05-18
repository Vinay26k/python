'http://www.mpgh.net/forum/showthread.php?t=659694'
from bs4 import BeautifulSoup
import requests

url = raw_input("Enter a website to extract the URL's from: ")
#r  = requests.get("http://" +url)
r  = requests.get(url)
data = r.text
#print(data)
soup = BeautifulSoup(data,"html.parser")
#for link in soup.find_all('a'):
#    print(link.get('href'))

#print(soup.get_text())
for script in soup(['script','style']): #deletes javascript and style scripts
    script.extract()
data = soup.get_text()

with open("ab.txt",'w') as f:
    f.write(data.encode('utf-8'))
print "DONE!"
