#!/usr/bin/python3

import socket
import sys
import time
import getopt
from colorama import init, Fore  # Import colorama for colored output

# Initialize colorama
init(autoreset=True)

# Function to display usage instructions
def usage():
    print("\nSMTP User Enumeration Script")
    print("Usage:")
    print("  python3 smtp_user_enum.py -i <IP> -p <PORT> -o <OUTPUT_FILE> -U <USER_LIST> [options]\n")
    print("Required arguments:")
    print("  -i <IP>         Target SMTP server IP address")
    print("  -p <PORT>       Target SMTP port (default: 25)")
    print("  -o <OUTPUT>     File to save valid usernames")
    print("  -U <USERFILE>   File containing list of usernames to test")
    print("\nOptions:")
    print("  -v              Verbose mode (shows each result)")
    print("  -vv             Debug mode (displays all responses)")
    print("  -h              Show this help message and exit")
    print("\nExample:")
    print("  python3 smtp_user_enum.py -i 10.10.167.142 -p 25 -o result.txt -U users.txt -v")
    sys.exit(1)

# Function to log messages to console and file
def log(message, out_file=None, verbose=False, debug=False, valid=True):
    if verbose:
        if valid:
            print(Fore.GREEN + "[+] valid username" + " " + message)  # GREEN for valid user
        else:
            print(Fore.YELLOW + "[-] wrong username" + " " + message)  # YELLOW for invalid user

    # Only log additional debug information when debug mode (-vv) is enabled
    if debug:
        print(Fore.CYAN + "[DEBUG] Response received for user: " + message)  # CYAN for debug messages
        # You can print additional debug-level responses, for example:
        # print(Fore.CYAN + "[DEBUG] Server Response: " + response) 

    # Only log valid users to the output file
    if valid and out_file:
        out_file.write(message + "\n")

# Function to parse command-line arguments
def parse_arguments():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:p:o:U:vh")
    except getopt.GetoptError:
        usage()

    ip, port, outputfile, userfile = None, 25, None, None
    verbose, debug = False, False

    for opt, arg in opts:
        if opt == "-i":
            ip = arg
        elif opt == "-p":
            try:
                port = int(arg)
            except ValueError:
                print(f"Error: Invalid port number '{arg}'")
                sys.exit(1)
        elif opt == "-o":
            outputfile = arg
        elif opt == "-U":
            userfile = arg
        elif opt == "-v":
            verbose = True
        elif opt == "-vv":
            debug = True
        elif opt == "-h":
            usage()

    if not ip or not outputfile or not userfile:
        print("Error: Missing required arguments.")
        usage()

    return ip, port, outputfile, userfile, verbose, debug

# Function to check if a file exists
def check_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

# Function to get SMTP server banner
def get_banner(s, debug):
    try:
        banner = s.recv(1024).decode()
        if debug:
            print(f"Banner: {banner}")
        return banner
    except Exception as e:
        print(f"Error receiving banner: {e}")
        return None

# Function to check if a user exists using VRFY
def check_user(s, user, out_file, verbose, debug):
    try:
        s.sendall(f"VRFY {user}\r\n".encode())
        response = s.recv(1024).decode()

        if "250" in response or "252" in response:
            log(f"{user}", out_file, verbose, debug, valid=True)
            return user
        else:
            log(f"{user}", out_file, verbose, debug, valid=False)
    except Exception as e:
        log(f"Error checking user {user}: {e}", out_file, verbose, debug, valid=False)
    return None

# Function to enumerate SMTP users
def enumerate_users(ip, port, usernames, outputfile, verbose, debug):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)

    try:
        s.connect((ip, port))
    except socket.timeout:
        print(f"Error: Connection to {ip}:{port} timed out.")
        sys.exit(1)
    except socket.error as e:
        if "Connection refused" in str(e):
            print(f"Error: Cannot connect to {ip}:{port}. The port might be closed.")
        else:
            print(f"Error: Cannot connect to {ip}:{port}. Check the IP and try again.")
        sys.exit(1)

    with open(outputfile, "a") as out:  # Change 'w' to 'a' to append to the file
        banner = get_banner(s, debug)
        if debug and banner:
            log(f"Banner: {banner}", out, verbose, debug, valid=True)

        for user in usernames:
            user = user.strip()
            if not user:
                continue

            check_user(s, user, out, verbose, debug)

        s.close()

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print(f"Enumeration completed at {timestamp}")

# Main execution
def main():
    ip, port, outputfile, userfile, verbose, debug = parse_arguments()
    usernames = check_file(userfile)
    enumerate_users(ip, port, usernames, outputfile, verbose, debug)

if __name__ == "__main__":
    main()
