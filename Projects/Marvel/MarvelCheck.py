import requests,json
url = r'https://gateway.marvel.com/v1/public/comics?ts=1&apikey=2014db5ba5d67d85c1aa4dc66f380b2b&hash=04820767aca21ae662f712f25a9a871b'
r= requests.get(url)
print r.status_code
r = json.loads(r.text)
#print r['data']['results'][1]
for x in r['data']['results']:
    #print x['series']['name']
    print x
    print '***************************************************'
