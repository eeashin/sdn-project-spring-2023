import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://192.168.64.16:8181/onos/v1/flows?appId=org.onosproject.fwd"
auth = HTTPBasicAuth('onos', 'rocks')
flow_request_body = {
    "flows": [
        {
            "priority": 50001,
            "timeout": 0,
            "isPermanent": True,
            "deviceId": "of:0000dad97eeb5845", #device id of br-3, to creat e flow rule on br-3
            "tableId": 0,
            "treatment": {
                "instructions": [
                    {
                        "type": "NOACTION"
                    }
                ]
            },
            "selector": {
                "criteria": [
                    {
                        "type": "ETH_TYPE",
                        "ethType": "0x0800"
                    },
                    {
                        "type": "IPV4_SRC",
                        "ip": "10.0.0.3/32" #ip address of namespace blue
                    },
                    {
                        "type": "IPV4_DST",
                        "ip": "10.0.0.2/32" #ip address of namespace red
                    },
                    {
                        "type": "IP_PROTO",
                        "protocol": "1"
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
