from netmiko import ConnectHandler
from getpass import getpass

# Device Paramaters
R1 = {
    "device_type": "cisco_ios",
    "host": "172.16.166.129",
    "username": "admin",
    "password": getpass(),
}

# Commands to be send to the device
commands = [
    "show ip int brief",
    "show ip route",
    "show version",
]

# Connect to the device and send the commands
ssh = ConnectHandler(**R1)
print(f'=== Successfully connected to {R1["host"]} ===\n')

# Use for loop as we have multiple commands to send and print the output
for c in commands:
    show_output = ssh.send_command(c)
    # Print the output of the commands with the command name for better readability
    print(f'=== Output of "{c}" ===\n{show_output}\n')
    # Print a new line for better readability
    print("\n")
# Disconnect from the device
ssh.disconnect()
