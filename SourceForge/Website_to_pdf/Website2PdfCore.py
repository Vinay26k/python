import urllib.request as ul
from bs4 import BeautifulSoup as bs
from time import sleep
import pdfkit
import os.path
from datetime import datetime

url = None
def converter(url,direc=None):
    path = r'./wkhtmltopdf.exe'
    if not direc:
        direc = "./Website2Pdf"
    else:
        direc = direc + "/Website2Pdf"
    
    if not os.path.exists(direc):
        os.makedirs(direc)
    config = pdfkit.configuration(wkhtmltopdf = path)
    name = url.split('/')[-2]+".pdf"
    fname = direc+'/'+url.split('/')[-2]+".pdf"
    #print(fname)
    pdf = pdfkit.from_url(url,fname,configuration = config)
    #print("Done")
    return True,name
