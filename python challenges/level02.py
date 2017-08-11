
'Hint: Page Source'
#https://github.com/Vinay26k/pythonchallenge
import requests

url = r'http://www.pythonchallenge.com/pc/def/ocr.html'
r = requests.get(url).text

import re
find = re.findall("<!--(.*?)-->", r, re.DOTALL)[-1]
print("".join(re.findall("[A-Za-z]", find)))
