log = "WARNING 2026:06:11 09:07:33 disk space low on SERVER-DB01"

#extract using split and slice

parts = log.split()    #['WARNING', '2026:06:11', '09:07:33', 'disk', 'space', 'low', 'on', 'SERVER-DB01'
                       #alert_level 0    #date 1    #time 2      #message 3           #server_name -1
print(parts)
#slicing
alert_level = parts[0]
date = parts[1]
time = parts[2]
#message = parts[3]           #if we print only 3 it gives result only disk ,so we need to join part 3 to -1
message = " ".join(parts[3:-1])     #join parts of index 3 to last(-1)
server_name = parts[-1]

print(f"ALERT_LEVEL: {alert_level}")
print(f"DATE: {date}")
print(f"TIME: {time}")
print(f"ISSUE: {message}")
print(f"SERVER: {server_name}")

#check if critical
if alert_level in ("ERROR", "CRITICAL"):
    print(">>>>needs immediate action")
else:
    print(">>>monitor only")
