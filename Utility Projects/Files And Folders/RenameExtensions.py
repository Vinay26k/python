'''
https://github.com/Vinay26k/
'''
import glob
import os

print("Enter the folder path: ")
path =str(raw_input())
data = None
def cw():
    print('''
        Creating FileList please do not delete this,
        we require it for changing files to original :)
''')
    f =open(path+r'\zzzzzfileList.txt','w+')
    for i in os.listdir(path):
        if os.path.isfile(path+'\\'+i):
            if i!='zzzzzfileList.txt':
                f.write(i+'\n')
    f.close()
def rw(data,val):
    f = open(path+r'zzzzzfileList.txt','w')
    index=0
    print('Changing file extensions Wait......')
    for i in os.listdir(path):
        if os.path.isfile(path+'\\'+i):
            a = i.split('.')[-1]
            b = i.split('.')[0:-1]
            #conversion
            if a!='xxf' and i.split('.')[0]!='zzzzzfileList':
                #print i.split('.')[0]
                #print '.'.join(b)
                os.rename(path+'\\'+i,path+'\\'+'.'.join(b)+'.xxf')
            #original
            elif i.split('.')[0]!='zzzzzfileList':
                #print val[index],
                #print '.'.join(b)
                os.rename(path+'\\'+i,path+'\\'+'.'.join(b)+'.'+val[index])
            index+=1
def ftype(data):
    val =[]
    for i in data.split('\n'):
        val.append(i.split('.')[-1])
    return val
def main():
    f = open(path+r'\zzzzzfileList.txt','r')
    data = f.read()
    f.close()
    if data!=None:
        #print "ok"
        rw(data,ftype(data))
        print ftype(data)
if 'zzzzzfileList.txt' in os.listdir(path):
    main()
else:
    ext = cw()
    main()
print("Work Done :)")
