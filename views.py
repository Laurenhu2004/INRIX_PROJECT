from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request
import time


import requests
import json
import polyline
import numpy as np
import geopy.distance
from geopy.geocoders import nominatim
import itertools
import random
import operator
import requests
import json
import math

address = "501 Twin Peaks Blvd, San Francisco, CA 94114"
radius = "50"
preference = "closest"
# location = []
# r = []

views = Blueprint('views',__name__)

@views.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
 
    # get request body as text
    body = request.get_data(as_text=True)
    views.logger.info("Request body: " + body)

    return 'OK'

@views.route('/', methods = ["POST","GET"])
def index():
    global radius
    global address
    global preference
    global location
    global r
    global response
    if request.method == "POST":
        street = request.form["address"]
        city = request.form["city"]
        state = request.form["state"]
        zip = request.form["zip"]
        radius = request.form["radius"]
        address = street + ", " + city + ", " + state + " " + zip
        preference = request.form["preference"]
        return redirect(url_for('views.spots'))
    return render_template('index.html')

location_API = requests.get("https://geocode.maps.co/search?q={}".format(address))
info = location_API.text
parse_json = json.loads(info)
lati = parse_json[0]['lat']
long = parse_json[0]['lon']
location = [lati, long]

url = "https://api.iq.inrix.com/blocks/v3?point={}%7C{}&radius={}".format(lati,long,radius)

payload = {}
headers = {
'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IndtbGR5bmRzemMiLCJ0b2tlbiI6eyJpdiI6IjA1ZDgxNDg5MzVlN2FkZmEzMjFmZDlkODJmNjJhZmNlIiwiY29udGVudCI6ImQ1MmVmNDE1ZjQ0ZTFkMzczYmRhMjVmYjNjOGQ2ZjY4NWI2MWI1NmIwYzRlMTM0ODk1ZGM2OWE3OTI2OWY2N2Y2YWE0Y2E1ZmFiN2NiOTI4MGIwNGM0MzVhMTIxYjQ3OWFkMjcyNmI5OTQ2Y2U2OWY3OGYxMzg3ZmI5Y2NlZjE4M2M1ZjQ5YmUxZDUxZTdhYzM2YWIwZjU5MzcyMGU0YzNiODM4ZjE2Yzc5ZmQwNjY5NjIyZmI2YWFkZjZiYjQ0ZDg3NGVlNzIwZTM2ZTY1YTQ3NTljM2NjNjZmNTYxYzRlM2QyODgxYzJkNTI1ODBhYmMwNjU1MGI3OTcxMTk0MGJiZmZmMDdlMGI2NTAzOGUwMTEzZjA5ZGRhZTM1MDFiMDVjOGFhZGUyNzE1MjIwNjcwMjNkMzA4YzZhMjUwNzE3YThjZTE4YWU5OTU3MGQ5OWZkMDhkNjAwMGM0NjkzYTZmNzhhOTI5MmViZGY4NTQzNWMwMmVkMjQzNmUyZmNjMDNhNWIyYWM1Mzg1MmY2NWQyZWVlZDdlNjNlY2MzZjEyYmIyNDQ0Y2IwMDk2OTQ3ZWJkZTYwYWIxNjc4MzIxMTNiNTBhNDk1YTBmYjQxNWYxMTdlNDc5ZjE4YTM5ODc1N2FlMzM2NmRkMjU4YzQwZmMwY2IzOTAwMjlkNGUyYzdmODE2MDQyNzI4ZjdlYTJmYzE4ZTJkZjhjYzNlZWIwOWZjNmI0N2IzOTg1NTBiZTY4NWFlNjkxZTNlODk4ZTk0YTUzYTk5MGYzNzU1NmJlMmFlMTI1NDllM2FmZjM0YzUxYzI5MGIyOGVlY2IzOWM0MjEyYWUwZjBlZWFiODU0MWY0M2JjYzYxMzE2NjhjNzhiNWNiYzhjIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiIwNWQ4MTQ4OTM1ZTdhZGZhMzIxZmQ5ZDgyZjYyYWZjZSIsImNvbnRlbnQiOiJjNDM2Y2U0OWEyNGUzYTFiMTdmMjE5YzA1ZWEzMTUxYjUzM2RkMTYwMzY0NzEwMTliZGU5MTNkN2U4NzdlOTE1NDZhMGVkMGFmMDcwODIzODAyMGFkZDBiIn0sImp0aSI6IjhiZjE3MWNjLTcwNTYtNDQzZS1iMmNmLWFhOTE3Y2E4MTRlYSIsImlhdCI6MTY5OTgwNDAyMywiZXhwIjoxNjk5ODA3NjIzfQ.IMFwGsg-6kvqMwjX_VJCQT_tz-wMDNJinvVxttRkHSw'
}
response = requests.request("GET", url, headers=headers, data=payload)
r = (response.json()).get('result')
    
