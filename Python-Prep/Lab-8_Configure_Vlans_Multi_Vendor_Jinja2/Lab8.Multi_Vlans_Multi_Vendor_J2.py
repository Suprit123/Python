from netmiko import ConnectHandler
from getpass import getpass

# import the jinja2 template library
from jinja2 import Environment, FileSystemLoader

# import yaml library to read the yaml file
import yaml

# Load the templates folder from the templates directory
env = Environment(loader=FileSystemLoader("templates"))

# Map each vendor to its own yaml file and jinja2 template
files = {
    "cisco_ios": {"yaml": "cisco_vlans.yaml", "template_file": "cisco_vlans.j2"},
    "arista_eos": {"yaml": "arista_vlans.yaml", "template_file": "arista_vlans.j2"},
}

# Device dictionary to get the hostname, ip and vendor
device_dict = {
    "S1": {"ip": "172.16.166.133", "vendor": "cisco_ios"},
    "VEOS1": {"ip": "172.16.166.132", "vendor": "arista_eos"},
}

# Loop throguh each device
for r_name, r_ip in device_dict.items():
    print(f"=== Connection to {r_name} {r_ip['ip']} ===\n")

    # Prompt for username and and password
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Load the yaml file for the device
    with open(files[r_ip["vendor"]]["yaml"]) as f:
        vlans = yaml.safe_load(f)

    # Render the jinja2 template with the vlan from the yaml file
    template = env.get_template(files[r_ip["vendor"]]["template_file"])

    # Render the template with the vlan data from the yaml file
    config = template.render(vlans=vlans["vlans"])
    print(f"=== Config to be sent to {r_name} ===\n{config}\n")

    # Create ssh connection to the device
    ssh = ConnectHandler(
        device_type=r_ip["vendor"],
        host=r_ip["ip"],
        username=username,
        password=password,
    )

    # Enter the enable mode if not already in it (Needed for Arista)
    if not ssh.check_enable_mode():
        ssh.enable()

    # Send the rendered config to the device
    vlan_config = ssh.send_config_set(config.splitlines())
    print(f"=== Output from {r_name} ===\n{vlan_config}\n")

    # Verify the configuration on the devices
    if r_ip["vendor"] == "cisco_ios":
        output = ssh.send_command("show vlan brief")
        print(f"=== VLANs on {r_name} ===\n{output}\n")
    else:
        output = ssh.send_command("show vlan")
        print(f"=== VLANs on {r_name} ===\n{output}\n")
