from netmiko import ConnectHandler

R1 = {
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "cisco",
    "ip": "192.168.249.129",
}

R1 = ConnectHandler(**R1)
print("ssh connection eastablished")

commands = [
    "interface loopback1",
    "ip add 1.1.1.1 255.255.255.255",
    "description configured via python",
]

send_to_R1 = R1.send_config_set(commands)
print(send_to_R1)

show = R1.send_command("show ip int brief")
print(show)

R1.save_config()
R1.disconnect
