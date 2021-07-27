import requests
import json
post_api_path="https://reqres.in/api/users"
input_data={
    "id":"8064878",
    "name":"Vipin",
    "job":"Virtusa",
    "salary":"50000"
}
response=requests.post(post_api_path,data=input_data)
print(response.status_code)
print(response.content)
json_data=json.loads(response.content)
print(json_data["id"])
