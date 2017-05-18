import glob
import os
import re
path = r'D:\VinayHere'
words= ['keywords','to','find','in','list','of','files']
val = []
q = open('Getinfo.txt','w')
for filename in glob.glob(os.path.join(path, '*.txt')):
    f = open(filename,'r')
    d = f.read().split('\n')
    for i in d:
        t,r = i.split(" ")[0],i.split(" ")[1:]
        r = ''.join(r)
        for j in words:
            if j in r:
                print t,r
                #if t not in val and int(t)>1000: #you dont need this in your work
                #    val.append(t)
                q.write(t+" "+r+"\n")
                
    f.close()
q.close()
print val
