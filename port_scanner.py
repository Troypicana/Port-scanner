import socket
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

# Prompt the user to type a website or IP address and store it as a string.
target = input("Enter the target IP or website to scan: ")

# Create a list containing the specific TCP port numbers you want to check.
port_input = input("Enter range of ports to scan (e.g. 1-1024): ")

# Split the string at the hyphen into a starting string and ending string.
start_port, end_port = port_input.split("-")

# Convert the split strings into integers and create a loopable range (adding 1 to include the last port).
ports = range(int(start_port), int(end_port) + 1)

# Scan ports using a thread pool
def scan_port(port):
    # Initialize a new IPv4 (AF_INET) and TCP (SOCK_STREAM) socket object for this port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Use a try block to safely run the connection attempt.
    try:

        # Restrict the socket to wait a maximum of 1.0 second for a network response.
        sock.settimeout(1.0)

        # Attempt to connect to the target host and port, returning an error code integer.
        result = sock.connect_ex((target, port))

        # Evaluate if the connection attempt returned an error code of zero (success).
        if result == 0:

            try:
                # Send a simple request to the server to get the banner
                sock.send(b"\r\n")

                # Receive the banner from the server 
                banner = sock.recv(1024).decode().strip()

            # If an error occurs when grabbing banner, set to empty string.
            except:
                banner = ""

            # Wrap the service lookup in a try-except block to handle errors.
            try:
                # Get the service name for the specific port.
                service_name = socket.getservbyport(port, "tcp")

            # If service name isn't found, set to "Unknown"
            except OSError:
                service_name = "Unknown"

        # Print a message to the terminal stating that the current port is open and which service is running.
        # Also display the banner if available.
            if banner:
                return(f"Port {port}: Open ({service_name}), Banner: {banner}")
            else:
                return(f"Port {port}: Open ({service_name})")

        else:
        # Return None (or a string) so the thread pool knows the port is closed.)
            return None
    # The finally block will always run, ensuring the socket is closed after the return.
    finally:
    # Terminate the socket connection to free up system operating memory and resources.
        sock.close()

with ThreadPoolExecutor(max_workers=100) as executor:
    results = executor.map(scan_port, ports)

    # Loop through compiled results from all finished threads.
    for output in results:
        # Check if the thread returned a result (i.e., the port is open).
        if output is not None:
            # Print the open port message
            print(output)

# Pause execution until the user presses Enter
input("Press enter to exit...")