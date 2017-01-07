#The tone analyzer API is used to analyze subjective queries
#This portion needs to incorporated still and returned json will give anger and sadness values which will me minimized.
import json	
from requests.auth import HTTPBasicAuth
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
   username='servicecredential-username',#enteryourusername
   password='servicecredential-password',#enteryourpassword
   version='2016-05-19')# creating an instance of the service

with open('/home/sethinitin4/Downloads/test_tone.txt') as file:
  dilemma = tone_analyzer.tone(file)#your text file

print(json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2))
#fit in your file in place of text for analysis