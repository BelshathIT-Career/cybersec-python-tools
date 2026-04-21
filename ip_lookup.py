import socket

target = input("Enter domain (e.g., google.com): ")

try:
    ip = socket.gethostbyname(target)
    hostname = socket.gethostbyaddr(ip)

    print("\n===== RESULT =====")
    print(f"Domain: {target}")
    print(f"IP Address: {ip}")
    print(f"Hostname Info: {hostname}")

except socket.gaierror:
    print("Invalid domain. Try again.")
except socket.herror:
    print("Hostname not found.")

