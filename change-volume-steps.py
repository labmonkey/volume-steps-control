import sys
import subprocess
import time
import os
from src.common import *

# start = time.time()

## CONFIGURATION VARIABLES ##

# What volume "steps" do you want. By default volume increments by 5. It can be whatever but the values have to to be in increasing order.
volumeSteps = [
    0,
    5,
    10,
    15,
    20,
    25,
    30,
    35,
    40,
    45,
    50,
    55,
    60,
    65,
    70,
    75,
    80,
    85,
    90,
    95,
    100,
]
# Device name as seen by using the list-devices.py script
deviceName = sys.argv[1]
# Do you want to increase 'up' or decrease 'down' the volume
volumeMode = sys.argv[2]

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
    exit

currentVolumeLevel = GetMasterVolume(activeDevice)

if volumeMode == "up":
    if currentVolumeLevel == volumeSteps[-1]:
        targetVolumeLevel = currentVolumeLevel
    else:
        for i, step in enumerate(volumeSteps):
            if step > currentVolumeLevel:
                targetVolumeLevel = step
                break
elif volumeMode == "down":
    if currentVolumeLevel == volumeSteps[0]:
        targetVolumeLevel = currentVolumeLevel
    else:
        for i, step in enumerate(reversed(volumeSteps)):
            if step < currentVolumeLevel:
                targetVolumeLevel = step
                break

SetMasterVolume(activeDevice, targetVolumeLevel)

# end = time.time()
# elapsed_time_ms = (end - start) * 1000
# print(f"Elapsed time: {elapsed_time_ms:.2f} milliseconds")