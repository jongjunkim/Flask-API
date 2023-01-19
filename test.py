import requests

BASE  = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Joe", "views": 1000000},
        {"likes": 10, "name": "Jun", "views": 8000000},
        {"likes": 30, "name": "Hey", "views": 6000000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())