from netmiko import ConnectHandler

R1 = "172.16.166.129"
username = input("Enter your username: ")
password = input("Enter your password: ")

device_details = {
    "device_type": "cisco_ios",
    "password": password,
    "username": username,
    "ip": R1,
}

ssh_to_device = ConnectHandler(**device_details)
print("ssh connection eastablished")

# Here we are using int () function because by defualt data collected in input() function is string
user_input = int(input("How many interfaces you want to configure: "))

# We call the user_input varaible in the for loop function
for interface in range(0, user_input):

    int_name = input("enter the interface name: ")
    int_ip = input("enter the interface ip: ")
    int_mask = input("enter the ip mask: ")
    int_des = input("enter the int desc: ")

    commands = [
        f"interface {int_name}",
        f"ip address {int_ip} {int_mask}",
        f"desc {int_des}",
    ]
    int_config = ssh_to_device.send_config_set(commands)
    print(int_config)

    show_output = ssh_to_device.send_command("show ip int brief")
    print(show_output)

# The disconnect function should be outside the loop.
ssh_to_device.disconnect()
