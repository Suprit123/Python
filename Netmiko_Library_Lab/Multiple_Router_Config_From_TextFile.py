from netmiko import ConnectHandler
import os
from getpass import getpass

# =======================
# Define Config Folder Path
# =======================
CONFIG_FOLDER = (
    "Config_Folder"  # Make sure this folder exists in your project directory
)

# Prompt password once (optional improvement if all routers use same creds)
password = getpass("Enter your router password: ")

# =======================
# Define Router Info
# =======================
routers = {
    "router1": {
        "device_type": "cisco_ios",
        "ip": "172.16.166.131",
        "username": "admin",
        "password": password,
        "config_file": "R1_Config.txt",
    },
    "router2": {
        "device_type": "cisco_ios",
        "ip": "172.16.166.132",
        "username": "admin",
        "password": password,
        "config_file": "R2_Config.txt",
    },
}

# =======================
# Loop Through Routers
# =======================
for router_name, details in routers.items():

    print(f"\n Connecting to {router_name} ({details['ip']}):")

    # Build full path to the config file in 'configs' folder
    config_path = os.path.join(CONFIG_FOLDER, details["config_file"])

    # -------------------------------
    # Step 1: Check if config file exists
    # -------------------------------
    if not os.path.exists(config_path):
        print(f"❌ Config file not found: {config_path}")
        continue

    # -------------------------------
    # Step 2: Read configuration commands and split it into individual CLI command lines
    # -------------------------------
    with open(config_path, "r") as f:
        config_lines = f.read().splitlines()

    try:
        # -------------------------------
        # Step 3: SSH to Router
        # -------------------------------
        connection = ConnectHandler(
            device_type=details["device_type"],
            ip=details["ip"],
            username=details["username"],
            password=details["password"],
        )

        print(f"✅ Connected to {router_name}. Sending configuration...")

        # -------------------------------
        # Step 4: Send Config to Device
        # -------------------------------
        output = connection.send_config_set(config_lines)

        print(f"Configuration output for {router_name}:\n{output}")

        # -------------------------------
        # Step 5: Disconnect
        # -------------------------------
        connection.disconnect()
        print(f"Disconnected from {router_name}")

    except Exception as e:
        print(f"Error connecting to {router_name}: {e}")
