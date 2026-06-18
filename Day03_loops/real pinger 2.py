import subprocess
import datetime


def ping_server(server):
    try:
        result = subprocess.run(["ping", "-n", "1", "-w", "1000", server],
                                capture_output=True,
                                text=True,
                                timeout=3)  # kill command if stuck for >3 sec
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False  # took too long = down
    except:
        return False  # any other error = down


# Main monitoring script........
servers_to_check = ["google.com", "8.8.8.8", "github.com", "192.168.1.1"]
failed_servers = []

print(f"===server health check===")
print(f"Time : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-" * 35)
for server in servers_to_check:
    print(f"pinging {server:<15}", end="....")  # align text
    if ping_server(server):
        print("UP")
    else:
        print("DOWN")
        failed_servers.append(server)

    # summary report.....
print("\n----- summary report-------")
total = len(servers_to_check)
down = len(failed_servers)
up = total - down
print(f"total: {total} | UP: {up} | DOWN: {down}")

if failed_servers:
    print("\n ACTION REQUIRED:")
    for i, srv in enumerate(failed_servers, 1):
        print(f"{i}.{srv}")
    else:
        print("\n ALL systems operational")
