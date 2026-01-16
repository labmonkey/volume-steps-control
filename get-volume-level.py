import sys
from src.common import *

## CONFIGURATION VARIABLES ##

# Device name as seen by using the list-devices.py script
deviceName = sys.argv[1]

## END OF CONFIGURATION VARIABLES ##

## DO NOT TOUCH FROM THIS POINT ##
if deviceName == "DefaultRenderDevice":
    activeDevice = GetDefaultDevice()
elif ".exe" in deviceName:
    activeDevice = GetProcess(deviceName)
else:
    activeDevice = GetActiveDevice(deviceName)

if activeDevice is None:
    print(f"{deviceName} not found. Exit.")
    sys.exit()

print(GetMasterVolumeInternal(activeDevice))
