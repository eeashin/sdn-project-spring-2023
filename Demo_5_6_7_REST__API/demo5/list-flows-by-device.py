import requests
from requests.auth import HTTPBasicAuth
import json
from tabulate import tabulate

# Set the URL of the ONOS controller
url = "http://192.168.64.15:8181/onos/v1/flows"
# Set the authentication 
auth = HTTPBasicAuth('onos', 'rocks')
# ask user the device ID
device_id = input("Enter the device ID to query: ")
#GET /flows/{deviceId}
response = requests.get(f"{url}/{device_id}", auth=auth)
# Parse the response as JSON and extract the flow information
flows = response.json()["flows"]
flow_info = [(flow["id"], flow["appId"], flow["deviceId"], flow["treatment"]["instructions"]) for flow in flows]
# Print the flow information as a table
print(tabulate(flow_info, headers=["Flow ID", "Application ID", "Device ID", "Instructions"]))