#names of streets
names = []
#probability of finding parking on a street
probability = []
#segment ids of segments that are open
segmentNames = []
polyLines = []
segmentDict = {}
probDict = {}
distanceAdressDict = {}
coordList = []
distances = []
costAdressDict = {}
bestStreetProb = 0
bestCost = 0
prices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def prob(adress, m):
    for p in range(len(list(probDict))):
        if(list(probDict)[p] in list(distanceAdressDict2)[m]):
            return list(probDict.values())[p]

def rating(d, c, n):
    distance = list(d.values())[n]
    cost = list(c.values())[n]
    park_prob = prob(list(d), n)
    safety = summ/151

    if(distance >= 0 and distance <= 29):
        distance_rating = 4
    elif(distance >= 30 and distance <= 149):
        distance_rating = 3
    elif(distance >= 150 and distance <= 300):
        distance_rating = 2
    else:
        distance_rating = 1
    
    if(cost >= 0 and cost <= 1):
        cost_rating = 4
    elif(cost >= 2 and cost <= 4):
        cost_rating = 3
    elif(cost >= 5 and cost <= 10):
        cost_rating = 2
    else:
        cost_rating = 1

    if(park_prob >= 0 and park_prob <= 9):
        prob_rating = 1
    elif(park_prob >= 10 and park_prob <= 39):
        prob_rating = 2
    elif(park_prob >= 40 and park_prob <= 89):
        prob_rating = 3
    else:
        prob_rating = 4

    if(safety >= 3):
        safety_factor = 1
    elif(safety >= 1.20):
        safety_factor = 2
    elif(safety > 0.3):
        safety_factor = 3
    elif(safety >= 0):
        safety_factor = 4 

    rating_num = int((distance_rating +  cost_rating +  prob_rating + safety_factor)/4)

    if(rating_num == 4):
        return "A"
    if(rating_num == 3):
        return "B"
    if(rating_num == 2):
        return "C"
    if(rating_num == 1):
        return "D"


#Getting name and probability of finding parking on given 
#street from coordinates and radius.

category1 = "Motor Vehicle Theft"
url0 = f"https://data.sfgov.org/resource/wg3w-h783.json?incident_category={category1}"

payload0 = {}
headers0 = {}

response0 = requests.request("GET", url0, headers=headers0, data=payload0)
response_text0=response0.text
response_list0 = json.loads(response_text0)
location_list = []

#for item in response_list1:
  #  print(item)
for itemlist in response_list0:
    itemdict = dict(itemlist)
    if "point" in itemdict.keys():
        coord = itemdict.get("point")
        location_list.append(coord.get("coordinates"))


parking_coord = [37.787362, -122.427540]
distance = math.dist(parking_coord,location_list[0])
truecoord = location_list[0]
for coord in location_list:
    coord = sorted(coord, reverse=True)
    x = math.dist(parking_coord,coord)
    if x < distance:
        distance = x
        truecoord = coord

truecoord = sorted(truecoord, reverse=False)


