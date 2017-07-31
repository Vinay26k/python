import requests
from bs4 import BeautifulSoup as bs
#purl = r'http://www.sanfoundry.com/1000-database-management-system-questions-answers/'
purl = ''
url = []
def getUrl(purl):
    r = bs(requests.get(purl).text,'html.parser')
    for x in r.find_all('div',attrs={'class':'entry-summary'}):
        for y in x.find_all('a'):
            url.append(y['href'])
    return url
    
#url = r'http://www.sanfoundry.com/database-mcqs-sql-basics-definitions/'
data = None
f = None

def getQandA(url,f):
    c = 0
    for i in url:
        print 'Processing ',i
        f.write('xXx \t{} xXx\n\n'.format(i))
        r = bs(requests.get(i).text,'html.parser')
        for x in r.find_all('div',attrs={'class':'entry-content'}):
            data = ''.join(x.get_text().strip().replace('View Answer','\n'))
            data = data.replace(' Answer:','Answer : ')
        for x in data.split('\n')[2:-5]:
            print x
            f.write(x.encode('utf-8')+'\n')
        f.write('\n')



print '''
        https://github.com/Vinay26k/
        All copyrights related this software belongs to Vinay :)
        Mail : vinay@programmer.net
        Contact : +91-9872375950

usage : Enter sanfoundry website url
example :
    http://www.sanfoundry.com/1000-database-management-system-questions-answers/

'''

purl = str(raw_input('Enter url : '))
url = getUrl(purl)
f = open(purl.split('/')[-2]+'.txt','w+')
print 'Gathered URLS :)'
getQandA(url,f)
f.close()

#download link: https://www.dropbox.com/s/mqmsixd7zzmfw6p/SanfoundryGetQandA.exe?dl=0
