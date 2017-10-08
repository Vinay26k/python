from bs4 import BeautifulSoup as bs
import requests
import os
'''
check = ''
if os.path.isfile('Trainslog.txt'):
    check = open('Trainslog.txt','r').read()
l = open('Trainslog.txt','a+')
i = 0
'''
f = open('cprogLinks.txt','w+')
links = []

def link():
    url = r'https://www.indiabix.com/c-programming/questions-and-answers/'
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
subPage(link())
f.close()
#EpageMax(link())

'''
f = open('Trains.txt','a+')
for i in range(38001,38007):
    if str(i) not in check:
        core(i,f)
        l.write(str(i)+'\n')
core(39001,f)
core(40001,f)
core(41001,f)
#for i in range(39001,6015):
#    if str(i) not in check:
#        core(i,f)
#        l.write(str(i)+'\n')
f.close()
l.close()
#os.remove('Trainslog.txt')
'''
