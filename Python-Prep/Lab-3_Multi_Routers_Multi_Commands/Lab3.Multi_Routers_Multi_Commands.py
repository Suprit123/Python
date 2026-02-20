# Import netmiko library
from netmiko import ConnectHandler

# Import getpass library to securely get the password
from getpass import getpass

# Device hostname and ip address
R1 = "172.16.166.129"
R2 = "172.16.166.131"

router_list = [R1, R2]

# List of commands to be sent to the routers
commands = [
    "show ip int brief",
    "show version",
    "show banner login",
]


# Use for loop to connect to the routers as we have the list of routers in router_list
for r in router_list:
    # Get the username and password. Using the input() function to get the username from the user and getpass() function to get the password
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    # Create ssh connection to the routers
    ssh = ConnectHandler(
        device_type="cisco_ios",
        host=r,
        username=username,
        password=password,
    )
    print(f"=== Successfully connected to '{r}' === \n")

    # Using the nested for loop to send the commands to the routers and print the output of the commands
    for c in commands:
        show_output = ssh.send_command(c)
        print(f'=== Output of "{c}" ===\n{show_output}\n')
        print("\n")

# Disconnect the ssh connection to the routers
ssh.disconnect()
