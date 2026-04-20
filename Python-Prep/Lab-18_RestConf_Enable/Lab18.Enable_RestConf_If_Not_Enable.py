# Import the Netmiko library
from netmiko import ConnectHandler

# Import getpass
from getpass import getpass

# Create device information dictionary
routers = {
    "R1": {
        "device_type": "cisco_ios",
        "host": "192.168.42.129",
    },
    "R2": {
        "device_type": "cisco_ios",
        "host": "192.168.42.130",
    }
}

# Create a loop to connect to each device
for r_name, r_info in routers.items():
    print (f" === Connecting to {r_name} with IP {r_info['host']} === ")
    # Pass the device info and creds to ConnectHandler
    device = {
        "device_type": r_info["device_type"],
        "host": r_info["host"],
        "username": input("Enter your username: "),
        "password": getpass("Enter your password: "),
    }

    # Connect to the device
    with ConnectHandler(**device) as c:
        # Check if RestConf is enabled
        send = c.send_command("show run | in restconf")
        if "restconf" in send:
            print(f"RestConf is already enable on {r_name}")
        else:
            print(f"RestConf is not enabled on {r_name}, enabling it now: ")
            # Commands to enable RestConf
            config_commands = [
                "ip http server",
                "ip http secure_server",
                "restconf",
            ]
            # Send the Configuration commands to the devices
            c.send_config_set(config_commands)

            # Verify RestConf is enabled
            send = c.send_command(" sh run | i restconf")
            if "restconf" in send:
                print(f"RestConf is now enabled on {r_name}")
            else:
                print(f"RestConf is still not enabled on {r_name}")
                
            # save the configuration
            print(f"Saving the config on {r_name}")
            c.save_config()