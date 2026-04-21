# impor the request library
import requests

# import the request.auth library
from requests.auth import HTTPBasicAuth

# Import the getpass
from getpass import getpass

# Define the routers details with IP
routers = {
    "R1": "192.168.42.129",
    "R2": "192.168.42.130"
}

# Create a for loop to iterate over the routers
for r_name, r_ip in routers.items():
    
    # Define the URL for the restoconf endpoint
    get = f"https://{r_ip}/restconf/data/Cisco-IOS-XE-native:native"
    print(f"Connecting to {r_name} at {r_ip} to fetch configuration information...")
    
    # Define the creds to the devices
    creds = HTTPBasicAuth(username = "admin", password = getpass(f"Enter your password for {r_name}: "))
    
    # Define the header
    headers = {
        "Accept": "application/yang-data+json",
    }
    
    # Use the get.request method to send the GET request to the specified URL with the provided credentials and headers
    response = requests.get(url = get, auth = creds, headers = headers, verify = False)
    
    # use the if else statement to check if the request was successful and print the response in text format and status code
    if response.status_code == 200:
        print(f"Successfully connected to {r_name} at {r_ip} and fetched configuration information.")
        print(response.text)
    else:
        print(f"Failed to connect to {r_name} at {r_ip} and fetch configuration information. Status Code: {response.status_code}")