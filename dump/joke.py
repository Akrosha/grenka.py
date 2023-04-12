import requests, json

api="https://grenkapy.akrosha.repl.co/api"


print("GET ALL")
r = requests.get(f"{api}/user/")
print(r.text)

print("GET 468719193798213654")

r = requests.get(f"{api}/user/468719193798213654/")
print(r.text)

print("UPDATE MONEY")

data = {
    "api_key": "qwerty",
    "id": "468719193798213654",
    "money": 2000
}

r = requests.put(f"{api}/user/", data=json.dumps(data))
print(r.text)

print("GET 468719193798213654")

r = requests.get(f"{api}/user/468719193798213654/")
print(r.text)