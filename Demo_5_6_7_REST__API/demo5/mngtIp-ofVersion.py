import requests
from requests.auth import HTTPBasicAuth
import json
# Set url
url = "http://192.168.64.15:8181/onos/v1/devices/{device_id}"
# Set the authentication 
auth = HTTPBasicAuth('onos', 'rocks')
#GET /devices
response = requests.get(url, auth=auth)
# Prompt the user for the device ID
device_id = input('Enter device ID: ')
#GET /devices/{deviceId}
url = url.format(device_id=device_id)
response = requests.get(url, auth=auth)
# get IP Management address and OpenFlow version of devices from JSON response
device_info = json.loads(response.text)
ip_address = device_info['annotations']['managementAddress']
of_version = device_info['annotations']['protocol']
print(f'Device ID: {device_id}')
print(f'IP Management Address: {ip_address}')
print(f'OpenFlow Version: {of_version}')