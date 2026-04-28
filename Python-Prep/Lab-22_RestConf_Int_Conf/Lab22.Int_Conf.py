# Import requests library
import requests

# Import the request.auth library
from requests.auth import HTTPBasicAuth

# Import the getpass
from getpass import getpass

# Import the json library to handle JSON data
import json


# Define the routers details with IP
R1 = "192.168.42.129"


# Define the URL to the restoconf endpoint for interface configuration
get = f"https://{R1}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"
print(f"Connecting to R1 at {R1} ...")

# Defind the creds to the endpoint
creds= HTTPBasicAuth(username = input("Enter your username for R1: "), password = getpass("Enter your password for R1: "))

# Define the header
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

# Defind the interface payload to configure the interface
payload = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet2",
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
    }
}
        
# Use the patch.request method to send the PATCH request to the specified URL with the provided credentials, headers and payload
response = requests.patch(url = get, auth = creds, headers = headers, json = payload, verify = False)

# Print the response status code and the response body
print(f"Response Status Code: {response.status_code}")
print(f"Response Body: {response.text}")


# Verfiy the configuration by sending a GET request to the same endpoint
response = requests.get(url = get, auth = creds, headers = headers, verify = False)
# Print the response status code and the response body
print(f"Verification Response Status Code: {response.status_code}") 
print(f"Verification Response Body: {response.text}")    