import time
logs = ["ERROR 10:15:13 disk full on server-01",
        "INFO 10:16:01 backup started",
        "WARNING 10:17:45 CPU 85% on server-02",
        "ERROR 10:18:12 database connection failed",
        "INFO 10:19:33 User login success",
        "CRITICAL 10:20:55 power supply failure"]

error_count = 0
warning_count = 0
critical_count = 0

print("analyzing log file....\n")
time.sleep(0.6)

for log_line in logs:
    if "ERROR" in log_line:
        error_count += 1
        print(f"found error: {log_line}")
    elif "WARNING" in log_line:
        warning_count += 1
        print(f"found warning: {log_line}")
    elif "CRITICAL" in log_line:
        critical_count += 1
        print(f"found critical: {log_line}")
        time.sleep(0.9)    #to delay ..........
print("\n....log summary....\n")
time.sleep(0.7)
print(f"total logs: {len(logs)}")
print(f"ERROR: {error_count}")
print(f"WARNING: {warning_count}")
print(f"CRITICAL: {critical_count}")

if critical_count > 0:
    print("\nESCALATE TO L2 TEAM")
