import subprocess #runs ping inside script
import csv #write csv file
import platform #for appropriate host OS
from datetime import datetime #timestamps

#subnet to scan
base_ip = "192.168.1" #network
start = 1 #range beg hoat
end = 254 #range end- host

output_file = "network_inventory.csv"
results = [] #collects results

print("Starting ping sweep...")
print("-" * 40)

for i in range(start, end + 1): #loops through host portion
    ip = f"{base_ip}.{i}" #builds whole IP

    # Linux/Mac uses -c, Windows uses -n (ping count)
    if platform.system() == "Linux":
        command = ["ping", "-c", "1", "-W", "500", ip]
    else:
        command = ["ping", "-n", "1", "-w", "1", ip]

    response = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) #devnull- dont need output, just success/failure

    if response.returncode == 0: #sucess
        status = "Up"
    else:
        status = "Down"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results.append([ip, status, timestamp])
    print(f"{ip} — {status}")


# Write everything to CSV
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["IP Address", "Status", "Timestamp"])
    writer.writerows(results)

print("-" * 40)
print(f"Sweep complete. Results saved to {output_file}")


# run
    #/usr/bin/python "/home/mk/Documents/CyberSecurityPathway/projects /Network Inventory/pingSweep.py"