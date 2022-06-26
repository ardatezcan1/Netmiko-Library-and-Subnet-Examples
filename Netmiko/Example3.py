import netmiko


device_list = ["192.168.11.51", "192.168.11.52"]

for device in device_list:
    print("~" * 79)
    print("Connecting to {}".format(device))
    connection = netmiko.Netmiko(
        host=device,
        device_type="sros",
        username='admin',
        password='admin'
    )

    cmd = "show port"
    output = connection.send_command(cmd)
    # print(output)
    for line in output.split("\n"):
        line_parts = line.split()
        if len(line_parts) > 7:
            if line_parts[7].lower() == "accs":
                print(line)

    connection.disconnect()