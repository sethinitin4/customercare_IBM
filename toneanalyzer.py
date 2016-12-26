import requests
import json	
from requests.auth import HTTPBasicAuth
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3



tone_analyzer = ToneAnalyzerV3(
   username='0b8745a9-77f9-444f-85aa-d6a02f09b853',
   password='ifyDaK8rvt4F',
   version='2016-05-19')
with open('/home/sethinitin4/Downloads/test_tone.txt') as file:
  dilemma = tone_analyzer.tone(file)

print(json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2))