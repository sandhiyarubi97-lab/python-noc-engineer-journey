log = "ERROR 2026_06_11 09:45:23 CPU usage 95% on WEB-01"

#split and slicing...............

parts = log.split()  #['ERROR','2026_06_11', '09:45:23', 'CPU', 'usage', '95%', 'on', 'WEB-01']

#slicing..........
alert = parts[0]
date = parts[1]
time = parts[2]
message = " ".join(parts[3:-1])
server = parts[-1]
print(f"ALERT: {alert}")
print(f"DATE: {date}")
print(f"TIME:  {time}")
print(f"issue: {message}")
print(f"SERVER: {server}")

if alert in "ERROR":                  #CAN USE :IF ALERT NOT IN "ERROR"
    print("NEEDS IMMEDIATE ACTION")
else:
    print("CPU ONLY<<<<>>>>")