import subprocess     #python run windows CMD COMMANDS LIKE PING....
import datetime        # PYTHON RUNS CURRENT DATE AND TIME...


  # THIS IS THE ENGINE.It pings 1 server and says TRUE/FALSE
def ping_server(server):        #define function,'sever is input'
    try:    #----------->attempt this,but if it crashes,don't kill the program
        result = subprocess.run(     #------> run a CMD command
            ["ping", "-n", "1", "-w", "1000", server],  #----->command as list
            capture_output=True,       #-->grab text output from CMD
            text=True, #----->give output as string not bytes
            timeout=2)      #----->Kill if ping takes >2 seconds
        return result.returncode == 0     #------>0 = success up,so return true
    except subprocess.TimeoutExpired:    #if timeout=2 hits
        return False      #----------->server too sloe = down
    except:        #if any other error happens
        return False    # assume down

def log_down_server(server):
    #,,,,,append failed servers to log files with timestamp,,,,,
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #datetime.now() = 2026-06-16 11:42:45.123456
    #strftime() = format it to "2026-06-16 11:42:45"
    with open("alert_log.txt", "a") as f:   #"a" append, f = nickname forthe file inside this block
        f.write(f"{timestamp} - DOWN - {server} \n")   #file auto closes when 'with' block ends
    print(f"Logged : {timestamp} - {server}")

#======MAIN SCRIPT=====
servers = ["google.com", "github.com", "192.168.1.1", "fake.server.test"]
down_list = []

print("====server check with logging====")
for srv in servers:
    print(f"checking {srv:<20}", end=" ")   #end = don't goto new line yet wait for up/down
    if ping_server(srv):
        print("UP")
    else:
        print("DOWN - logging...")
        down_list.append(srv)
        log_down_server(srv)    #call functions to wrire file now
print(f"\n check complete. {len(down_list)} servers DOWN.")
print("see alert _log.txt for details.")



