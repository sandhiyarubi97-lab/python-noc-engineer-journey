from netmiko import ConnectHandler

#.........
cisco_device = {
    'device_type': 'cisco_ios',  # cisco_ios, juniper, arista_eos etc
    'host': '192.168.1.1',  # Router/Switch IP
    'username': 'admin',
    'password': 'cisco123',
}

try:
    print(f"Connecting to {cisco_device['host']}...")
    net_connect = ConnectHandler(**cisco_device)

    # Run the command
    output = net_connect.send_command("show ip int brief")
    print(output)

    #  save the File
    with open("show_ip_int_brief.txt", "w") as f:
        f.write(output)
    print("Output saved to show_ip_int_brief.txt")

    net_connect.disconnect()

except Exception as e:
    print(f"Connection failed: {e}")