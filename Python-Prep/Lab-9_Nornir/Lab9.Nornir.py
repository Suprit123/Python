# Import the nornir library
from nornir import InitNornir

# Import the norninr tasks netmiko_send_command
from nornir_netmiko.tasks import netmiko_send_command

# Import the nornir plugins for printing the results
from nornir_utils.plugins.functions import print_result

# Import nornir execution error library
from nornir.core.exceptions import NornirExecutionError

# Import the sys library for error code
import sys


# Initialize norninr
init = InitNornir()

# Run the netmiko_send_command task by adding the run function to send the command to the devices.
output = init.run(task=netmiko_send_command, command_string="show arp")

# Print the output by using the print_result library
print_result(output)

# Fail the script with error code if any host failed
if output.failed:
    print("Device Failed")
    sys.exit(1)
