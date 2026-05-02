# Import the request library
import requests

# Import the request.auth library
from requests.auth import HTTPBasicAuth

# Import the getpass
from getpass import getpass

# Import the json library to handle JSON data
import json

# Define the endpoints for the routers
routers = {
    "R1": "192.168.42.129",
    "R2": "192.168.42.130"  
}

# Define the interface config for the routers (multi-interface per router)
interfaces = {
    "R1": {
        "GigabitEthernet2": {
            "type": "iana-if-type:ethernetCsmacd",
            "description": "Configured via RESTCONF API",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "192.168.1.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            }
        },
        "GigabitEthernet3": {
            "type": "iana-if-type:ethernetCsmacd",
            "description": "Configured via RESTCONF API",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "192.168.2.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            }
        }
    },
    "R2": {
        "GigabitEthernet2": {
            "type": "iana-if-type:ethernetCsmacd",
            "description": "Configured via RESTCONF API",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "192.168.1.2",
                        "netmask": "255.255.255.0"
                    }
                ]
            }
        },
        "GigabitEthernet3": {
            "type": "iana-if-type:ethernetCsmacd",
            "description": "Configured via RESTCONF API",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "192.168.2.2",
                        "netmask": "255.255.255.0"
                    }
                ]
            }
        }
    }
}

# Loop through each router and configure multiple interfaces
for r, i in routers.items():
    print(f"Connecting to {r} at {i} ...")

    # Define the creds to the endpoint
    creds = HTTPBasicAuth(username=input(f"Enter your username for {r}: "), password=getpass(f"Enter your password for {r}: "))

    # Define the header
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json",
    }
    
    # Loop through each interface configuration for this router
    for intf_name, intf_config in interfaces[r].items():
        # Define the URL to the restconf endpoint for the interfaces collection
        url = f"https://{routers[r]}/restconf/data/ietf-interfaces:interfaces"
        
        # Define the payload with correct YANG structure (interfaces array with interface element)
        payload = {
            "ietf-interfaces:interfaces": {
                "interface": [
                    {
                        "name": intf_name,
                        **intf_config
                    }
                ]
            }
        }
        
        # Use PATCH to update the interfaces collection
        response = requests.patch(url=url, auth=creds, headers=headers, json=payload, verify=False)

        # Print the response status code and the response body
        print(f"Response Status Code for {r} {intf_name}: {response.status_code}")
        if response.status_code not in [200, 204]:
            print(f"Response Body: {response.text}")
        else:
            print(f"Successfully configured {r} {intf_name}")
            
        # Verify the configuration by sending a GET request to the same endpoint
        verify_response = requests.get(url=url, auth=creds, headers=headers, verify=False)
        print(f"Verification Response Status Code for {r} {intf_name}: {verify_response.status_code}")
   