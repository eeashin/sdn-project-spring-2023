import requests
from requests.auth import HTTPBasicAuth
import json
from tabulate import tabulate

# Set the URL of the ONOS controller
url = "http://192.168.64.15:8181/onos/v1/links"
# Set the authentication 
auth = HTTPBasicAuth('onos', 'rocks')
#  GET /links
response = requests.get(url, auth=auth)
# Parse the response as JSON and extract the active links info
links = response.json()["links"]

active_links = [(link["src"]["device"], link["src"]["port"],
                 link["dst"]["device"], link["dst"]["port"]) for link in links if link["state"] == "ACTIVE"]
# Print the active links information as a table
print(tabulate(active_links, 
headers=["Device ID Source", 
"Port Source", 
"Device ID Destination", 
"Port Destination"]))