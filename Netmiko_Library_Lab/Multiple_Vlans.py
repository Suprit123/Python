from netmiko import ConnectHandler
from getpass import getpass

# IP addres of the Cisco Switch
S1 = "172.16.166.134"

# Type of network device being connected.
device_os = "cisco_ios"

# Dictionary holding the device connection parameters.
device_details = {
    "device_type": device_os,
    "username": "admin",
    "password": getpass("enter your password: "),
    "ip": S1,
}
# Establish SSH connection to the Cisco switch using Netmiko.
netmiko_connection = ConnectHandler(**device_details)
print("Connection eastablished successfully...!")

# Ask user for the number of VLANs they want to configure.
vlan_count = int(input("enter the number of vlan you wish to configure: "))

# Loop through the number of VLANs to configure each one.
for vlans in range(vlan_count):

    # Ask user for VLAN ID and VLAN name.
    vlan_id = input("Enter the vlan id (e.g., 1): ")
    vlan_name = input("Enter the vlan name: ")

    # Prepare the list of configuration commands for the VLAN.
    vlan_commands = [f"vlan {vlan_id}", f"name {vlan_name}"]

    # Send the VLAN configuration commands to the switch.
    vlan_config = netmiko_connection.send_config_set(vlan_commands)
    print(f"\nVlan {vlan_id} configured with name {vlan_name}")

# After the configuration, retrive and display the VLAN configuration on the switch.
vlan_output = netmiko_connection.send_command("show vlan")
print(vlan_output)

# Disconnect the SSH connection.
netmiko_connection.disconnect()
