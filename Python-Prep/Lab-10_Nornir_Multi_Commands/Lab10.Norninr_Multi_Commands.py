# Import the nornin library
from nornir import InitNornir

# Import the netmiko_send_command task
from nornir_netmiko.tasks import netmiko_send_command

# Import nornir print reult library
from nornir_utils.plugins.functions import print_result

# Getpass library
from getpass import getpass

# Initialize nornir with inventory files with threaded plugin and simpleinventory plugin from the config.yaml file
init = InitNornir(config_file="config.yaml")

# Ask for the username and password
init.inventory.defaults.username = input("Enter your username: ")
init.inventory.defaults.password = getpass("Enter your password: ")


# Defining the task for send_command
def send_command(task):

    # Push the commands based on the device platform using the if-else function
    if task.host.platform == "cisco_ios":
        commands = ["show ip int brief", "show ip arp"]
    else:
        commands = ["show mac address-table", "show ip route"]

    print(f"\n === Connecting to {task.host.name} ({task.host.platform}) ===")

    # Loop through the commands and use try and except for error handling
    for cmd in commands:
        try:
            # Send the nornir netmiko send_coammnd task
            result = task.run(task=netmiko_send_command, command_string=cmd)
            print(f'\n Output of "{cmd}" on {task.host.name}:')
            print(result.result)
        except Exception as e:
            print(f"[ERROR] Failed to run '{cmd}'on {task.host.name}: {e}")


# Execute the task against all hosts in the inventory (num_workers=1 for sequential execution)
init.run(task=send_command)
