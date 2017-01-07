# an early attempt to work with the API using requests library
import requests
import json	
from requests.auth import HTTPBasicAuth

headers = {'Content-Type':'application/json'}
r = requests.post('https://gateway.watsonplatform.net/tradeoff-analytics/api', data=open('/home/sethinitin4/Downloads/problem.json', 'rb'), headers=headers)
response=requests.get('https://gateway.watsonplatform.net/tradeoff-analytics/api', auth=HTTPBasicAuth('8c818e92-ce0e-40e4-8e5f-20ab9b839f1f', 'PFfXrQRiMAUY'))
result=response.content  
print(type(result.decode("utf-8")))
print(result.decode("utf-8"))
print(response.status_code)

#result was an empty binary file
#status code 200