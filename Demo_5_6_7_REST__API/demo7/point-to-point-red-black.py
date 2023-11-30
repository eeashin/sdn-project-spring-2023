import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://192.168.64.16:8181/onos/v1/intents"
auth = ('onos', 'rocks')

def add_intent(src_device, src_port, dst_device, dst_port):
    # Set thepayload for the request
    payload = {
        "type": "PointToPointIntent",
        "appId": "org.onosproject.cli",
        "priority": 111,
        "selector": {
            "criteria": [
                {
                    "type": "ETH_TYPE",
                    "ethType": "0x800"
                }
            ]
        },
        "ingressPoint": {
            "device": src_device,
            "port": src_port
        },        
        "egressPoint": {
             "device": dst_device,
            "port": dst_port
        }
    }
    # Send the request to add the intent
    response = requests.post(url,  auth=auth, data=json.dumps(payload))
    print(response.text)

# Add the intents red-black : add_intent(src_device, src_port, dst_device, dst_port)
add_intent("of:00001ecd0832e94c", "4", "of:00001ecd0832e94c", "1")
add_intent("of:0000b6c236375e49", "1", "of:0000b6c236375e49", "2")
add_intent("of:0000166648ad8848", "2", "of:0000166648ad8848", "4")
# Add the intents black-red : add_intent(src_device, src_port, dst_device, dst_port)
add_intent("of:0000166648ad8848", "4", "of:0000166648ad8848", "2")
add_intent("of:0000b6c236375e49", "2", "of:0000b6c236375e49", "1")
add_intent("of:00001ecd0832e94c", "1", "of:00001ecd0832e94c", "4")