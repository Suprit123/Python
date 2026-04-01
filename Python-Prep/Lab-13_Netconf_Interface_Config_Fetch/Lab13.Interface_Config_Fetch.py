# Import manager from ncclient to connect via Netconf
from ncclient import manager

# Import getpass to securely get the password input from the user
from getpass import getpass

# Import parseString from xml.dom.minidom to convert the deserialized output of data in serialized manner
from xml.dom.minidom import parseString

# Define device IP
device_ip = "172.16.166.129"

# Connect to the device using manager.connect() method
with manager.connect(
    host=device_ip,
    port=830,
    username="cisco",
    password=getpass("Enter your password: "),
    hostkey_verify=False,
) as n:
    print(f"Connected to the device with IP {device_ip} Successfully!")

    # Defining the filter to fetch the interface configuration of the device
    int_filter = """
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
            
            </interface>
        </interfaces>
    </filter>
    """

    # Fetch the interface confi using the get_config() method and passing the fiter as and argument
    int_config = n.get_config(source="running", filter=int_filter)

    # Converting the deserialized output of data in serialized manner using parseString() method
    int_config_xml = parseString(int_config.xml).toprettyxml()

    # Create a text file and save the output of interface config in text file
    with open("int_config.txt", "w") as f:
        f.write(
            f"=== Configuration of interfaces for device with IP {device_ip} ===\n\n"
        )
        f.write(int_config_xml)
        print(
            f"Interface configuration has been saved in int_config.txt file successfully! for{device_ip}"
        )
