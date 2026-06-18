servers = ["google.com", "youtube.com", "github.com", "amazon.com"]
numbers = [60, 75, 345, 23, 235]
mixed = ["server-01", 4, True]              #can mix types, but avoid it

print(servers[0])
print(servers[-1])
print(servers[2])
print(len(servers))

print(numbers[0])
print(numbers[-1])
print(numbers[-2])
print(len(numbers))

servers.append("facebook.com")
servers.remove("github.com")
print(servers)

numbers.append("999")
print(numbers)