# Import the request library to make HTTP request
import requests

# Import the request.auth library to handle authentication
from requests.auth import HTTPBasicAuth

# Import getpass
from getpass import getpass

# import json library to handle json data
import json

# Device details
device = {
    "R1": "192.168.42.129",
    "R2": "192.168.42.130"
}

# Create a loop to connect to each
for r_name, r_ip in device.items():
    # Defind the URL to connect to the restconf API endpoint for fetching int info
    get = f"https://{r_ip}/restconf/data/ietf-interfaces:interfaces"
    print(f"Connecting to {r_name} at {r_ip} to fetch interface information...")
    
    # Use the creds to login into the devices
    creds = HTTPBasicAuth(username = "admin", password = getpass(f"Enter your password for {r_name}: "))
    
    # Create the header
    headers = {
        "Accept": "application/yang-data+json",
    }
    
    # Use the get.request method to send the GET request to the specified URL with the provided credentials and headers
    response = requests.get(url = get, auth = creds, headers = headers, verify = False)
    
    # Print the response in text format and status code to check if the request was successful
    print(response.text)
    print(f"Status Code: {response.status_code}")