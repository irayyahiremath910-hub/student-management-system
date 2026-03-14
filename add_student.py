import requests

url = "http://127.0.0.1:5000/students"

data = {
    "id": "101",
    "name": "Rahul",
    "age": 21,
    "course": "Information Science"
}

response = requests.post(url, json=data)

print(response.json())