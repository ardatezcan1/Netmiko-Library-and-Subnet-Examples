ip_addr = input("Enter IP address: ") # Getting IP from the user
print(ip_addr)

with open("ip_ranges.txt") as ip_ranges:
    ip_range_lines = ip_ranges.readlines()

for line in ip_range_lines:
    line = line.strip() # Splited by spaces
    line_parts = line.split(":") # Splited by ":"
    ip_range = ""
    if len(line_parts) > 1:
        ip_range = line_parts[1]
        ip, subnet_mask = ip_range.split('/') # Splited by "/"
    ip_parts = ip.strip().split(".")
    first_host = int(ip_parts[3])
    last_host = first_host + (2 ** (32 - int(subnet_mask)) - 2)
    ip_addr_parts = ip_addr.split(".")
    if int(ip_addr_parts[3]) in range(first_host, last_host+1):
        if ip_addr_parts[0] == ip_parts[0] and ip_addr_parts[1] == ip_parts[1] and ip_addr_parts[2] == ip_parts[2]:
            print(line)

