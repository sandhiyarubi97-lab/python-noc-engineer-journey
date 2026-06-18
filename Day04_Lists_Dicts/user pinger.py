import subprocess


def ping_server(server):
    try:
        result = subprocess.run(["ping", "-n", "1", "-w", "1000", server],
                                capture_output=True, text=True, timeout=2)
        return result.returncode == 0
    except:
        return False


servers = []
print("Enter the servers to ping . Type 'done' to start check \n")
while True:
    s = input("servers: ").strip()
    if s.lower() == 'done':
        break
    elif s:
        servers.append(s)
if not servers:
    print("No servers entered. Exit.")
else:
    print(f"checking: {len(servers)} servers.....\n")
    for server in servers:
        status = "up" if ping_server(servers) else "down"
        print(f"{server} : {status}")