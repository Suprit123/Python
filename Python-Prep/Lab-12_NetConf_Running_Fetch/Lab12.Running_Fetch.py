# Import the manager from nccliet to connect via Netconf
from ncclient import manager

from getpass import getpass

# Import the parseString from xml.dom.minidom to convert the deserialized output of data in serialized manner
from xml.dom.minidom import parseString

# Establish a connection to the device using the manager.connect() method
with manager.connect(
    host="172.16.166.129",
    port=830,
    username="cisco",
    password=getpass("Enter your password: "),
    hostkey_verify=False,
) as net:
    print("Netconfig connection eastablished successfully..!")
    output = net.get_config(source="running")
    # Convert the deserialized output of data in serialized manner and print the output
    pretty_output = parseString(output.xml).toprettyxml()
    print(pretty_output)

    # Create a text and write the date in the text file
    with open("running_config.txt", "w") as file:
        file.write(pretty_output)
        print(
            "Running configuration has been written to running_config.txt file successfully..!"
        )
