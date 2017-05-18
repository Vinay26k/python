import requests
from bs4 import BeautifulSoup
import xmltodict
import time

date = time.strftime("%B %d %Y")
ls =[]
det = {}
tScore = {}
url = 'http://synd.cricbuzz.com/j2me/1.0/livematches.xml'
r = requests.get(url)
data = r.text
doc = xmltodict.parse(data)
soup = BeautifulSoup(data,'html.parser')
matches = soup.find_all(['match','Tme'])
#directScore = {}
def matchDetails():

    for i in range(len(doc['mchdata']['match'])):
        if doc['mchdata']['match'][i]['Tme']['@Dt']== date and doc['mchdata']['match'][i]['state']['@mchState']=='inprogress':
            #print doc['mchdata']['match'][i]['@id']
            matchId = doc['mchdata']['match'][i]['@id'].encode('utf-8')
            desc = doc['mchdata']['match'][i]['@mchDesc'].encode('utf-8')
            #a,x,b = desc.split(' ')
            score = scoreDetails(i)
            print matchId
            try:
                f,s = score[0],score[1]
            except:
                f,s = 0,0
            #ls.append(matchId)
            if f != 0 and s != 0:
                #ls.append(desc)
                #ls.append(f)
                #ls.append(s)
                #print score
                tScore[score[2]] = f
                tScore[score[3]] = s
                det[matchId] = tScore
    return tScore

def scoreDetails(matchNum):
    result = []
    try:
        FirstScore = doc['mchdata']['match'][matchNum]['mscr']['blgTm']['Inngs']['@r'].encode('utf-8')
        Fname = doc['mchdata']['match'][matchNum]['mscr']['blgTm']['@sName'].encode('utf-8')
        Sname = doc['mchdata']['match'][matchNum]['mscr']['btTm']['@sName'].encode('utf-8')
        SecondScore = doc['mchdata']['match'][matchNum]['mscr']['btTm']['Inngs']['@r'].encode('utf-8')
        result.append(FirstScore)
        result.append(SecondScore)
        result.append(Fname)
        result.append(Sname)
       # print result
        return result
    except KeyError:
        return
'''   
url = 'http://synd.cricbuzz.com/j2me/1.0/livematches.xml'
r = requests.get(url)
data = r.text
doc = xmltodict.parse(data)
soup = BeautifulSoup(data,'html.parser')
matches = soup.find_all(['match','Tme'])

#print [ match['id'] for match in matches if match['Dt']=='May 03 2017']
#print soup.find_all('match')
#s = soup.find_all('Tme')
#if doc['mchdata']['match'][i]['Tme']['@Dt']== u'May 03 2017'
 #May 04 2017 format
#date = 'May 03 2017'
#print date 
#TotalMatches = [doc['mchdata']['match'][i]['Tme']['@Dt'] for i in range(len(doc['mchdata']['match'])) if doc['mchdata']['match'][i]['Tme']['@Dt']== date]
#MatchIds = [doc['mchdata']['match']['@id'] for i in range(len(doc)) if doc['mchdata']['match'][i]['Tme']['@Dt']== date]
#if not TotalMatches:
#    print "No Current Running match today"
#else:
#    print MatchIds
#print [match['Dt'] for match in soup.match]
#if match['Dt']=='May 03 2017']
matchDetails(doc)
print [det[i] for i in det]
print tScore
'''
