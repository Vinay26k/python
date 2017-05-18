import requests
from bs4 import BeautifulSoup
import xmltodict
import time

date = time.strftime("%B %d %Y")
ls =[]
det = {}
tScore = {}
url = 'fdfdfdgfgh.com'
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
        returnore

