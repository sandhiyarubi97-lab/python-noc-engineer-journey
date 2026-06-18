servers = ["google.com", "amazon.com", "github.com"]

#loop through list......
for server in servers:
    print(f"checking {server}.....")

#loop with numbers......
for i in range(5):             #0,1,2,3,4
    print(f"attempt: {i + 1}")        #0+1, 1+1, 2+1, 3+1, 4+1

#loop with index + item......
for index, server in enumerate(servers):
    print(f"{index + 1}.{server}")
