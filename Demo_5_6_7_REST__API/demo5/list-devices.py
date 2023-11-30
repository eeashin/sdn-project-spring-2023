import requests
from requests.auth import HTTPBasicAuth
import json
# Set url
url = "http://192.168.64.15:8181/onos/v1/devices"
# Set the authentication 
auth = HTTPBasicAuth('onos', 'rocks')
#GET /devices
response = requests.get(url, auth=auth)
# get the list of devices from JSON response
devices = json.loads(response.text)['devices']
for device in devices:
    print(device['id'])