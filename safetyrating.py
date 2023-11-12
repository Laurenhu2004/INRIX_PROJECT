#!/usr/bin/env python
# coding: utf-8

# In[120]:


import requests
import json
import math

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

def get_safety_rating(crime):  
    safety = summ/151
    if safety >=1.75:
        return 1
    if safety >1.2:
        return 2
    if safety >0.7:
        return 3
    if safety >=0:
        return 4

print(get_safety_rating(summ))

