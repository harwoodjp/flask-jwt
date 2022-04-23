import requests
import json

# POST /login
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# r = requests.post("http://127.0.0.1:5000/login", json={"email":"justin@harwoodjp.com", "password": "admin"}, headers=headers)
# r = requests.post("http://127.0.0.1:5000/login", json={"email":"foo@bar.com", "password": "admin"}, headers=headers)
# print(r.status_code, r.reason)
# print(r.text[:300])

# GET /users
# r = requests.get("http://127.0.0.1:5000/users")
# print(r.status_code, r.reason)
# print(r.text[:300] + '...')


# POST /books
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImlkIjoxfX0.6gM2msKtQVZ9r7RRVOtOrK1rsZLqocW5qw2zsn2Tw9c"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImlkIjoyfX0.rRmGU6YgyO3Er6w9MexHf6YSiJ-18ogANgU0SrbsRGM"
# token = "bad_token"
r = requests.post("http://127.0.0.1:5000/books", json={"token": token}, headers=headers)
print(r.status_code, r.reason)
print(r.text[:300])