import json

import requests

target_email = "tobias.funke1@reqres.in"

api1_url = "https://reqres.in/api/users?page=2"
response=requests.get(api1_url)
print(response.status_code)
response_data=response.content
print(response_data)
json_data=json.loads(response_data)
print(json_data["data"])

exist=False
for data in json_data["data"]:
    print(data)
    if target_email in data['email']:
        exist=True
        break
    else:
        continue
print("Expected email exist :",exist)


#page_data = response_data["data"]
#for data in page_data:
    #print(data)
