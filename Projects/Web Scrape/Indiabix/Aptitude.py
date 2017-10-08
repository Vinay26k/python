from bs4 import BeautifulSoup as bs
import requests
import os

f = open('AptiLinks.txt','w+')
links = []

def cred():
    print '''
        https://github.com/Vinay26k/
        All copyrights related this software belongs to Vinay :)
        Mail : vinay@programmer.net
        Contact : +91-9872375950
'''
def link():
    url = r'https://www.indiabix.com/aptitude/questions-and-answers/'
    r = requests.get(url).text
    soup = bs(r,'html.parser')
    for x in soup.find_all('div',attrs={'class':'div-topics-index'}):
        for y in x.find_all('a'):
            links.append('https://www.indiabix.com'+y['href'])
            print links[-1]
    return links

singlePage = []
subPages = []
def EpageMax(url):
    r = requests.get(url).text
    soup = bs(r,'html.parser')
    for x in soup.find_all('p',attrs={'class':'mx-pager mx-lpad-25'}):
        for y in x.find_all('a'):
            if 'Next' not in y.get_text():
                singlePage.append('https://www.indiabix.com'+y['href'])
                print singlePage[-1]+' ',
                f.write(singlePage[-1]+'\n')
                print y.get_text()


def subPage(links):
    for url in links:
        print url
        r = requests.get(url).text
        soup = bs(r,'html.parser')
        f.write(url+'\n')
        EpageMax(url)
        for x in soup.find_all('ul',attrs={'class':'ul-top-left'}):
            for y in x.find_all('a'):
                subPages.append('https://www.indiabix.com'+y['href'])
                print subPages[-1]+' ',
                print y.get_text()
                f.write(subPages[-1]+'\n')
                EpageMax(subPages[-1])

  

#link()
cred()
subPage(link())
f.close()
#EpageMax(link())
