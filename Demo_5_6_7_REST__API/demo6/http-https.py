import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://192.168.64.16:8181/onos/v1/flows?appId=org.onosproject.fwd"
auth = HTTPBasicAuth('onos', 'rocks')

# JSON for https flow rule 

flow_https = {
    "flows": [
        {
            "priority": 50006,
            "timeout": 0,
            "isPermanent": True,
            "deviceId": "of:0000dad97eeb5845", #device id of br-3, to creat e flow rule on br-3
            "treatment": {
                "instructions": [
                    {
                        "type": "OUTPUT",
                        "port": "2"         
                    }
                ]
            },
            "selector": {
                "criteria": [
                    {
                       "type": "IP_PROTO",
                        "protocol": "6"
                    },
                    {
                        "type": "IPV4_DST",
                        "ip": "10.0.0.2/32" #ip address of namespace red
                    },
                    {
                        "type": "TCP_DST",
                        "tcpPort": "443",
                        "tcpPortMask": "0xFFFF"
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
    #Create https rule
    response = requests.post(url, json=flow_https, auth=auth)
    response.raise_for_status()
    print("flow_https rule created successfully!")
except requests.exceptions.HTTPError as err:
    print(f"Error creating flow_https rule. Status code: {err.response.status_code}. Message: {err.response.content}")

# JSON for http flow rule 
flow_http = {
    "flows": [
        {
            "priority": 50006,
            "timeout": 0,
            "isPermanent": True,
            "deviceId": "of:0000dad97eeb5845", #device id of br-3, to creat e flow rule on br-3
            "treatment": {
                "instructions": [
                    {
                        "type": "OUTPUT",
                        "port": "2"         
                    }
                ]
            },
            "selector": {
                "criteria": [
                    {
                       "type": "IP_PROTO",
                        "protocol": "6"
                    },
                    {
                        "type": "IPV4_DST",
                        "ip": "10.0.0.2/32" #ip address of namespace red
                    },
                    {
                        "type": "TCP_DST",
                        "tcpPort": "80",
                        "tcpPortMask": "0xFFFF"
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
     #Create http rule
    response = requests.post(url, json=flow_http, auth=auth)
    response.raise_for_status()
    print("flow_http rule created successfully!")
except requests.exceptions.HTTPError as err:
    print(f"Error creating flow_http rule. Status code: {err.response.status_code}. Message: {err.response.content}")

#JSON to block other traffic 
flow_block = {
    "flows": [
        {
            "priority": 50005,
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
                        "type": "IPV4_DST",
                        "ip": "10.0.0.2/32" #ip address of namespace red
                    }
                ]
            }
        }
    ]
}

try:
    #Create to block other traffic 
    response = requests.post(url, json=flow_block, auth=auth)
    response.raise_for_status()
    print("flow_block rule created successfully!")
except requests.exceptions.HTTPError as err:
    print(f"Error creating flow_block rule. Status code: {err.response.status_code}. Message: {err.response.content}")
