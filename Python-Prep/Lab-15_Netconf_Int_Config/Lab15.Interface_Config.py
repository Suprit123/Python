# Import the ncclient library
from ncclient import manager

# Import the get pass library
from getpass import getpass

# # Import parseString from xml.dom.minidom to convert the deserialized output of data in serialized manner
from xml.dom.minidom import parseString

# Device details
R1 = "192.168.42.129"

# Connect to the device using manager.connect() method
with manager.connect(
    host=R1,
    port=830,
    username=input(f"Enter your username for {R1}: "),
    password=getpass("Enter your password: "),
    hostkey_verify=False,
) as c:
    print(f"Connected to the device with IP {R1} Successfully!")
    
    # Configure the interface using edit_config() method
    int_payload = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"
                xmlns:ietf-ip="urn:ietf:params:xml:ns:yang:ietf-ip">
        <interface>
            <name>GigabitEthernet2</name>
            <description>Configured by Netconf</description>
            <enabled>true</enabled>
            <ietf-ip:ipv4>
                <ietf-ip:address>
                    <ietf-ip:ip>192.168.1.2</ietf-ip:ip>
                    <ietf-ip:netmask>255.255.255.0</ietf-ip:netmask>
                </ietf-ip:address>
            </ietf-ip:ipv4>
        </interface>
    </interfaces>
</config>
"""
    c.edit_config(target="running", config=int_payload)
    # Convert the output to a pretty XML format using parseString() method
    int_config = parseString(int_payload)
    # Print the interface configuration in a pretty XML format
    print(int_config.toprettyxml())
    
