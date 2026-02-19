from netmiko import ConnectHandler
from getpass import getpass

# Define the router OS version
os_version = "cisco_ios"

R1 = "172.16.166.131"
R2 = "172.16.166.132"
R3 = "172.16.166.129"

devices = [R1, R2, R3]

# Loop through each device
for routers in devices:
    # Define the device parameters. Here we are using username and password inside for loop as we have different username and password for each device.
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    device_details = {
        "device_type": os_version,
        "ip": routers,
        "username": username,
        "password": password,
    }

    # Connect to the device
    connect_to_routers = ConnectHandler(**device_details)
    print(f"Connected to {routers} successfully...!")

    user_input = int(input("enter the number of interface to be configured: "))

    for interface in range(user_input):
        int_name = input("enter the interface name (e.g. , Loopback1): ")
        int_ip = input("enter the ip add of interface: ")
        int_mask = input("enter the subnet mask for ip give: ")
        int_des = input("enter the desc to the interface: ")

        commands = [
            f"interface {int_name}",
            f"ip add {int_ip} {int_mask}",
            f"desc {int_des}",
            "no shut",
        ]

        send_config = connect_to_routers.send_config_set(commands)
        print(f"configured {int_name} on {routers} with {int_ip}")

        output = connect_to_routers.send_command(
            input("enter the command you for which you need the output: ")
        )
        print(output)

    connect_to_routers.disconnect()
