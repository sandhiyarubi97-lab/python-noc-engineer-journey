# my goal is to count how many ERROR and WARNING lines in a log file
#step 1: iam going to create a fake log file for practice


with open("router.log", "w") as log:
    log.write("INFO: router booted\n")
    log.write("ERROR: Interface Gi0/1 down \n")
    log.write("WARNING: CPU 80% \n")
    log.write("ERROR: OSPF neighbor lost \n")
    log.write("INFO: config saved \n")

 # step 2: read and analyze
error_count = 0
warning_count = 0

with open("router.log", "r") as log:
    for line in log:
        if "ERROR" in line:
            error_count += 1
            print(f"Found ERROR: {line.strip()}")
        if "WARNING" in line:
            warning_count += 1
            print(f"Found WARNING: {line.strip()}")

# step 3: summary report
print(f"\n -----summary report------")
print(f"Total errors: {error_count}")
print(f"Total warnings: {warning_count}")

# step 4: save report to new file
with open("report.txt", "w") as report:
    report.write(f"NOC daily report \n")
    report.write(f"ERRORS: {error_count} \n")
    report.write(f"WARNINGS: {warning_count} \n")

print("\n Report saved to report.txt")