url1 = f"https://data.sfgov.org/resource/wg3w-h783.json?latitude={truecoord[1]}&longitude={truecoord[0]}&incident_category={category1}"

payload1 = {}
headers1 = {}

response1 = requests.request("GET", url1, headers=headers1, data=payload1)
response_text1=response1.text
response_list1 = json.loads(response_text1)
category2= "Larceny Theft"
url2 = f"https://data.sfgov.org/resource/wg3w-h783.json?latitude={truecoord[1]}&longitude={truecoord[0]}&incident_category={category2}"

payload2 = {}
headers2 = {}
response2 = requests.request("GET", url2, headers=headers2, data=payload2)
response_text2=response2.text
response_list2 = json.loads(response_text2)

summ= len(response_list1)+len(response_list2)

for i in range(0, len(r)):
    names.append(r[i].get('name'))
    probability.append(r[i].get('probability'))

    probDict[r[i].get('name')] = r[i].get('probability')

    #Deciding best street probability and best street to park on

    if(r[i].get('probability') > bestStreetProb):
        bestStreetProb = r[i].get('probability')
        bestStreet = r[i].get('name')

    segments = r[i].get('segments')

    #Creating segment dictionary with name of street, probability
    #of parking on the street, side of the street parking spot is on.

    for j in range(0, len(segments)):
        spaces = segments[j].get('spacesTotal')
        isOpen = segments[j].get('isOpen')

        if spaces >= 1 & isOpen == True:
            polyLines.append(segments[j].get('polyline'))
            segmentDict[segments[j].get('segmentID')] = [r[i].get('name'), r[i].get('probability'), segments[j].get('side'), segments[j].get('start'), segments[j].get('end')]

#Converting polyline data into coordinates, averaging coordinates,
#and adding all average coordinates into a list.

for k in range(0, len(polyLines)):
    np.a = polyline.decode(polyLines[k])
    averaged = np.average(np.a, axis=0)
    coordList.append(averaged)

#From coordinate list convert to adresses and sort based on distance away 
#from starting location.

for l in range(0, len(coordList)):
    a = requests.get("https://geocode.maps.co/reverse?lat={}&lon={}".format(coordList[l][0], coordList[l][1]))
    info1 = a.text
    p = ((json.loads(info1)).get('display_name')).replace(";" , "/")
    distanceAdressDict[p] = int(geopy.distance.geodesic(coordList[l], location).feet)
    costAdressDict[p] = random.choice(prices)
    distanceAdressDict1 = {k: v for k, v in sorted(distanceAdressDict.items(), key=lambda v: v[1])}
    costAdressDict1 = dict(sorted(costAdressDict.items(), key=operator.itemgetter(1)))


distanceAdressDict2 = dict(itertools.islice(distanceAdressDict1.items(), 5))    
costAdressDict2 = dict(itertools.islice(costAdressDict1.items(), 5))

#Printing out top 3 parking spots if distance was only concern.
names = []
details = []
grades = []

if preference == "closest":
    for o in range(0, 5):
        key = list(distanceAdressDict2)[o]
        value = list(distanceAdressDict2.values())[o]

        names.append("The #" + str((o + 1)) + " parking spot is " + str(key) + ".")
        details.append("The #" + str((o + 1)) + " parking spot is " + str(value) + " feet away.")
        grades.append(rating(distanceAdressDict2, costAdressDict2, o))
elif preference == "cheapest":
    for p in range(0, 5):
        key = list(costAdressDict2)[p]
        value = list(costAdressDict2.values())[p]

        names.append("The #" + str((p + 1)) + " parking spot is " + str(key) + ".")
        details.append("The #" + str((p + 1)) + " parking spot costs $" + str(value) + " dollars to park there per hour.")
        grades.append(rating(distanceAdressDict2, costAdressDict2, p))

@views.route('/spots')
def spots():
    return render_template('spots.html', names0=names[0],names1=names[1],names2=names[2],names3=names[3],names4=names[4],
                           details0=details[0],details1=details[1],details2=details[2],details3=details[3],details4=details[4],)
