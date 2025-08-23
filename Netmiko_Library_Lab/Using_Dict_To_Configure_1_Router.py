from netmiko import ConnectHandler
from getpass import getpass

os_version = "cisco_ios"
username = input("enter your username: ")
password = getpass("enter your password: ")

routers = {"r1": "172.16.166.131", "r2": "172.16.166.132", "r3": "172.16.166.129"}

user_choice = input("enter the router name that you want to confiugre: ").lower()

# Here we are calling the above input function to fetch the dictonary keys.
router_ip = routers[user_choice]
print(f"connection initiated with {router_ip}")


router_details = {
    "device_type": os_version,
    "username": username,
    "password": password,
    "ip": router_ip,
}

connect_to_device = ConnectHandler(**router_details)
print(f"ssh connection eastablished with {router_ip} successfully..!")

user_input = int(input("enter the number of interface you want to configure: "))

for interfaces in range(user_input):

    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the interface ip add: ")
    int_mask = input("Enter the maks: ")
    int_des = input("Enter the description: ")

    commands = [
        f"intface {int_name}",
        f"ip add {int_ip} {int_mask}",
        f"desc {int_des}",
        "no shut",
    ]

    send_config = connect_to_device.send_config_set(commands)
    print(send_config)

output = connect_to_device.send_command(
    input("enter the command for which you want to see the outout: ")
)

print(output)

connect_to_device.disconnect()
