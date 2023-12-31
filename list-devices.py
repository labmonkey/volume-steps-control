from src.common import *

"""
Use this script to print device and process names which you can use in other scripts.
"""

print(f"{bcolors.BOLD}Active Devices:{bcolors.ENDC}")
for device in GetActiveDevices():
    print(GetDeviceName(device))

# Please note that processes will be visible after they are started and active. For example Discord.exe may show up only after you join a channel
print(f"{bcolors.BOLD}Active Processes:{bcolors.ENDC}")
for session in GetProcesses():
    print(GetDeviceName(session))
