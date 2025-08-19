from netmiko import ConnectHandler

# Here we are using the getpass library to securely handle passwords
from getpass import getpass


username = input("Enter your username: ")
# Here we call the getpass library to securely handle the password input
password = getpass("Enter your password: ")

# We are creating the variables for the routers.
# R = "172.16.166.129"
R1 = "172.16.166.131"
R2 = "172.16.166.132"
R3 = "172.16.166.129"

# Calling the list of routers
devices = [R1, R2, R3]

# Looping through the list of routers
for routers in devices:
    device_details = {
        "device_type": "cisco_ios",
        "ip": routers,
        "username": username,
        "password": password,
    }

    connect_to_devices = ConnectHandler(**device_details)
    print(f"Connected to {routers} successfully..!!")

    user_input = int(
        input("Enter the number of interfaces that you want to configure: ")
    )

    for interface in range(user_input):
        int_name = input("Enter the interface name (e.g., GigabitEthernet0/0): ")
        ip_address = input("Enter the IP address for the interface: ")
        int_mask = input("Enter the subnet mask (e.g., 255.255.255.0): ")
        int_description = input("Enter the interface description: ")

        commands = [
            f"interface {int_name}",
            f"ip address {ip_address} {int_mask}",
            f"description {int_description}",
        ]

        interface_config = connect_to_devices.send_config_set(commands)
        print(f"Configured {int_name} on {routers} with IP {ip_address}")

        output = connect_to_devices.send_command(input("Enter a command to execute: "))
        print(output)

connect_to_devices.disconnect()
