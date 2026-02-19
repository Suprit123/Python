# Importing ConnectHandler from Netmiko to handle SSH connections to network devices
from netmiko import ConnectHandler

# Importing getpass to securely input passwords without showing them on the screen
from getpass import getpass

# Prompting user for login credentials
username = input("Enter your username: ")
password = getpass("Enter your password: ")  # Securely handle password input

# Defining IP addresses of Cisco routers we want to connect to
router1_ip = "172.16.166.131"
router2_ip = "172.16.166.132"
router3_ip = "172.16.166.129"

# Storing all router IPs in a list to loop through them later
router_ip_list = [router1_ip, router2_ip, router3_ip]

# Loop through each router's IP to establish a connection and configure interfaces
for router_ip in router_ip_list:
    # Creating a dictionary with connection parameters for Netmiko
    device_params = {
        "device_type": "cisco_ios",  # Define the platform (Cisco IOS)
        "ip": router_ip,  # IP of the current router
        "username": username,  # Username input by user
        "password": password,  # Password input by user
    }

    # Establish SSH connection to the router using Netmiko
    ssh_connection = ConnectHandler(**device_params)
    print(f"✅ Connected to {router_ip} successfully!")

    # Ask user how many interfaces they want to configure on this router
    interface_count = int(
        input("Enter the number of interfaces that you want to configure: ")
    )

    # Loop through the number of interfaces to configure each one
    for _ in range(interface_count):
        # Collect interface configuration details from user
        interface_name = input("Enter the interface name (e.g., GigabitEthernet0/0): ")
        interface_ip = input("Enter the IP address for the interface: ")
        subnet_mask = input("Enter the subnet mask (e.g., 255.255.255.0): ")
        description = input("Enter the interface description: ")

        # Create a list of commands to send to the router
        config_commands = [
            f"interface {interface_name}",
            f"ip address {interface_ip} {subnet_mask}",
            f"description {description}",
        ]

        # Send configuration commands to the router
        ssh_connection.send_config_set(config_commands)
        print(f"🛠️ Configured {interface_name} on {router_ip} with IP {interface_ip}")

        # Ask the user for a show or verification command to execute
        verification_command = input(
            "Enter a command to execute (e.g., show ip int brief): "
        )
        command_output = ssh_connection.send_command(verification_command)

        # Print the output of the command
        print("📄 Command Output:")
        print(command_output)

    # Close SSH connection after configuration
    ssh_connection.disconnect()
    print(f"🔌 Disconnected from {router_ip}\n")
