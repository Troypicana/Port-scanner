import socket

# Prompt the user to type a website or IP address and store it as a string.
target = input("Enter the target IP or website to scan: ")

# Create a list containing the specific TCP port numbers you want to check.
port_input = input("Enter range of ports to scan (e.g. 1-1024): ")

# Split the string at the hyphen into a starting string and ending string.
start_port, end_port = port_input.split("-")

# Convert the split strings into integers and create a loopable range (adding 1 to include the last port).
ports = range(int(start_port), int(end_port) + 1)

# Start a loop to iterate through each port number inside your ports list.
for port in ports:
    # Initialize a new IPv4 (AF_INET) and TCP (SOCK_STREAM) socket object for this port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Restrict the socket to wait a maximum of 1.0 second for a network response.
    sock.settimeout(1.0)

    # Attempt to connect to the target host and port, returning an error code integer.
    result = sock.connect_ex((target, port))

    # Evaluate if the connection attempt returned an error code of zero (success).
    if result == 0:
        # Print a message to the terminal stating that the current port is open.
        print(f"Port {port}: Open")

    # Terminate the socket connection to free up system operating memory and resources.
    sock.close()

