import requests
import json


data= open("sample_data.json","r").read()
data = json.loads(data)

print(data)

#data= {"data": json.dumps(data)}

resp=requests.post("http://149.165.157.107:5001/upload", json=data)

print(resp.status_code)