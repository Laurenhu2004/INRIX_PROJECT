import requests

url = "https://api.iq.inrix.com/blocks/v3?point=37.74304518280319%7C-122.42438793182373&radius=50"

payload = {}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IndtbGR5bmRzemMiLCJ0b2tlbiI6eyJpdiI6ImFkMDQxYzVlYTY5YzI2OTgyMGQ2MjYzYmU5NGEzODBlIiwiY29udGVudCI6IjZkMzdjMzliMmM5Nzk4NjViNjVjZDJmOWY4NDczOGNhOWU3ZGVhNmJiZjJkMDBhY2VkMjVkOTlhNmJlZTY2MmVkNGIyOGUwMGRjNjJhODY4M2UwMjEyNzM5Y2Q5MDA3MWQ1NzljZmM2OGEwMzIxNWJiMDZlNTZhZjUzNWVmNWNhODdmMGYwZWI1NmFjYjkzMjk3ZDkzZjE4NjkwZWU0ZjhjZjkzMGIzY2IyN2ZkNmI3NWEzMzZmZGVjYzI1ZTc4NTgzM2E2YzhmOGE0Zjk2ODIzZTExYmIyMTIyNGFjZGNmMWJkNmJiMjJiYmUxOWQ4ZDczMDZiYzIzODcxYmIxYWM4NWJhMWM5MjU5YzM2NjcyMjk1MTlkZjMzYjgzMDQ5NDU1MWFmZDk5MjRjMGYxMzYxNzAyMzA3MGVkZTdlZWJkNmQyMTc4YTg4NmJkMzUzZmYzNGIxMjc1MWEzNGMzZTQ4ODk4NDAzMDYxZDVlMjY3MzE3NDMwMGU3ZTU3NmRmODMxNTBiNDRhODA1NDdiODQ2ZmFiZGUwODZlOWU3MzBkZjIwNWE2MzlkY2VkM2Y0MjdlN2Y3YTZjNGM2Nzc5ZTk0YzcxYmVhMzVkNzU4ZGEyNTE2NmVhNDBlZDk1MzBkYzlmYjEyNzAwMDI1ZTI2ZGI2NzRhOTNkYmQxYmY1ODVmNjBhZDkyYmVkMzc3M2NmOTA2YjlkNmFlNmYwYmQxMjE3YTQ4OGJmOWJlNDA5MmU2NzNhMmE5MDQ4M2FjMTkzMTNmYTM3OGQ3MTA4NWIxYzIxYzlmYjBjNDI4NWY0YjlhMmY0ZjU2Y2MyYjgxNTA0MzIwNmU0NzBhYzE1ZjA0ZWEwN2Y1OWUyYzYxN2RmYmQ0NTAifSwic2VjdXJpdHlUb2tlbiI6eyJpdiI6ImFkMDQxYzVlYTY5YzI2OTgyMGQ2MjYzYmU5NGEzODBlIiwiY29udGVudCI6IjY3NzlkMGE3Nzc4YWE5NDBhMzUwZDdjMzliNGIyMGI2YTA1M2NkNjBhMTBiMDJkMGY2NTZmMzk0NTNkMDcwMzBjY2EwOTc3MWM0NGQ5OTRiMjEwYTEzNGQifSwianRpIjoiMzExZGM5NjktNzAyYS00ZGEyLWJjMDktMzZkMGZlZDRkZWVlIiwiaWF0IjoxNjk5NzQzMDMwLCJleHAiOjE2OTk3NDY2MzB9.S21aia8M-ltE8rSSgd6qNv5TwgeBz8rod7Zexl8wn78'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

names = []
probability = []
seg = []

r = (response.json()).get('result')


cost1 = r[0].get('rateCards')

for i in range(0, len(r)):
    names.append(r[i].get('name'))
    probability.append(r[i].get('probability'))
    segments = r[i].get('segments')

    for j in range(0, len(segments)):
        spaces = segments[j].get('spacesTotal')
        isOpen = segments[j].get('isOpen')

    
print(names)
print(probability)

#r = ((response.json()).get('result'))[0].get('name')

#print(r)





