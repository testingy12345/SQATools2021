import requests
import json
patch_api_path="https://reqres.in/api/users/2"
input_data={
    "id":"8064878",
    "name":"Vipin1",
    "job":"Virtusa",
    "salary":"500000"
}
response=requests.patch(patch_api_path,data=input_data)
print(response.status_code)
print(response.content)
json_data=json.loads(response.content)
print(json_data["id"])
