""" 
import http.client

conn = http.client.HTTPSConnection("api.iq.inrix.com")
payload = ''
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IndtbGR5bmRzemMiLCJ0b2tlbiI6eyJpdiI6IjcxMDU4ZjQ2YjhhZDNiZGJhM2U0NDAxYTU4NjY5MTFjIiwiY29udGVudCI6IjA0YmJjMWRmNTdmMDQ5Y2I5ZmU0YTBkMjhlNjZmMDZmN2I5ZTIwNzNhNmM4NzYyZDY5NDhlYjY2ZDg5ZmU4ZWFiNDBhYTEyNTZmOGYxOTdmOTc4ZmNmNTg2YTRlNTMxNmQ4MjExM2M1MTNiZmIwYzEzZTBkM2RjNzQwMjgwNzY2NDhiODI4N2JkMmY4ZjkzYmQyY2VjM2VhYzY0YjQ4Mjk5YWMwM2FiYWRmNGYxYWZmMjUwZWNiODM2MWRiZDFlNzQ1YWNkZjdlNzQzYTBiZmQ1MjBmYmQ4ZDMzMTA3YzFiNDdjMWM2MGZmNWY5YWM3OTM0YmFhYTI3YTgxNjBhODk1YTcxMDEwZjllMmUwNTFmOGQ5MDA3NzZhYWM0NzIxMDQ3YzkyMTNkMzRiOGJkOWZlOWYzNmY0OTI2NWY1MGVhZGNiMjk2MWMyNWE1M2ZmYjIwZWEzYTM3MTM2ZWZhYzczOWQ0ZGE3MDFlZDVmMjFiZTE3OGYxZWZhMmY0MWJlYTY1YjBmNWE5MWVmNzM4MjI2ZDJjN2M5ZGZiN2RjN2UyNjM0NzM3ODdmOGVjOGIzYzAzMjI3NzJiYTViZDM2ZmQzYmU4ZjQyYzEzZTI4YjEzNGIyMGI4YWY0Yjk2ODYwYWZlMjMxYWVjOWU1MWNiZGJlNDc4YTRhMjNjM2MyZWUwOWVjNmIyYWVlMTg3MWUxNDMyNmU3NThjNGY4YjU1YzE2Mzg4ZWY0NjUzMGVjMmMwZTMwYzgyNDg0NzEyY2JiNDhmYjdlNmI1ZGRhN2RmYWQxYjAyNWJhOTZiZDc4ZGRjNmFiMTgzZjQ3ZmZmOTg4ZDAyZjdkMWE4ODViNzg3N2UzZTRjYWQ5NzRiMTA3OTJjMjRjODk1In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI3MTA1OGY0NmI4YWQzYmRiYTNlNDQwMWE1ODY2OTExYyIsImNvbnRlbnQiOiI1OGE0YjM4ZjFmOGU1YWYxODZlMWRiYWJhOTUwZjEzMjFmODU1ZjY5ODE5ZTY3NTU3MzYxOTAxNWE0YzJmY2RmZDUxZGJjNzMxOTk4Mzk1YmM5YzFmNDY2In0sImp0aSI6IjdmMjJiN2FmLTc2MGYtNDU1Ni04Y2VjLTU5YzNlZmIyMWNiOCIsImlhdCI6MTY5OTczNjMzOSwiZXhwIjoxNjk5NzM5OTM5fQ.IuLAbLRducGiAC8xy00mmdVPG5tRLLEcQAYHA1K3fCc'
}
conn.request("GET", "/lots/v3?point=37.74638779388551%257C-122.42209196090698&radius=150", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
"""