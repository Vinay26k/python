#! python 3
#https://github.com/Vinay26k/pythonchallenge

url = r'http://www.pythonchallenge.com/pc/def/map.html'
'''
Given
k->m
o->q
e->g

everybody thinks twice before solving this.

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

'''

st = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''

a = [chr(x) for x in range(97,123)]
ar = a[2:]
ar.append(a[0])
ar.append(a[1])
a = ''.join(a)
ar = ''.join(ar)
#print a,ar
print(st.translate(str.maketrans(a,ar)))

st = str(input())
print(st.translate(str.maketrans(a,ar)))
