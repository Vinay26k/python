# -*- coding: cp1252 -*-
import requests
from bs4 import BeautifulSoup
from time import sleep
import pdfkit
import os.path

url = r'https://automatetheboringstuff.com'
path=r'./wkhtmltopdf.exe'
extrapath = r"C:\Users\lenovo\Documents\Vinay Python\github\Automate with python/"
config = pdfkit.configuration(wkhtmltopdf=path)
f = open('chapters.txt','r')
data = f.read().split('\n')
c = 1
print 'Local Status\t\t','Server status\t','Final Status\t','File'
for i in data[1:-1]: #ignore chap 0
    url = r'https://automatetheboringstuff.com'
    j = i.split('[->]')
    if 'https' not in j[-1].strip():
        url = url+j[-1].strip()
    f = str(c)+'.'+j[0].split('–')[-1].strip()+'.pdf'
    if not os.path.isfile(f):
        r = requests.get(url)
        print 'File not found\t\t',r.status_code,'\t\t',
        pdf = pdfkit.from_url(url,f, configuration=config)
    #sleep(5)
    else:
        print 'File found\t\t','200\t\t',
    c += 1
    print 'Done\t\t',f

sleep(100000)
