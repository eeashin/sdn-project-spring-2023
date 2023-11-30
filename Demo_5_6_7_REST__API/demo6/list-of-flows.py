import requests
from requests.auth import HTTPBasicAuth
import json
from tabulate import tabulate

# Set the URL of the ONOS controller
url = "http://192.168.64.16:8181/onos/v1/flows/"
# Set the authentication 
auth = HTTPBasicAuth('onos', 'rocks')
#GET /flows/
response = requests.get(url, auth=auth)
flows = response.json()["flows"]
flows_by_device = {}

# Loop through each flow in the flows list
for flow in flows:
    device_id = flow["deviceId"]
    flow_info = [flow["priority"], flow["appId"], flow["state"], flow["tableId"],flow["id"], flow["bytes"]]
    if device_id not in flows_by_device:
        flows_by_device[device_id] = []
    flows_by_device[device_id].append(flow_info)

# Loop through each device id in the dictionary and output the flows data in a table
for device_id in flows_by_device:
    print("Device ID:", device_id)
    print(tabulate(flows_by_device[device_id], headers=["Priority", "App ID", "State", "Table ID", "Flow ID","Bytes"]))
    print()
