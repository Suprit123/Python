from netmiko import ConnectHandler
from getpass import getpass

# Create router dictionary to ip address and hostname of the devices.
router_dict = {"R1": "172.16.166.129"}


# Group commands for each interface
commands = [
    ["interface loopback 1", "ip address 2.2.2.2 255.255.255.255", "exit"],
    [
        "interface GigabitEthernet 0/1",
        "ip address 10.10.10.1 255.255.255.0",
        "no shutdown",
        "exit",
    ],
]

show_commands = ["show ip int brief", "show run int gigabitEthernet 0/1"]


# Create a for loop to connect to the devices using item() to get the key and value fron the router_dict
for r_name, r_ip in router_dict.items():
    print(f" === Connection to {r_name} with IP {r_ip} is successful ===\n")

# Create an ssh connection to the device
ssh = ConnectHandler(
    device_type="cisco_ios",
    host=r_ip,
    username=input("Enter your SSH username: "),
    password=getpass("Enter your SSH password: "),
)


# Send show commands to the device to verify the configuration
for c in commands:
    output = ssh.send_config_set(c)
    print(output)

# Verify the configuration be send the show command to the device
for s in show_commands:
    output = ssh.send_command(s)
    print(f" === Output of {s} on {r_name} ===\n{output}\n")

# Disconnect the ssh connection to the device
ssh.disconnect()
print(f" === SSH connection to {r_name} with IP {r_ip} is disconnected ===")
