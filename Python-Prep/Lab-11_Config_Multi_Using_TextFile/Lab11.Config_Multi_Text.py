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

commands = ["show ip int brief", "show ip bgp summary"]

# Loop through the routers
for r_name, r_ip in devices.items():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    print(f"=== Connection to {r_name} ({r_ip['ip']}) is successfull ===: ")

    # Define the full path to the config file in "Config_Folder"
    config_path = os.path.join(folder, r_ip["config_file"])

    # Check if the config file is present
    if not os.path.exists(config_path):
        print(f"Config File not found: {config_path}")
        continue

    # Read the configurations commands and split them into individual CLI command lines and ingore the # comments from the text file
    with open(config_path, "r") as f:
        config_line = [
            line.strip()
            for line in f.readlines()
            if line.strip() and not line.strip().startswith("#")
        ]

    try:
        ssh = ConnectHandler(
            device_type=r_ip["device_type"],
            ip=r_ip["ip"],
            username=username,
            password=password,
            global_delay_factor=2,
        )

        print(f"Connected to {r_name}. Send Config: ")

        # Enter in enable mode if not alredy in it (Arista device)
        if not ssh.check_enable_mode():
            ssh.enable()

        # Send config to the devices
        push_config = ssh.send_config_set(config_line)
        print(f"Configuration output for {r_name}:\n {push_config}")

        # Verify the configuration of the devices.
        for c in commands:
            output = ssh.send_command(c)
            print(f"\n=== {c} output for {r_name} ===")
            print(output)
            print("===\n")

    except Exception as e:
        print(f"Error connecting to {r_name}: {e}")
