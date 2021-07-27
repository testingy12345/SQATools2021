import requests
import json

post_api_path = "https://reqres.in/api/register"

input_data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = requests.post(post_api_path, data=input_data)

print(response.status_code)
print(response.content)

json_data = json.loads(response.content)

print(json_data["id"])