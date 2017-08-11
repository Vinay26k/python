from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

path = r'C:\Users\lenovo\Documents\Vinay Python\github\selenium drivers\chromedriver.exe'
driver = webdriver.Chrome(path)

#change these 
user = 'username'
pswd ='password'

taurl = r'https://10fastfingers.com/account/twitter_login'
driver.get(taurl)
sf = driver.find_element_by_id('username_or_email')
sf.send_keys(user)
sf = driver.find_element_by_id('password')
sf.send_keys(pswd)
sf = driver.find_element_by_id('allow')
sf.click()

url = r'https://10fastfingers.com/typing-test/english'
#url = r'https://10fastfingers.com/multiplayer/alpha'
driver.get(url)


soup = BeautifulSoup(driver.page_source,'html.parser')
count = 0
for x in soup.find_all('div',attrs={'id':'row1'}):
    sf = driver.find_element_by_id('inputfield')
    sf.send_keys(x.get_text())
    if count == 20:
        sleep(1)
        count = 0
    count += 1
    
