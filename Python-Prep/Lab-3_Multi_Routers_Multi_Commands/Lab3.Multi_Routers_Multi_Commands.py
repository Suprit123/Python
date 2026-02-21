# Import netmiko library
from netmiko import ConnectHandler

# Import getpass library to securely get the password
from getpass import getpass

# Dictionary of the routers with their hostnames and ip addresses

# Dictionary of the routers with their hostnames and ip addresses
router_dict = {
    "R1": "172.16.166.129",
    "R2": "172.16.166.131",
}

# List of commands to be sent to the routers
commands = [
    "show ip int brief",
    "show version",
    "show banner login",
]


# Use a for loop with the items() method to iterate through the router_dict and get the hostname and ip add of each router
for r_name, r_ip in router_dict.items():
    print(f"=== Successfully connected to '{r_name}' === \n")

    # Get the username and password. Using the input() function to get the username from the user and getpass() function to get the password
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Create ssh connection to the routers
    ssh = ConnectHandler(
        device_type="cisco_ios",
        host=r_ip,
        username=username,
        password=password,
    )

    # Using the nested for loop to send the commands to the routers and print the output of the commands
    for c in commands:
        show_output = ssh.send_command(c)
        print(f'=== Output of "{c}" ===\n{show_output}\n')
        print("\n")

# Disconnect the ssh connection to the routers
ssh.disconnect()
