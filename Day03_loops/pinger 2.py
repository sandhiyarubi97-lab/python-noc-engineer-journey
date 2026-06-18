import random
import time

server = ["amazon.com", "google.com", "github.com", "yahoo.com", "whatsapp.com", "message.com", "instagram.com", "catgut.com"]
down_server = []
time.sleep(0.3)
print(f"starting server health check \n")

for servers in server:
    print(f"pinging {servers}...... ", end=" ")
    time.sleep(0.5)
    #90% up and 10%down.................
    status = random.choice(["up", "up", "up", "up", "up", "up", "down", "down"])

    if status == "up":
        print("up")
    else:
        print("down")
        down_server.append(servers)

print("\n....summary report.....")
print(f"length of the servers: {len(server)}")
print(f"servers up: {len(server)} - {len(down_server)} ")
print(f"down_servers: {len(down_server)}")


if len(down_server) > 0:
    print("\n ALERT:action need for this server")
    for index, bad_server in enumerate(down_server, 1):
        print(f"{index}.{bad_server}")
else:
    print("\n NO action needed")
