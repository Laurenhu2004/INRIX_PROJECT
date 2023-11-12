import requests
import json

address = "1301 Church St, San Francisco, CA 94114"
radius = "50"

location_API = requests.get("https://geocode.maps.co/search?q={}".format(address))
info = location_API.text
parse_json = json.loads(info)
lati = parse_json[0]['lat']
print(lati)

long = parse_json[0]['lon']
print(long)

url = "https://api.iq.inrix.com/blocks/v3?point={}%7C{}&radius={}".format(lati, long, radius)

#url = "https://api.iq.inrix.com/blocks/v3?point=37.74304518280319%7C-122.42438793182373&radius=50"

payload = {}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IndtbGR5bmRzemMiLCJ0b2tlbiI6eyJpdiI6ImQ0NjE3YmNlZDA5ZWQ0MzhmMDRiNzkyN2I4YmU4MDM2IiwiY29udGVudCI6Ijk5N2FhZTk2ODBhMGY0ZTA3Yzg0ZTcwMGEwMTFiMjhjOWZhYzY5OThmZjhhZWRkZGM1ZWU1Y2U3MWZiYTQzNjY2NTkzMjczY2YxMzFhYzk2YmUxMjFlODFmMmEwMWNkNDE0NjczODBmOWU4MjM1OGUxZDg0NTdmZTA1NzJkNDE4ZjdlNjdjOGFmYjM2ZTYwMzk5MTljYzAzNjA2YzMzOWJmM2FkMmJjMDFmNjIzODExYjQzMjM0NjRlMjZhYzhhMzQzN2Q2MGNmNTk1YzNlMjRkNGZjOTkwMjY2NDNmZDRkZTc0Y2NhNTE1NDU3NDQ5ZWExMmZiMTAyYTNmZmFjZDk0Y2RjY2Y3MDU3MjM1ZDNiOWNlYjNkMzBiMzQ2ODc2OTNjZDIxMjU2NzhiMjVmNmVhNzliOGNlYzU4ZTJlNGQwMjczMjYwYzU1ODIyN2Q5ZTc0MjQwNDU2NTY5ZmFjNzg3Y2Y0Nzk4ZDI4NDE2NjE4MTdhMjVmMzMwYmQ5MzYzZDk5OWQ1NTE5Yjc0MjY4NDU5YzM0MTZlZjAzODUzMTQ5OWQyNzQxZDdkN2MzZTRhNjBjOWNjZmZiMjEzNDIyNWNmNDhiYWRhNjhkNGViMjljMGUzYzJiZWIzZGQ3ZTZjYWVkM2M0Yjg4MmMxMjVkN2I4NDI5NWEwZjkyZjdhZjk3ZTgyMzJlYjA2ZjE5YzBlYmRlNTViNmJkZDJiZGUyMTk1ODBiM2E4NWJmZGM4MTEyMWEyOGJjZmU2ZmRhZGY1YTZlMzlkZjVjODIyMTgxYTg1MjkzNTZlOWFlYjg3YjdkOWU4Mzc2ODUxOGVlNmM1ZjI3N2Y5NGQ0MjlhMGRjNDYxNzJkOGY1YWJkNjlkZjg3OWExMjczIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJkNDYxN2JjZWQwOWVkNDM4ZjA0Yjc5MjdiOGJlODAzNiIsImNvbnRlbnQiOiJkMTZjZGRiYmQ0ZDZlNWNhMWU5Nzg3MGE5MjNhOTZkY2JkODM3MWRiZGY5MGNkODFkNGRlM2ZhMjE4OWM1YjczMDFhNjE3NmRiOTM2OTZiYTgxMjMyNWJmIn0sImp0aSI6ImFhMjYwNDk5LTg4MmQtNDk4MC05MTZhLTAyMThjN2NiYWI5OCIsImlhdCI6MTY5OTc1MzQxMSwiZXhwIjoxNjk5NzU3MDExfQ.JFl9jtRMhYQrFsGYJPRvOwGpXuVEphgx114syrQBzKE'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

names = []
probability = []
openSegments = []
segmentNames = []
segmentDict = {}

r = (response.json()).get('result')

for i in range(0, len(r)):
    names.append(r[i].get('name'))
    probability.append(r[i].get('probability'))
    segments = r[i].get('segments')

    for j in range(0, len(segments)):
        spaces = segments[j].get('spacesTotal')
        isOpen = segments[j].get('isOpen')

        if spaces >= 1 & isOpen == True:
            #openSegments[r[i].get('name')] = segments[j].get('segmentID')
            openSegments.append(segments[j].get('segmentID'))
            segmentNames.append(r[i].get('name'))


for k in range(len(openSegments)):
    segmentDict[openSegments[k]] = segmentNames[k]


    

#print(names)
print(probability)
#print(openSegments)
#print(segmentNames)

print(segmentDict)
print(len(segmentDict))

#r = ((response.json()).get('result'))[0].get('name')

#print(r)