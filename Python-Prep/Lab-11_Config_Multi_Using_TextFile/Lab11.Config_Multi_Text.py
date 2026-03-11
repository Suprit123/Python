from netmiko import ConnectHandler
import os
from getpass import getpass

# Define the config folder path from the directory
folder = "Config_Folder"

# Device Info
devices = {
    "Cisco": {
        "device_type": "cisco_ios",
        "ip": "172.16.166.129",
        "config_file": "cisco.txt",
    },
    "Arista": {
        "device_type": "arista_eos",
        "ip": "172.16.166.132",
        "config_file": "arista.txt",
    },
}

# Loop through the routers
for r_name, r_ip in devices.items():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    print(f"=== Connection to {r_name} ({r_ip['ip']})is successfull ===: ")

    # Define the full path to the config file in "Config_Folder"
    config_path = os.path.join(folder, r_ip["config_file"])

    # Check if the config file is present
    if not os.path.exists(config_path):
        print(f"Config File not found: {config_path}")
        continue

    # Read the configurations commands and split them into individual CLI command lines
    with open(config_path, "r") as f:
        config_line = f.read().splitlines()

    try:
        ssh = ConnectHandler(
            device_type=r_ip["device_type"],
            ip=r_ip["ip"],
            username=username,
            password=password,
        )

        print(f"Connected to {r_name}. Send Config: ")

        # Enter in enable mode if not alredy in it (Arista device)
        if not ssh.check_enable_mode():
            ssh.enable()

        # Send config to the devices
        output = ssh.send_config_set(config_line)
        print(f"Configuration output for {r_name}:\n {output}")

    except Exception as e:
        print(f"Error connecting to {r_name}: {e}")
