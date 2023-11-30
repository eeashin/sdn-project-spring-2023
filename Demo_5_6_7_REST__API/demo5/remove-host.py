import requests
from requests.auth import HTTPBasicAuth
import json

# Set the URL of the ONOS controller
url = "http://192.168.64.15:8181/onos/v1/hosts"
# Set the authentication 
auth = HTTPBasicAuth('onos', 'rocks')
# Set the IP address of the host to lookup
ip_address = "10.0.0.130"
# Make an HTTP GET request to retrieve the host information
response = requests.get(url, auth=auth)
# Parse the response as JSON and search for the host with the given IP address
hosts = response.json()["hosts"]
mac = ""
vlan = ""
for host in hosts:
    if ip_address in host["ipAddresses"]:
        mac = host["mac"]
        vlan = host["vlan"]
        break
# Make an HTTP DELETE request to remove the host
response = requests.delete(f"{url}/{mac}/{vlan}", auth=auth)