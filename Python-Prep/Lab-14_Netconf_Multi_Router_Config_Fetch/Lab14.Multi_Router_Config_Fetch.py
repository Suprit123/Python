# Import the ncclient library to manage network devices using NETCONF protocol
from ncclient import manager

# Import getpass
from getpass import getpass

# Import xml.dom.minidom to parse XML data
from xml.dom.minidom import parseString


# Define a dictionary to store the connection details of the routers
routers = {
    'R1': "192.168.1.4",
    'R2': "192.168.1.5",
}

# Create a loop for each router in the dictionary
for r_name, r_ip in routers.items():
    
    # Connect do the routers using the ncclient manager
    with manager.connect(
        host = r_ip,
        port = 830,
        username = input(f"Enter username for {r_name}: "),
        password = getpass(f"Enter password for {r_name}: "),
        hostkey_verify = False
    ) as m:
        # Get the running configuration for each router
        config = m.get_config(source='running').data_xml
        
        # Parse the XML data using xml.dom.minidom
        config_xml = parseString(config)
        
        # Write the configuration to a file named after the router
        with open(f"{r_name}_config.txt", "w") as f:
            f.write(f"=== RunningConfiguration for {r_name} with IP {r_ip} ===\n\n")
            f.write(config_xml.toprettyxml())
            # Print a message indicating that the configuration has been saved
        print(f"Configuration for {r_name} with {r_ip} saved to {r_name}_config.txt")
        
