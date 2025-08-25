from netmiko import ConnectHandler
from getpass import getpass

device_ip = "172.16.166.131"
device_ios = "cisco_ios"
username = input("enter your username: ")
password = getpass("enter you password: ")

device_details = {
    "ip": device_ip,
    "username": username,
    "password": password,
    "device_type": device_ios,
}

ssh = ConnectHandler(**device_details)
print("connection eastablished...!")

# Here we are going to ask the user what he needs to configure as a routing protocol using input() function

user_input = int(
    input(
        """which routing protocol you wish to configure?
                       1. static routing
                       2. eigrp
                       3. ospf
                       please make a choise (1/2/3): """
    )
)

# Now we will define what to do if user selects the option number 1 i.e. Static Routing.

if user_input == 1:
    print("you have selectd static routing. \nPlease provide the information below")
    user_input1 = int(
        input("enter the number of static routes you wish to configure: ")
    )

    for static_routes in range(user_input1):

        nw_id = input("enter the network id: ")
        mask = input("enter the network mask: ")
        next_hop = input("enter the next hop add: ")

        commands = [f"ip route {nw_id} {mask} {next_hop}"]
        static_config = ssh.send_config_set(commands)
        print(static_config)

    output_details = ssh.send_command("show ip route")
    print(output_details)

# Here we are adding the details for option 2 eigrp:
elif user_input == 2:
    print("you have selected eigrp. \nPlease provide the below function")

    # The below commands will be entered only once hence they are out of the for loop statement
    eigrp_as = input("enter the as number: ")
    eigrp_networks = int(input("enter the number of network you wish to configure: "))

    # Here we are calling the number of eigrp network we want configure
    for eirp in range(eigrp_networks):
        nw_id = input("enter the network id: ")
        wc_mask = input("enter the wildcard mask: ")

        commands = [f"router eigrp {eigrp_as}", f"network {nw_id} {wc_mask}"]
        eigrp_config = ssh.send_config_set(commands)
        print(eigrp_config)

    eigrp_detail = ssh.send_command("show eigrp protocols")
    print(f"=== printing the output of {eigrp_detail} ====")

    # Here we are adding the details of option 3 ospf:
elif user_input == 3:
    print("you have selecte3d ospf..\nPlease provide the below details: ")

    # The below commands will be entered only once hence they are out of the for loop statement
    ospf_id = input("enter the is proccess id: ")
    ospf_networks = int(input("enter the number of network you want to confiure: "))
    router_id = input("enter the router id: ")

    # Here we are calling the ospf networks
    for ospf in range(ospf_networks):

        nw_id = input("enter the network id: ")
        wc_mask = input("enter the wc mask: ")

        commands = [f"router ospf {ospf_id}", f"network {nw_id} {wc_mask}"]
        ospf_config = ssh.send_config_set(commands)
        print(ospf_config)

    ospf_output = ssh.send_command("show ip ospf")
    print(f"\nprinting the output of {ospf_output}\n")

else:
    print("Invalid input detected. Please use the correct option.")

ssh.disconnect()
