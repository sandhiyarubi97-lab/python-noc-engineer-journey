import subprocess
import datetime


def ping_server(Server):
    # ping a server once. Return True if UP or False if Down

    try:
        # windows: ping -n 1 -w 10000 server
        # -n 1 = packet, -w 1000 = wait 1000ms = 1 sec timeout
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "1000", Server],
            capture_output=True, text=True, timeout=2)  # kill if takes >2 sec

        return result.returncode == 0  # 0 means success
    except:
        return False  # if any error assume Down


servers = ["google.com", "youtube.com", "8.8.8.8", "192.48.84.1"]
down_servers = []  # stores if any servers is down
print(f"server health check - {datetime.datetime.now()}")
print("-" * 40)

for server in servers:
    print(f"pinging {server}...", end=" ")
    if ping_server(server):
        print("up")
    else:
        print("down")
        down_servers.append(server)

print("\n .......summary......")
print(f"total: {len(servers)} | up: {len(servers) - len(down_servers)} | down: {len(down_servers)}")
if down_servers:
    print("ALERT: check these servers")
    for s in down_servers:
        print(f" - {s}")

    with open("down_servers.txt", "w") as f:
        f.write(f"failed at {datetime.datetime.now()}\n")
        for s in down_servers:
            f.write(f"{s}\n")
    print("\n saved DOWN servers TO down_servers.txt ")


