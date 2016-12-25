
import requests
import json	
#parameters = {"username" : 8c818e92-ce0e-40e4-8e5f-20ab9b839f1f, "password" : PFfXrQRiMAUY}
#response = requests.get("https://gateway.watsonplatform.net/tradeoff-analytics/api/v1/dilemmas?generate_visualization=false", params=parameters)
from requests.auth import HTTPBasicAuth
# Print the status code of the response.


#headers = {'Content-Type':'application/json'}
#r = requests.post('https://gateway.watsonplatform.net/tradeoff-analytics/api/v1/dilemmas?generate_visualization=false', data=open('/home/sethinitin4/Downloads/problem.json', 'rb'), headers=headers)
#response=requests.get('https://gateway.watsonplatform.net/tradeoff-analytics/api/v1/dilemmas?generate_visualization=false', auth=HTTPBasicAuth('8c818e92-ce0e-40e4-8e5f-20ab9b839f1f', 'PFfXrQRiMAUY'))



headers = {'Content-Type':'application/json'}
r = requests.post('https://gateway.watsonplatform.net/tradeoff-analytics/api', data=open('/home/sethinitin4/Downloads/problem.json', 'rb'), headers=headers)
response=requests.get('https://gateway.watsonplatform.net/tradeoff-analytics/api', auth=HTTPBasicAuth('8c818e92-ce0e-40e4-8e5f-20ab9b839f1f', 'PFfXrQRiMAUY'))
#sponse=requests.get('https://, auth=('8c818e92-ce0e-40e4-8e5f-20ab9b839f1f', ''))
result=response.content  
#print(result.status_code)
print(type(result.decode("utf-8")))
print(result.decode("utf-8"))
print(response.status_code)
#print(type(response.content))