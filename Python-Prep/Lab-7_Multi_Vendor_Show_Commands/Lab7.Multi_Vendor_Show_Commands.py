from netmiko import ConnectHandler
from getpass import getpass

# Create a router dictionary with their hostname, ip address and vendor information
# Here we are using dictionary of dictionary to store the information about the devices.
# The outer dictionary is used to store the device name as the key and the inner dictionary is used to store the ip address and vendor information of the device.
router_dict = {
    "R1": {"ip": "172.16.166.129", "vendor": "cisco_ios"},
    "vEOS1": {"ip": "172.16.166.132", "vendor": "arista_eos"},
}

# Show commands to be sent to cisco device
cisco_commands = ["show ip int brief", "show version"]

# show command to be sent to arista device
arista_command = ["show mac address-table", "show arp"]

# Loop through the router dictionary and create ssh connection to each device.
for r_name, r_ip in router_dict.items():
    print(f"=== Connecting to {r_name} {r_ip['vendor']} ===\n")

    # Prompt for userand and password to connect to the device.
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    ssh = ConnectHandler(
        device_type=r_ip["vendor"],
        host=r_ip["ip"],
        username=username,
        password=password,
    )
    print(f"=== Successfully connected to {r_name} ===\n")

    # Create a if-else statement to check the vendor of the device and send the commands accordingly.
    if r_ip["vendor"] == "cisco_ios":
        # Now create a for loop to send the show commands to the cisco device and print the output.
        for c in cisco_commands:
            show_output = ssh.send_command(c)
            print(f"Output of '{c}' on {r_name}:\n{show_output}\n")

    else:
        # Now create a for loop to send the show command to the arista device and print the output.
        for c in arista_command:
            show_output = ssh.send_command(c)
            print(f"Output of '{c}' on {r_name}:\n{show_output}\n")
