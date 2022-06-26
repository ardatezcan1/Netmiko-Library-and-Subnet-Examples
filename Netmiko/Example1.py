import netmiko    # For SSH to network elements
import os         # For dealing with directories and files


list_of_nodes = input("Please enter file name for node list: ")
# Based on file extension, process the node list
nodes = list()
with open(list_of_nodes) as node_file:
    node_list = node_file.readlines()

for node in node_list:
    node = node.strip().split(",")
    node = {'ip': node[0],
            'device_type': node[1]
            }
    nodes.append(node)

commands = ["show port", "show card"]

login = "admin"
password = "admin"

# Loop over each network device
for node in nodes:
    # Update each network device dictionary with credentials entered by the user
    node["username"] = login
    node.update({"password": password})

    # Just for pretty formatting
    print("~" * 79)
    print("Connecting to the node -> {}".format(node["ip"]))

    # Create the connection to the network device
    connection = netmiko.Netmiko(**node)

    # Get the network device name using base_prompt property of the ConnectionHandler
    # so we split this string by ":" to get the second part out of it
    node_name = connection.base_prompt.split(":")[1]

    # For each command create a file under the directory with network device name
    for cmd in commands:
        print("Command '{}' is running on {}".format(cmd, node_name))
        print("Command '%s' is running %s" % (cmd, node_name))
        cmd = cmd.strip()
        output = connection.send_command(cmd)
        print(output)

    # Close the connection to the node
    connection.disconnect()
