servers = []   #starts with empty list because the user may enter many servers/IP

print("servers monitor setup")
print("Enter server name. Type 'done' when finished .\n")

while True:      #loop forever until i stop
    server = input("enter the server/IP or 'done':").strip()

    if server.lower() == 'done':
        break
    elif server == "":
        print("empty . try again")
    else:
        servers.append(server)
        print(f"added : {server}")

print(f"you will monitor {len(servers)} servers:")
for i, s in enumerate(servers, 1):    #i, s = index,server
    print(f"{i} . {s}")
