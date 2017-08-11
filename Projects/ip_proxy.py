import requests,json
url = r'http://gimmeproxy.com/api/getProxy?country=US'
q = open('proxylist.txt','r')
d = q.read().split('\n')
q.close()
f = open('proxylist.txt','a+')
for x in range(500):
    r = json.loads(requests.get(url).text)
    st =  r['ipPort']
    print x+1,st
    if st not in d:
        f.write(st+'\n')
f.close()
    
