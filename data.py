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
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IndtbGR5bmRzemMiLCJ0b2tlbiI6eyJpdiI6ImE5YTkwZWI5Nzc0YTFkNjVhYWFmMTE1MzkzOGE3NzA2IiwiY29udGVudCI6IjU0YjU5YmVkMDA5MjhjN2QxZDA3Y2RiMTY3ZWUzYmJhZDBiYWFmY2RjM2M5ZDhkOTliOWYzZTVlMmE0OWFjMTM4OWMyM2JkMTE3NjFlNjU1ZTkzYjExZjNhMTE5MmM1ZGE4YmNiNWVhZmEyZjkxMDU3ZTk4ZTBlYmY1ZjQxMjQ5NjE1YmMwMzZjYzAxOGYzYTFkMTkzZjA3Njk0NGYwN2M0MTRlZjA1YjNiNWZkOWJlOWUxNTQzOTI1Mzc2YTVmZjNjMjgyMGQ4NDZhNzM4NDgxY2JlNWUwNzJkODVkMWYwMWM5YmMyOWYyYmVmMWU1ODYyYjk5NDdkOWEwYTIxMjYxMmNmMmY4YTM0NzFiMWM4NDBmOWFmZmZiYzhiMTdlMWU1OTg0ZmRmNjY1NDE2ZGJlNGZkNGFkNzNkYzgyZTUzOWQ4YjgyMDVlNWU2MDJiZDUwYzk3MjdjMDExNjMwMmM0YjNjMTI3ZjlhZGYwM2QxODRiMzg4Mzc1MzYxMTliMWE1NDAxM2M2MzU1MjgzMzQ0ZDk4NGQ3YmIxMTFjNDI2OWNhYjNkOWMyMjhlOTE3MjE0Mjg1ZDQ4ZDI4YWZlNGY3ZGFkOGMyZDVkZGJhMTMwMzMzMDlkODBlZjgyYTM0NmYwNTQ5ZTJkYzgwOWIxYjdkOGUwZWQxMmNiYTg1MGYwZTBhMDk3MGU0YTIzZmE2YThlZjE3ZTBiN2RmY2UzYjI4MzFlMGE1NGUyYmU3MTMwOTZhODJlNjJiMjE2OTJmNzhlNmM4YThlZDJhYjQyYzg0MzUzYjJjZDNiOTEyYzQ4OWFjM2IzYTBmNGNiZjg2ZjY2MTRlMWZlYzUyZjY5YWNiOWE1NzA2YzY5NDc4OTQ4MDBkNWRiIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJhOWE5MGViOTc3NGExZDY1YWFhZjExNTM5MzhhNzcwNiIsImNvbnRlbnQiOiI1NzhhOTVlMzNhODJkOTVhNmI0NGMwYjU1MGM2NGFiOWM2YWE5N2VlZGZkNGJlYzFiMGE4MDcyZDI5MDhiMDAzYjdlOTJiYzUxMzQ5ZjI3NmVlM2QwMGNkIn0sImp0aSI6IjUyNDAzN2IwLWNlMmItNDNhOC1iMWQ1LWM3NGE5MmMyMzc4NiIsImlhdCI6MTY5OTc1OTY5NiwiZXhwIjoxNjk5NzYzMjk2fQ.YUBOeDxWdubQEF3MsiuatfOUdhXvvZujtgY6OeBrdw4'
}
response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

names = []
probability = []
openSegments = []
segmentNames = []
segmentDict = {}
probDict = {}
bestStreetProb = 0

r = (response.json()).get('result')
#print(r)

for i in range(0, len(r)):
    names.append(r[i].get('name'))
    probability.append(r[i].get('probability'))

    if(r[i].get('probability') > bestStreetProb):
        bestStreetProb = r[i].get('probability')

    segments = r[i].get('segments')


    for j in range(0, len(segments)):
        spaces = segments[j].get('spacesTotal')
        isOpen = segments[j].get('isOpen')

        if spaces >= 1 & isOpen == True:
            segmentDict[segments[j].get('segmentID')] = [r[i].get('name'), r[i].get('probability'), segments[j].get('side'), segments[j].get('start'), segments[j].get('end')]


#print(names)
#print(probability)
#print(openSegments)
#print(segmentNames)
#print(probDict)
print(segmentDict)
