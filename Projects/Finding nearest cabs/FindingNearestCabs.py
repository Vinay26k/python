import json
from math import acos, sin, cos

location_data = open("locations.json","r").read().split("\n")
#print(location_data)

##All math constants goes here
PI = 3.14159265358979323846
Earth_Radius = 6371.0
#Random location of me
lat = 12.9611159
long = 77.6362214

each_loc_data = []
each_user_data = []

'''
φ1,φ2 - latitudes
Δλ - delta longitude
Law of cosines:	d = acos( sin φ1 * sin φ2 + cos φ1 * cos φ2 * cos Δλ ) * Earth_Radius
'''


def degToRad(deg):
    #we have location data in degrees so converting to radians
    return ((deg * PI) / 180)


def getDistanceFromPoint(each_loc_data):
    #Suppose two points A(x1,y1), B(x2,y2)
    x1 = degToRad(lat) #x1 - my latitude
    x1 = degToRad(41.49008)
    y1 = degToRad(long) #y1 - my longitude
    y1 = degToRad(-71.312796)
    
    x2 = degToRad(float(each_loc_data[0])) #x2 - cab latitude
    y2 = degToRad(float(each_loc_data[1])) #y2 - cab longitude


    delta_lon = y2 - y1 #cab long minus my long

    central_angle = acos( sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(delta_lon))

    return (Earth_Radius * central_angle)

output = []

l1 = [41.49008, -71.312796] 
l2 = [41.499498, -81.695391]


import argparse as ap
parser = ap.ArgumentParser()
parser.add_argument('l1',type=float)
parser.add_argument('l2',type=float)
args = parser.parse_args()
print(args) 
print(getDistanceFromPoint(l2))

'''
for data in location_data[:-1]: #skip last one and iterate all
    #print(json.loads(data))
    formatted_data = json.loads(data)
    each_loc_data = [formatted_data['latitude'], formatted_data['longitude']]
    each_user_data = [formatted_data['user_id'], formatted_data['name']]
    #print(each_loc_data, each_user_data)
    foundDistance = getDistanceFromPoint(each_loc_data)
    print(foundDistance, each_user_data)


    
    if(foundDistance <= 50.0000):
        output.append([each_user_data, foundDistance])


for data in sorted(output,key= lambda x:x[1]):
    print(data)
  '''  
