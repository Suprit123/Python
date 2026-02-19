# Import the netmiko library to establish SSH connections to network device
from netmiko import ConnectHandler

# Import getpass library to securely get the password input from the user
from getpass import getpass

# Device parameters for single cisco router
R1 = {
    "device_type": "cisco_ios",
    "host": "172.16.166.129",
    "username": "admin",
    "password": getpass(),
}

# Establish ssh connection to the device
ssh = ConnectHandler(**R1)
print(f"=== Successfully connected to {R1['host']} ===\n")

# Send show commands to the device and print the output
show_output = ssh.send_command("show ip int brief")
print(f"Output of 'show ip int brief':\n{show_output}")
