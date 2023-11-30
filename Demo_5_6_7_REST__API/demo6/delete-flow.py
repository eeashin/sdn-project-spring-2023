import requests
from requests.auth import HTTPBasicAuth

# Set the URL of the ONOS controller
url = "http://192.168.64.16:8181/onos/v1/flows/"
# Set the authentication 
auth = HTTPBasicAuth('onos', 'rocks')

# Prompt user for device ID and flow ID
device_id = input("Enter device ID: ")
flow_id = input("Enter flow ID: ")

# Construct the URL to delete the flow rule
delete_url = url + device_id + "/" + flow_id

# Send the DELETE request to delete the flow rule
response = requests.delete(delete_url, auth=auth)

# Check the response status code to ensure the flow rule was successfully deleted
if response.status_code == 204:
    print("Flow rule successfully deleted.")
else:
    print("Error deleting flow rule. Status code:", response.status_code)
