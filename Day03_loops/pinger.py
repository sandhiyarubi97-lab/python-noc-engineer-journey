import random         #to stimulate up/down
import time             #to add delay

#lists of servers to monitor..........................
servers = ["google.com", "youtube.com", "github.com", "amazon.com"]
down_servers = []        #empty list to store failed ones

print("starting server health check....\n")
time.sleep(1)

#loop through each servers...................
for server in servers:
    print(f"pinging {server}....", end=" ")
    time.sleep(0.5)
    # stimulate ping 80% chance up ,20% chance down..........
    status = random.choice(["up", "up", "up", "up", "down"])

    if status == "up":
        print("up ")
    else:
        print("down ")
        down_servers.append(server)  # add to down list

print("\n----summary report-------")
print(f"total servers checked: {len(servers)}")
print(f"servers up: {len(servers)} - {len(down_servers)}")
print(f"servers down: {len(down_servers)}")

if len(down_servers) > 0:
    print("\n alert : these servers need attention:")
    for index, bad_server in enumerate(down_servers): #we can use (down_seervers,1) to start index from 1
        print(f"{index + 1}.{bad_server}")             # or we can use {index+1} to start index from 1
    else:
        print("\nall systems operational ok.......")




