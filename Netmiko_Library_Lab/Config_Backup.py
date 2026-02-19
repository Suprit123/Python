from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

os = "cisco_ios"
R1 = "172.16.166.131"
R2 = "172.16.166.132"
username = input("enter your username: ")
password = getpass("enter your password: ")

# Defining device details.

routers = [
    {"device_type": os, "ip": R1, "username": username, "password": password},
    {"device_type": os, "ip": R2, "username": username, "password": password},
]

# Get the current date and time for the file naming
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Now we need to loop through each router and backup the configuration.
for router in routers:
    try:
        print(f'=== Connecting to {router["ip"]} ===\n')
        connection = ConnectHandler(**router)

        print(f'Successfully connected to {router["ip"]}...')
        print("Getting the interface brief.")

        # Here we are going to get the output of show ip int brief
        output = connection.send_command("show ip int brief")
        print(output)

        # Create a filename based on the router's IP and timestamp.
        filename = f'{router["ip"]}_backup_{timestamp}.txt'

        # Write the output and saves to the file
        with open(filename, "w") as file:
            file.write(output)

        print(f'backup of {router["ip"]} save to {filename}\n')

        connection.disconnect()

    # Error Handling
    except Exception as e:
        print(f'failed to backup {router["ip"]}: {e}')
