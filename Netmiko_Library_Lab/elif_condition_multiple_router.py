from netmiko import ConnectHandler
from getpass import getpass

R1 = "172.16.166.131"
R2 = "172.16.166.132"
device_ios = "cisco_ios"


# We create a list of router. Each element is a dictionary with details of one router: its IP and the fact it's running cisco IOS.
routers_detail = [
    {"ip": R1, "device_type": device_ios},
    {"ip": R2, "device_type": device_ios},
]

# Get the login details (same for both the routers)
username = input("enter your username: ")
password = getpass("enter your password: ")

# Loop through routers. We start a loop to go through each router from the routers_detail list above.
for routers in routers_detail:
    # For each router, we build a device_details dictionary.
    # Fetching the router's ip "ip" from the routers_detail list. Also same for device_type.
    device_details = {
        "ip": routers["ip"],
        "username": username,
        "password": password,
        "device_type": routers["device_type"],
    }
    # Printing which router we're connecting
    print(f"\n=== Connecting to {routers['ip']} ===\n")

    ssh = ConnectHandler(**device_details)
    print("Connection established ...!")

    # Ask the user what to configure.
    user_input = int(
        input(
            """Which configuration do you want to confgiure?
                           1. Interface Config
                           2. Static Routing Config
                           Please make a choice (1/2): """
        )
    )

    # Configuration for interface configuration
    if user_input == 1:
        print(
            "You have selected Interface config. \nPlease provide the below information: "
        )
        interface = int(
            input("Enter the number of interfaces you which to configure: ")
        )
        # Adding a loop for interface config
        for interface_config in range(interface):
            int_name = input("Enter the interface name (e.g.,GigabitEthernet0/0 ): ")
            int_ip = input("Enter the intface ip address: ")
            int_mask = input("Enter the subnet mask: ")

            commands = [
                f"interface {int_name}",
                f"ip add {int_ip} {int_mask}",
                "no shutdown",
            ]
            int_config = ssh.send_config_set(commands)
            print(int_config)

        int_output = ssh.send_command("show ip int brief")
        print(f"===\nPrinting the output of {int_output} ===")

        # Here we are adding the static routing details.
    elif user_input == 2:
        print("You have selected Static Routing.\nPlease provide the details below: ")

        static_routes = int(
            input("Enter the number of static routes you want to configure: ")
        )

        for static in range(static_routes):
            nw_id = input("Enter the network id: ")
            mask = input("Enter the network mask: ")
            next_hop = input("Enter the next hop: ")

            commands = [f"ip route {nw_id} {mask} {next_hop}"]

            static_config = ssh.send_config_set(commands)
            print(static_config)

        static_output = ssh.send_command("show ip route")
        print(static_output)

    else:
        print("Invalid input detected. Please use the correct option (1/2): ")

    ssh.disconnect()
