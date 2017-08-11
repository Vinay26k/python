
'Hint: Page Source'
#https://github.com/Vinay26k/pythonchallenge
import requests

url = r'http://www.pythonchallenge.com/pc/def/equality.html'
r = requests.get(url).text

import re
print(''.join((re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+",r))))
