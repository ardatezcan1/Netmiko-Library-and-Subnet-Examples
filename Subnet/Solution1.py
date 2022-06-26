a=input("Could you please give me a IP?")  # Getting IP from the user
asplit=a.split(".") # Each 8 bits is split and assigned to a variable below to investigate separately
a0= int (asplit[3])
a1= int (asplit[2])
a2= int (asplit[1])
a3= int (asplit[0])
wrong = 0
with open("ip_ranges.txt") as ip_ranges: # File opened
    for line in ip_ranges:
        line_parts=line.split() # Splited by spaces
        IP=line_parts[2::3] # The 3rd variable in the resulting list is kept because it is the IP address.
        for a in IP:
            b = a.split(".") # Split into 8 bits for reviewing the IP address
            b3= int (b[0]) # First 8 bits assigned to a variable
            if a3==b3: # Checked the IP sameness with this and below, if the same, the next 8 bits are assigned to a variable
                b2 = int(b[1])
                if a2==b2:
                    b1 = int(b[2])
                    if a1==b1:
                        b01=b[3].split("/") # The last 8 bits are reserved from signs such as /24 indicating the subnet at the end
                        b0 = int(b01[0])
                        if a0>=b0: # Is the given IP checked in the same subnet?
                            print(line) # Subnets were written, where IPs that are in the same subnet can be found
                            wrong=1 # To keep the information that the IP subnet is found
    if wrong==0: # Checks if the given IP address matches us
        print("You are not belong to here") # Error message