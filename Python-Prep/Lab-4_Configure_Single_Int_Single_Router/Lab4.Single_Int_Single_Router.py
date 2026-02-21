from netmiko import ConnectHandler
from getpass import getpass

# Create a dictionary to hold the hostname and ip address of the router
router_dict = {"R1": "172.16.166.129"}

# Commands to be sent to the router to configure the interface
config_commands = [
    "interface Loopback0",
    "description Configured by Netmiko",
    "ip address 192.168.1.1 255.255.255.255",
    "no shutdown",
]


# Loop through the router dictionary using the items() method to get the hostname and ip address
for r_name, r_ip in router_dict.items():
    print(f"=== Successfully connected to '{r_name} at {r_ip}' === \n")

# Get the username and and password
username = input("Enter your username: ")
password = getpass("Enter your password: ")

# Create ssh connection to the router
ssh = ConnectHandler(
    device_type="cisco_ios",
    host=r_ip,
    username=username,
    password=password,
)

# Send the Configuration to the router using the send_config_set() method and print the output of the configuration commands
int_config = ssh.send_config_set(config_commands)
print(f"=== Output of the configuration commands ===\n{int_config}\n")

# Verify the configuration of the interface using the send_command()
show_int = ssh.send_command("show ip int brief")
print(f"=== Output of 'show ip int brief' ===\n{show_int}\n")

# Save the configuration of the router using the save_config() method
ssh.save_config()
# Disconnect the ssh connection to the router
ssh.disconnect()
