import requests
from requests.auth import HTTPBasicAuth
import json


# Set the URL of the ONOS controller
url = "http://192.168.64.15:8181/onos/v1/intents"
# Set the authentication 
auth = HTTPBasicAuth('onos', 'rocks')
#GET /intents
response = requests.get(url, auth=auth)
intents = response.json()["intents"]
print (intents)