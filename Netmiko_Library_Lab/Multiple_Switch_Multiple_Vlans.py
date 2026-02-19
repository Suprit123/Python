from netmiko import ConnectHandler
from getpass import getpass

# Define the device OS
device_ios = "cisco_ios"

# IP addresses of the two cisco switches to be configured.
S1 = "172.16.166.134"
S2 = "172.16.166.135"

# List of switches to loop through for configuration
switch_ip_list = [S1, S2]

# Loop through each switch in the list.
for switch_ip in switch_ip_list:

    # Collect the connection paramaters fro the current switch.
    connection_paramaters = {
        "device_type": device_ios,
        "username": "admin",
        "password": getpass("Enter your password: "),
        "ip": switch_ip,
    }

    # Establish and SSH connection using Netmiko.
    netmiko_connection = ConnectHandler(**connection_paramaters)
    print(f"\n=== Successfully Connected to {switch_ip} ===\n")

    # Ask user how many VLAN they wish to configure on this switch.
    user_choice = int(input("Enter the number of vlan you want to configure: "))

    # Loop to configure each vlan.
    for vlans in range(user_choice):

        # Collect VLAN details from the user.
        vlan_id = input("Enter the VLAN ID: ")
        vlan_name = input("Enter the VLAN name: ")

        # Create VLAN configuration commands.
        vlan_commands = [f"vlan {vlan_id}", f"name {vlan_name}"]

        # Send VLAN configuration to switch.
        vlan_config = netmiko_connection.send_config_set(vlan_commands)
        print(f"Configure {vlan_id} on {switch_ip} with name {vlan_name}")

        # Display VLAN configuration after applying changes.
        vlan_output = netmiko_connection.send_command("Show vlan")
        print(vlan_output)

    # Close the SSH connection to the current switch.
    netmiko_connection.disconnect()
