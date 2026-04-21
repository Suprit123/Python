# import the requests library to make HTTP requests
import requests

# import the request.auth library to handle authentication
from requests.auth import HTTPBasicAuth

# import the getpass library to securely get the password from the user
from getpass import getpass

# Define the URL to connect to the RESTCONF API endpoint for fetching interface information
api_url = "https://192.168.42.129/restconf/data/ietf-interfaces:interfaces"
print(f"Connecting to {api_url} to fetch interface information...")

# Use the creads to login to the devices
creds = HTTPBasicAuth(username = "admin", password = getpass("Enter your password: "))


# Create the header variable to specify the content type and accept type for the RESTCONF API
headers = {
    "Accept": "application/yang-data+json", 
}

# Use the get.request method to send the GET request to the specified URL with the provided credentials and headers
response = requests.get(url = api_url, auth = creds, headers = headers, verify = False)

# Print the response in text format and status code to check if the request was successful
print(response.text)
print(f"Status Code: {response.status_code}")
