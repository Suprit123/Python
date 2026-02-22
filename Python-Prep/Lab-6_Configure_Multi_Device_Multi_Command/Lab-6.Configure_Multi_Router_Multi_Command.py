from netmiko import ConnectHandler

from getpass import getpass

# Define device dictionary
router_dict = {
    "R1": "172.16.166.129",
    "R2": "172.16.166.131",
}

# Commands to be sent to the each device
r1_commands = [
    "interface gigabitEthernet 0/1",
    "ip address 192.168.1.1 255.255.255.0",
    "no shutdown",
    "exit",
    "interface GigabitEthernet 0/2",
    "ip address 10.10.10.1 255.255.255.0",
    "no shutdown",
    "exit",
]

r2_commands = [
    "interface gigabitEthernet 0/1",
    "ip address 192.168.2.1 255.255.255.0",
    "no shutdown",
    "exit",
    "interface GigabitEthernet 0/2",
    "ip address 10.10.20.1 255.255.255.0",
    "no shutdown",
    "exit",
]

show_commands = [
    "show ip int brief",
    "show run int gigabitEthernet 0/1",
    "show run int gigabitEthernet 0/2",
]

# Map the commands to the devices so that we can use the device name to get the list of commands for the device
commands_dict = {"R1": r1_commands, "R2": r2_commands}

# Loop through the devices and send the commands
for r_name, r_ip in router_dict.items():
    print(f" === Connection to {r_name} with IP {r_ip} is successful ===\n")

    # Create an ssh connection to the device
    ssh = ConnectHandler(
        device_type="cisco_ios",
        host=r_ip,
        username=input("Enter your SSH username: "),
        password=getpass("Enter your SSH password:"),
    )
    print(f" === Pushing the configuration to {r_name} with IP {r_ip} ===\n")
    # Send commands to the device. Here using commands_dict[->r_name] to get the list of commands for the device
    output = ssh.send_config_set(commands_dict[r_name])
    print(output)

    # Send show commands to the device
    print(f" === Sending show commands to {r_name} ===\n")
    for s in show_commands:
        output = ssh.send_command(s)
        print(f" ==== Output of {s} on {r_name} ===\n{output}\n")

    # Close the connection ssh.disconnect()
    ssh.disconnect()
    print(f" === Disconnected from {r_name} ===\n")
