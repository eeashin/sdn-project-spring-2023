import requests
import json

# Set the ONOS controller details
url = "http://192.168.64.16:8181/onos/v1/intents"
auth = ('onos', 'rocks')

# Set the host details
host_red = "B2:18:C0:56:42:3C/-1"
host_black = "D6:F1:AA:C0:E6:A9/-1"

# Set the intent parameters
payload = {
    "type": "HostToHostIntent",
    "appId": "org.onosproject.cli",
    "priority": 103,
    "one": host_red,
    "two": host_black
}

# Send the request to create the intent
response = requests.post(url, auth=auth, data=json.dumps(payload))
print(response.text)
