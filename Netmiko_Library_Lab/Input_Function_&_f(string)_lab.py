from netmiko import ConnectHandler

R1 = "172.16.166.129"
# Here we are making the use of input function. Where we are manully inserting the values for variables that are been created.
username = input("Enter the username: ")
password = input("Enter the password: ")


device_details = {
    "device_type": "cisco_ios",
    "username": username,
    "password": password,
    "ip": R1,
}


ssh = ConnectHandler(**device_details)
print("SSH connection done!")

int_name = input("Enter the interface name: ")
int_ip = input("Enter the interface IP: ")
int_mask = input("Enter the interface mask: ")
int_des = input("Enter the interface description: ")

# The f string allows to format selected parts of a string. To specify a string as an f-string, simply put an f in front of the string.
commands = [
    f"interface {int_name}",
    f"description {int_des}",
    f"ip address {int_ip} {int_mask}",
    "no shut",
]

int_config = ssh.send_config_set(commands)
print(int_config)

int_detials = ssh.send_command("Show ip int brief")
print(int_detials)

ssh.disconnect()
