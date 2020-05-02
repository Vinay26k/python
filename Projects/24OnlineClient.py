from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time,sys

def cred():
    cr = '''
        https://github.com/Vinay26k/
        All copyrights related this software belongs to Vinay :)
        Mail me at: vinay@programmer.net

Note :
1. Allow access to phantomjs and 24OnlineClient application
2. Don't close this command window, coz that's a ghost :o
3. If closed, give life to that ghost :/ run application again
4. Time interval set to 5 seconds :)
5. Mail me for 1 minute optimized application ;)

usage :
1. Enter username and password
2. If it prompts for credentials again, you've entered wrong details
3. Open readme.txt for more details

'''

    print cr
cred()
path=r'./phantomjs.exe'
url = r'https://internet.lpu.in/24online/webpages/client.jsp'
driver=webdriver.Chrome()
#driver = webdriver.PhantomJS()
driver.set_window_size(1366, 768)
def ent():
    print 'Enter username and password :'
    user = str(raw_input('Username: '))
    pswd = str(raw_input('password: '))
    return user,pswd
print "\n=>", url
def check(soup):
    for x in soup.find_all('form'):
        for y in x.find_all('input', attrs={'type':'text'}):
            flag = len(y.attrs)
            return flag

def login():
    driver.get(url)
    try:
        driver.switch_to_frame(1)
    except:
        print 'Reconnect wifi and run application'
        sys.exit()
    soup = bs(driver.page_source,'html.parser')
    if check(soup)== 2:
        user,pswd = ent()
        print "xXx Logging In! xXx"
        sf = driver.find_element_by_name('username')
        sf.send_keys(user)
        sf = driver.find_element_by_name('password')
        sf.send_keys(pswd)
        sf = driver.find_element_by_xpath(r'//*[@id="jsena"]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[5]/td/button').click()
        time.sleep(2)
        soup = bs(driver.page_source,'html.parser')
        if check(soup)==2:
            print 'wrong password, run application again'
            login()
    else:
        timestamp = time.strftime('%H:%M:%S')
        print '{0} xXx Already logged in refreshing page xXx'.format(timestamp)
        driver.refresh()
        time.sleep(5)
    print '\tClose application manually, if want to exit\n'

while True:
    login()
