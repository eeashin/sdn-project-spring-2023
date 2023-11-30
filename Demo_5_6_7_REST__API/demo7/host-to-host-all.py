import requests
import json

def host_to_host_intent(one, two):
    # Set the ONOS controller details
    url = "http://192.168.64.16:8181/onos/v1/intents"
    auth = ('onos', 'rocks')

    # Set the intent parameters
    payload = {
        "type": "HostToHostIntent",
        "appId": "org.onosproject.cli",
        "priority": 104,
        "one": one,
        "two": two
    }

    # Send the request to create the intent
    response = requests.post(url, auth=auth, data=json.dumps(payload))
    print(response.text)

def create_intents(namespaces):
    # Iterate over all pairs of namespaces
    for i in range(len(namespaces)):
        for j in range(i+1, len(namespaces)):
            ns1 = namespaces[i]
            ns2 = namespaces[j]
            # Create the host-to-host intent between the hosts
            host_to_host_intent(ns1, ns2)

# Set the host mac addresses details
red = "B2:18:C0:56:42:3C/-1"
black = "D6:F1:AA:C0:E6:A9/-1"
green = "2A:48:76:22:68:D6/-1"
blue = "B6:2B:44:C0:CD:3A/-1"
yellow = "BE:52:AA:52:6D:55/-1"
# Call the function with the list of namespace mac addresses details
create_intents([red, black, green, blue, yellow])


