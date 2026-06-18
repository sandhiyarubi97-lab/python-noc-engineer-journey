#Goal: string methods NOC uses
router_ip = "  192.168.1.1  "
hostname = "CORE-RTR-01"

#Clean data
clean_ip = router_ip.strip()
print(f"Clean IP: {clean_ip}")

# Check Conditions
if hostname.startswith("CORE"):
    print("This is a core router")

# split config line
config = "interface Gig0/1:up"
interface, status = config.split(":")
print(f"Interface: {interface}, Status: {status}")

#NOC Task: Mask last octet of IP
parts = clean_ip.split(".")
parts[3] = "xxx"
masked_ip = ".".join(parts)
print(f"Masked IP for Logs: {masked_ip}")