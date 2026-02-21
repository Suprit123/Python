from netmiko import ConnectHandler
from getpass import getpass

# Using a dictionary to store the hostname and ip address of the device
router_dict = {"R1": "172.16.166.131"}

# Commands to be send to the device
commands = [
    "show ip int brief",
    "show ip route",
    "show version",
]

# Use for loop with the items() method to iterate through the router_dict and get the hostname and ip add of each router
for r_name, r_rip in router_dict.items():
    print(f"=== Successfully connected to '{r_name}' === \n")

    # Get the username and password. Using the input() function to get the username from the user and getpass() function to get the password
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Connect to the device and send the commands
    ssh = ConnectHandler(
        device_type="cisco_ios",
        host=r_rip,
        username=username,
        password=password,
    )

    # Use for loop as we have multiple commands to send and print the output
    for c in commands:
        show_output = ssh.send_command(c)
        # Print the output of the commands with the command name for better readability
        print(f'=== Output of "{c}" ===\n{show_output}\n')
        # Print a new line for better readability
        print("\n")
    # Disconnect from the device
    ssh.disconnect()
