# In netmiko library we have a ConnectHandler class that allows us to connect to network devices
from netmiko import ConnectHandler

# Below four key values in the dictionary are required to establish a connection to the routers.
R1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.249.129",
    "username": "admin",
    "password": "cisco",
}

# Here we establish a connection to R1 by calling the ConnectHandler class to connect with R1 router. We use (**before the dictionary unpacking)
Connection_to_R1 = ConnectHandler(**R1)

# We create a list of commands that needs to go into the router into the global config mode.
commands_to_R1 = list(
    (
        "interface loopback10",
        "ip add 10.10.10.10 255.255.255.255",
        "description configured via python netmiko",
    )
)

# Send the configuration commands to the router. Here we call the name of the ConnectHandler class from line 13.
int_config = Connection_to_R1.send_config_set(commands_to_R1)
# Print the output of the configuration commands
print(int_config)

# Show the interface status. Here we call the name of the ConnectHandler class from line 13.
int_show = Connection_to_R1.send_command("show ip int brief")
# Print the output of the show command
print(int_show)

# Save the configuration
Connection_to_R1.save_config()
# Disconnect from the router
Connection_to_R1.disconnect()
