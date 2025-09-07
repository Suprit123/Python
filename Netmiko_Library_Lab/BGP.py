from netmiko import ConnectHandler
from getpass import getpass

os = "cisco_ios"
password = getpass("Enter your password: ")

# A dictionary mapping router names to their IP addresses
host_to_ips = {"netmiko1": "172.16.166.131", "netmiko2": "172.16.166.132"}

# A list of router hostnames to configure
router_list = ["netmiko1", "netmiko2"]

# Loop over each router in the list
for routers in router_list:
    device_details = {
        "device_type": os,
        "username": "admin",
        "password": password,
        # Get the corresponding IP from the dictionary
        "ip": host_to_ips[routers],
    }

    # Establish an SSH connection to the router
    ssh_connection = ConnectHandler(**device_details)
    print(f"\n === Connected to {routers} successfully ===")

    # Prompt user for BGP configuration inputs
    local_as = input("Enter the AS number: ")
    neighbor_ip = input("Enter the neighbor IP: ")
    remote_as = input("Enter the remote-as number: ")
    advt_network = input("Enter the network that needs to be advertised: ")
    subnet_mask = input("Enter the subnet mask for the advt network: ")

    # Create a list of BGP configuration commands base on user input
    bgp_config = [
        f" router bgp {local_as}",
        f"neighbor {neighbor_ip} remote-as {remote_as}",
        f" network {advt_network} mask {subnet_mask}",
    ]

    # Send the configuration commands to the router.
    send_config = ssh_connection.send_config_set(bgp_config)
    print(f" Configuration applied successfully to {routers}:\n{send_config}")

    # Run the 'show ip bgp summary' to verify BGP
    bgp_output = ssh_connection.send_command("show ip bgp summary")
    print(f"BGP Summary for applied in {routers}:\n{bgp_output}")

    # Check the bgp peerig status based on the output string from the last router.
    if "Idle" in bgp_output:
        print(f"⚠️ BGP peer is not eastablished {routers}")

    elif "Established" in bgp_output or "EASTABLISHED" in bgp_output:
        print(f"✅ BGP peering is up {routers}")

    else:
        print(f"❓ Unknow bgp state on {routers}, check manually")

    # Disconnect the SSH session from the last router.
    ssh_connection.disconnect()
