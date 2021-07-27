import requests
import json

delete_api_path = "https://reqres.in/api/users/2"


response = requests.delete(delete_api_path)

print(response.status_code)
print(response.content)