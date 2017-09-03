from urllib2 import urlopen
from contextlib import closing
import json

def iplocate(ipaddress):
    #url = 'http://ip-api.com/json/208.80.152.201'
    url = 'http://ip-api.com/json/'+str(ipaddress)
    try:
        with closing(urlopen(url)) as response:
            location = json.loads(response.read())
           # print(location)
            location_city = location['city'].encode('utf-8')
            location_cc = location['countryCode'].encode('utf-8')
            location_isp = location['isp'].encode('utf-8')
            location_state = location['regionName'].encode('utf-8')
            location_country = location['country'].encode('utf-8')
            location_lat=location['lat']
            location_lon = location['lon']
            location_timezone= location['timezone'].encode('utf-8')
            location_zip = location['zip'].encode('utf-8')
            #st =r'''city: {0}
#state: {1}
#country: {2}
#latitude: {3}
#longitute: {4}
#zip: {5}
#timezone: {6}
#'''.format(location_city,location_state,location_country,location_lat,location_lon,location_zip,location_timezone)
  
            
            #print(st)
            print(location_city+" "+location_state+" "+location_cc+" "+location_country+" "+location_zip+" "+location_timezone+" "+location_isp)
    except:
        print("Location could not be determined automatically")


#iplocate('108.61.123.162')
