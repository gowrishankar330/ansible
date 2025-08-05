import os

def ping_servers(servers):
    for server in servers:
        response = os.system(f"ping -c 1 {server} > /dev/null 2>&1")
        if response == 0:
            print(f"{server} is reachable.")
        else:
            print(f"{server} is unreachable.")

# Example usage
ping_servers(["google.com", "github.com", "invalid.server"])