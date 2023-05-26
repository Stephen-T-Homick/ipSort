import sys

def concatenate_and_sort_ips(filename):
    with open(filename, 'r') as file:
        ip_list = file.read().splitlines()  # Read IP addresses from the file

    # Sort the IP addresses
    sorted_ips = sorted(ip_list)

    # Enclose each IP address in quotes and join them with commas
    formatted_ips = ','.join(['"' + ip + '"' for ip in sorted_ips])

    return formatted_ips


# Check if filename argument is provided
if len(sys.argv) < 2:
    print("Please provide the filename of the IP addresses as a command-line argument.")
    sys.exit(1)

# Get the filename from command-line arguments
filename = sys.argv[1]

formatted_ips = concatenate_and_sort_ips(filename)
print(formatted_ips)
