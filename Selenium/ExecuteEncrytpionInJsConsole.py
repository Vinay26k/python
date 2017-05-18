from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
path = 'C:\Users\lenovo\Documents\Vinay Python\python2\Mechanize and BeautifulSoup\phantomjs.exe'
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    

capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = { 'browser':'ALL' }
url = r'https://www.abcdefg.com/' #any url that's having AES encryption
driver = webdriver.PhantomJS(path,desired_capabilities=capabilities)
#driver = webdriver.Chrome(desired_capabilities=capabilities)
EncId = []
f = open('EncId.txt','w')
rId= []
def loop():
    for i in range(2,200):
        print i
        a = '''
var dataToEnc = %d;
var key = CryptoJS.enc.Utf8.parse('8080808080808080');
var iv = CryptoJS.enc.Utf8.parse('8080808080808080');
var encrypted = CryptoJS.AES.encrypt(CryptoJS.enc.Utf8.parse(dataToEnc), key,{ keySize: 128 / 8, iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 });
encrypted =encrypted.toString();
console.log(encrypted);
'''%(int(i))
        driver.get(url)
        key = funct(a)
        #rId.append(a)
        f.write(str(i) + " "+ key+"\n")
        print "Done!"
        #return rId
def init():
    #d = [3250]
    #loop(d)
    loop()
    #driver.get(url)
def funct(a):
    sf = driver.execute_script(a)
    for entry in driver.get_log('browser'):
        print entry['message'].split(' ')[0]
        EncId.append(entry['message'].split(' ')[0])
    sleep(5)
    return entry['message'].split(' ')[0]
def exitin():
    #print EncId
    driver.quit()
init()
#loop()
#exitin()
