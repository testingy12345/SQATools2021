import json


filepath="F:\\ToolsQAPython\\Test_Data.json"


def get_json_data(file_path=filepath):
    with open(file_path,'r') as file:
        data=file.read()
        file_data=json.loads(data)
    return file_data

'''output=get_json_data()
print(output)
print(output['url'])
print(output['users']['user1']['username'])
'''