#Thos file is to test tradeoff analytics API by IBM
import requests
import json	
from os.path import join, dirname
from watson_developer_cloud import TradeoffAnalyticsV1
#parameters = {"username" : 8c818e92-ce0e-40e4-8e5f-20ab9b839f1f, "password" : PFfXrQRiMAUY}
#response = requests.get("https://gateway.watsonplatform.net/tradeoff-analytics/api/v1/dilemmas?generate_visualization=false", params=parameters)
#above code does not work and returns empty binary

from requests.auth import HTTPBasicAuth
tradeoff_analytics = TradeoffAnalyticsV1(
  username='servicecredentials-username',
  password='servicecredentials-password')#create an instance

with open('/home/sethinitin4/Downloads/problem.json') as problem_json:
#enter your file path for json
  dilemma = tradeoff_analytics.dilemmas(json.load(problem_json),
                                        generate_visualization=False)
print(json.dumps(dilemma, indent=2))