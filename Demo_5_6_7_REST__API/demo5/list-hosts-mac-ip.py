import requests
from requests.auth import HTTPBasicAuth
import json

# Set the URL of the ONOS controller
url = "http://192.168.64.15:8181/onos/v1/hosts"

# Set the authentication 
auth = HTTPBasicAuth('onos', 'rocks')

# Make an HTTP GET request to retrieve the list of hosts
response = requests.get(url, auth=auth)

# Check if the request was successful
if response.status_code != 200:
    print(f"Error: {response.status_code} - {response.text}")
    exit()
# Parse the response as JSON and extract the host information
hosts = response.json()['hosts']
host_ids = [host["id"] for host in hosts]
mac_addresses = [host["mac"] for host in hosts]
ip_addresses = [host["ipAddresses"] for host in hosts]

# Print the host information
print("Host IDs:", host_ids)
print("MAC Addresses:", mac_addresses)
print("IP Addresses:", ip_addresses)
