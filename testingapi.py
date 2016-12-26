import requests
import json	
#parameters = {"username" : 8c818e92-ce0e-40e4-8e5f-20ab9b839f1f, "password" : PFfXrQRiMAUY}
#response = requests.get("https://gateway.watsonplatform.net/tradeoff-analytics/api/v1/dilemmas?generate_visualization=false", params=parameters)
from requests.auth import HTTPBasicAuth
# Print the status code of the response.
from os.path import join, dirname
from watson_developer_cloud import TradeoffAnalyticsV1



tradeoff_analytics = TradeoffAnalyticsV1(

  username='8c818e92-ce0e-40e4-8e5f-20ab9b839f1f',
  password='PFfXrQRiMAUY')
with open('/home/sethinitin4/Downloads/problem.json') as problem_json:
#with open(os.path.join('/home/sethinitin4/Downloads', 'problem.json')) as problem_json:
  dilemma = tradeoff_analytics.dilemmas(json.load(problem_json),
                                        generate_visualization=False)

print(json.dumps(dilemma, indent=2))