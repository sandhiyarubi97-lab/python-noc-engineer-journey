import subprocess


def ping_server(server):
    try:
        result = subprocess.run(["ping", "-n", "1", "-w", "1000", server],
                                capture_output=True, text=True, timeout=2)
        return result.returncode == 0
    except:
        return False
# getting servers lists from user...........
server_list = []
print("\n NOC SERVER CHECK TOOL")
print("\n Enter the server list . Type 'done' to start. \n")

while True:
    user_input = input("server list :").strip()
    if user_input.lower() == 'done':
        break
    if user_input:
        server_list.append(user_input)
        print(f"ADDED: {user_input}")
if not server_list:
    print(f"NO SERVER IS ADDED.")
else:
    print(f"Checking {len(server_list)} servers:\n")
    for server in server_list:
        if ping_server(server):
            print(f"{server:<15}  up")
        else:
            print(f"{server:<15} down")

