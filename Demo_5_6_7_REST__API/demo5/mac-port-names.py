import requests
from requests.auth import HTTPBasicAuth
import json

device_id = input("Enter the device ID: ")

url = "http://192.168.64.15:8181/onos/v1/devices/{}/ports".format(device_id)
print(url)
#headers = {"Content-Type": "application/json"}
auth = HTTPBasicAuth("onos", "rocks")

response = requests.get(url, auth=auth)
if response.ok:
    data = response.json()
    #print(data)
    for port in data["ports"]:
        if port["isEnabled"]:
            print("Port name:", port["annotations"]["portName"])
            print("MAC addresses:",port["annotations"]["portMac"])
            print("---------------------------")
else:
    print("Error retrieving port information for device:", device_id)
    print("Response code:", response.status_code)
