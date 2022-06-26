import netmiko


connection = netmiko.Netmiko(host="192.168.11.51", device_type="sros", username='admin', password='admin')
command = "show port"
output = connection.send_command(command)
# print(output)
for line in output.split("\n"):
    line_parts = line.split()
    if len(line_parts) > 6:
        if line_parts[1] == "Up":
            print(line)
connection.disconnect()
