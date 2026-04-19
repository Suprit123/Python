# import netmiko library
from netmiko import ConnectHandler

# Import getpass
from getpass import getpass

# Create a dictionary for device information

routers = {
    "R1": "192.168.42.129",
    "R2": "192.168.42.130"
}

# Create a loop to connect to each device
for r_name,r_ip in routers.items():
    print(f" === Connecting to {r_name} with IP {r_ip} === ")
    # Create a dictionary for device information
    device = {
        "device_type": "cisco_ios",
        "host": r_ip,
        "username": input("Enter your username: "),
        "password": getpass("Enter your password: "),
    }

    # Connect to the device using ConnectHandler
    with ConnectHandler(**device) as connect:

        # check if Netconf is enabled
        show = connect.send_command("show run | i netconf")
        if "netconf" in show:
            print(f"Netconf is enabled on {r_name}")
        else:
            print(f"Netconf is not enabled on {r_name}")
            print(f"Enabling Netconf on {r_name}: ")

            # Enable Netconf
            connect.send_config_set(["netconf-yang", "netconf-ssh"])

            # Verify Netconf is enabled
            verify = connect.send_command("show run | i netconf")
            if "netconf" in verify:
                print(f"Netconf is now enabled on {r_name}")