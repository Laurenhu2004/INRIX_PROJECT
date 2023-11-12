import requests
import json

address = "1301 Church St, San Francisco, CA 94114"
radius = "50"

location_API = requests.get("https://geocode.maps.co/search?q={}".format(address))
info = location_API.text
parse_json = json.loads(info)
lati = parse_json[0]['lat']
#print(lati)

long = parse_json[0]['lon']
#print(long)

url = "https://api.iq.inrix.com/blocks/v3?point={}%7C{}&radius={}".format(lati, long, radius)

#url = "https://api.iq.inrix.com/blocks/v3?point=37.74304518280319%7C-122.42438793182373&radius=50"

payload = {}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IndtbGR5bmRzemMiLCJ0b2tlbiI6eyJpdiI6ImZiZDU5ZThiOWU1YzU0ZjU4Nzc1OTA2OWQzZDg2MmVkIiwiY29udGVudCI6ImM5MmYzNTJjYzAxMzJhMGI1Y2Q1NzZkOGRkMDYwYzUzMTZmYjBhMWU1ODg4ZDU5OTEyYTE5ZWVlZDk3M2UyY2Y3MWNiMjFlZDhhZDhkYzdkNzQwZTAyMzdjZTEwMWVmODFmYzBkNzQ2NmQ5MjkwZThjNmZkZDAzNmUzNDMxZjA1YTdlNDBjYmY2ZWI5N2I2ODkxYzg3MDU2NmY1ZTZlNDk5NGJmZTA1NmRmZWU2OGQ0N2E5NjY5NmZjYjc0NTI3OTg4MDdiOWQ0ODJhNWUxZTBiNDUzMWU4ZjYxMWI2YzlhZWYxYjFiZTcyZTI1ZDVlZDFiYTcxOTMwZDViNmNkZTUyNzIxYTMxYzYwMjcwNWI3MGMzNTljMDg2MTg2NDY1ZTRhMzkzZTg3OTVmZGY3MzhlZTU1M2ZmODc5MjYyYTIwMzU2ZThlMTk5NzMzNThlNzE2YzgyYTNiNDdiN2ZiMzZhNmYxNWFkMmE0NWNlZmVjOGEyNDA1NjVlZjM1MjFiMGI0MzY3YzI1ZGNiYWUzYzRmOGJhYzhkMTFhMjQwMTY0OTE2NmFkOWY4YTc5MzljYzZhMDYzNmFkYzc1NWVhNWU2MWQwMmRjYjZlZGE1YmY4MmM5MTRiZDhiOTlhNDE3YTQ2YzM5OWVjMzZmNzQwM2M5OGMwOTJlN2Q4Y2M2OTY4NmM1OWU5ZTVkNzBkZGJiMmUwMTdhOWZmYjY1ZTJjMTgyMTMwNzZjMmExOGEwNjE0ZTNlOGY0ODQyYWNjYmFjY2RjODFmMmVlOTI4OWM4YTdkOWQ4MWQ3OGU1NTkyN2MwYTZhYTkyZjUzNTM3N2I4MzhiNTlhMmFhNDRiZDZmZjI3Y2QzMTVlZDkxNjY2NTMzMTYyMmNkIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJmYmQ1OWU4YjllNWM1NGY1ODc3NTkwNjlkM2Q4NjJlZCIsImNvbnRlbnQiOiJjZDdjMzgwMTkyMWMwMzVhMmFlODBhZGFjZTE3MTc1NjNkZDMzNzFhNWRiNWY2ZDUxOWI0YTViMWM0NmJmMWYxNmJlZDIzZTdkMGQ4ZTM3NjZmMDQxMzA5In0sImp0aSI6IjIyNWIxZjdjLTRiNjEtNDE0My05MzNkLThlYmI4YTk1NGJmYSIsImlhdCI6MTY5OTc1NTgwMiwiZXhwIjoxNjk5NzU5NDAyfQ.O6_o6Vr89yrvhHXgv2ZrPQpyjbjVJz6Y2HOzEyOBumg'
}
response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

names = []
probability = []
openSegments = []
segmentNames = []
segmentDict = {}
probDict = {}

r = (response.json()).get('result')
#print(r)

for i in range(0, len(r)):
    names.append(r[i].get('name'))
    probability.append(r[i].get('probability'))
    segments = r[i].get('segments')

    for j in range(0, len(segments)):
        spaces = segments[j].get('spacesTotal')
        isOpen = segments[j].get('isOpen')

        if spaces >= 1 & isOpen == True:
            openSegments.append(segments[j].get('segmentID'))
            segmentNames.append(r[i].get('name'))

        


for k in range(0, len(openSegments)):
    if 
        temp = [segmentNames[l], probability[k]]
        segmentDict[openSegments[l]] = temp

    
#print(names)
#print(probability)
#print(openSegments)
#print(segmentNames)

#print(probDict)
print(segmentDict)
