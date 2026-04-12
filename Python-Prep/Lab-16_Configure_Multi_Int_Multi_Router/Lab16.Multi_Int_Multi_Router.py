# Import ncclinet library
from logging import config

from ncclient import manager

# Import getpass
from getpass import getpass

# Import xml.dom for pretty print
from xml.dom.minidom import parseString

# Create a dict of devices to connect to
routers = {
    "R1": "192.168.42.129",
    "R2": "192.168.42.130"
}

# Create a dict of interfaces to configure
interfaces = {
    "R1": {
        "GigabitEthernet2": {
            "description": "Configured by NetConf",
            "ip_address": "192.168.1.1",
            "netmask": "255.255.255.0"
        }
    },
    "R2": {
        "GigabitEthernet2": {
            "description": "Configured by NetConf",
            "ip_address": "192.168.1.2",
            "netmask": "255.255.255.0"
        }
    }
}

# Loop through the router and configure the interfaces
for r_name, r_ip in routers.items():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    print(f"=== Connection to {r_name} ({r_ip}) is successfull === : ")
    
    # Create a connection to the router using ncclient
    with manager.connect(
        host=r_ip,
        port=830,
        username=username,
        password=password,
        hostkey_verify=False
    ) as m:
        print(f"Connected to {r_name}. Configuring interfaces: ")
        
        # Loop through the interfaces and configure them
        for intf_name, intf_config in interfaces[r_name].items():
            # Create the XML configuration for the interface
            int_payload = f"""
            <config>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                    <interface>
                        <name>{intf_name}</name>
                        <description>{intf_config['description']}</description>
                        <enabled>true</enabled>
                        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                            <address>
                                <ip>{intf_config['ip_address']}</ip>
                                <netmask>{intf_config['netmask']}</netmask>
                            </address>
                        </ipv4>
                    </interface>
                </interfaces>
            </config>
            """
            # Send the configuration to the router
            m.edit_config(target="running", config=int_payload)
            # Print the configuration in a pretty XML format
            int_config = parseString(int_payload)
            print(int_config.toprettyxml())
            