import requests
from requests.auth import HTTPBasicAuth

url = "http://192.168.64.16:8181/onos/v1/intents"
auth = HTTPBasicAuth('onos', 'rocks')

# Get all the intents
response = requests.get(url, auth=auth)
if response.status_code != 200:
    print("Error: Failed to get the intents")
    exit()

intents = response.json()["intents"]

# Delete all the intents
for intent in intents:
    app_id = intent["appId"]
    key = intent["key"]
    response = requests.delete(url + "/" + app_id + "/"+key, auth=auth)
    if response.status_code != 204:
        print("Error: Failed to delete the intent with KEY {}".format(key))
        exit()

print("All the intents have been deleted successfully!")
