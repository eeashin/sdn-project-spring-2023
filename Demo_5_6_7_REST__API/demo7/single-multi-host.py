
import requests
import json

# Set the ONOS controller details
url = "http://192.168.64.16:8181/onos/v1/intents"
auth = ('onos', 'rocks')

payload = {
    "type": "SinglePointToMultiPointIntent",
    "appId": "org.onosproject.cli",
    "priority": 110,
    "selector": {
        "criteria": [
            {
                "type": "ETH_TYPE",
                "ethType": "0x0800"
            },
            {
                "type": "IP_PROTO",
                "protocol": 6,
            },
            {
                "type": "TCP_DST",
                "tcpPort": 4009
            }
        ]
    },
    "ingressPoint": {
        "device": "of:00001ecd0832e94c",
        "port": "4"
    },
    "egressPoint": [
        {
            "device": "of:0000aad7370ed845",
            "port": "3"
        },
        {
            "device": "of:000012bffc270a4b",
            "port": "2"
        },
        {
            "device":  "of:0000166648ad8848",
            "port": "4"
        }
    ]
}
# Send the request to create the single to multi host intent for allowing matching traffic
response = requests.post(url, auth=auth, data=json.dumps(payload))
print(response.text)
# Set the payload for the request to block all traffic
block_traffic_payload = {
    "type": "PointToPointIntent",
    "appId": "org.onosproject.cli",
    "priority": 110,
    "selector": {
        "criteria": [
            {
                "type": "ETH_TYPE",
                "ethType": "0x800"
            }
        ]
    },
    "ingressPoint": {
        "device": "of:00001ecd0832e94c",
        "port": "4"
    },        
    "egressPoint": {
            "device": "of:00001ecd0832e94c",
        "port": "9999" # This is a non-existent port
    }
}
  # Send the request to add the intent
response = requests.post(url,  auth=auth, data=json.dumps(block_traffic_payload))
print(response.text)

