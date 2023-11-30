import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://192.168.64.16:8181/onos/v1/flows?appId=org.onosproject.fwd"
auth = HTTPBasicAuth('onos', 'rocks')
flow_request_body = {
    "flows": [
        {
            "priority": 50000,
            "timeout": 0,
            "isPermanent": True,
            "deviceId": "of:0000dad97eeb5845", #device id of br-3, to creat e flow rule on br-3
            "treatment": {
                "instructions": [
                    {
                        "type": "OUTPUT",
                        "port": "3"         #port 3 is the port which is connected to namespace blue
                    },
                    {
                        "type": "OUTPUT",
                        "port": "4"         #port 4 is the port which is connected to namespace green
                    }
                ]
            },
            "selector": {
                "criteria": [
                    {
                        "type": "IPV4_SRC",
                        "ip": "10.0.0.2/32" #ip address of namespace red
                    },
                    {
                        "type": "IPV4_DST",
                        "ip": "10.0.0.3/32" #ip address of namespace blue
                    },
                    {
                        "type": "ETH_TYPE",
                        "ethType": "0x0800" 
                    }
                ]
            }
        }
    ]
}

try:
    response = requests.post(url, json=flow_request_body, auth=auth)
    response.raise_for_status()
    print("Flow rule created successfully!")
except requests.exceptions.HTTPError as err:
    print(f"Error creating flow rule. Status code: {err.response.status_code}. Message: {err.response.content}")
