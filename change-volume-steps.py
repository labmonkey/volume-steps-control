import sys
import subprocess
import time
import os

# start = time.time()

## CONFIGURATION VARIABLES ##

# Path to the https://www.nirsoft.net/utils/sound_volume_command_line.html tool (Note it is the CLI version).
exePath="%userprofile%\\svcl-x64\\svcl.exe"
# What volume "steps" do you want. By default volume increments by 5. It can be whatever but the values have to to be in increasing order.
volumeSteps=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
# Device name as seen by using the https://www.nirsoft.net/utils/sound_volume_view.html tool (Note this is the GUI version)
deviceName=sys.argv[1]
# Do you want to increase 'up' or decrease 'down' the volume
volumeMode=sys.argv[2]

## END OF CONFIGURATION VARIABLES ##

## DO NOT TOUCH FROM THIS POINT ##
cachePath = f"{os.path.expanduser('~')}\\.volumecache" # The cache files are stored in user home directory
volumeName="".join(x for x in deviceName if x.isalnum())
cacheVolumePath = rf"{cachePath}\{volumeName}"

# Create cache dir if it does not exist
if not os.path.exists(cachePath):
    os.makedirs(cachePath)

# Check current volume level and store in cache (faster by 50%)
if not os.path.exists(cacheVolumePath):
    commandGetVolume=f"{exePath} /GetPercent \"{deviceName}\" /StdOut"
    resultVolumeLevel = subprocess.run(commandGetVolume, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    with open(cacheVolumePath, 'w') as file:
        file.write(str(resultVolumeLevel.stdout.strip()))

# Get current volume level from cache file
with open(cacheVolumePath, 'r') as file:
    currentVolumeLevel = float(file.read().strip())

print(f"Old Volume: {currentVolumeLevel}")

if volumeMode == 'up':
    if currentVolumeLevel == volumeSteps[-1]:
        targetVolumeLevel = currentVolumeLevel
    else:
        for i, step in enumerate(volumeSteps):
            if step > currentVolumeLevel:
                targetVolumeLevel = step
                break
elif volumeMode == 'down':
    if currentVolumeLevel == volumeSteps[0]:
        targetVolumeLevel = currentVolumeLevel
    else:
        for i, step in enumerate(reversed(volumeSteps)):
            if step < currentVolumeLevel:
                targetVolumeLevel = step
                break

commandSetVolume=f"{exePath} /SetVolume \"{deviceName}\" {targetVolumeLevel}"
subprocess.run(commandSetVolume, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print(f"New Volume: {targetVolumeLevel}")

# Store new volume level in cache
with open(cacheVolumePath, 'w') as file:
    file.write(str(targetVolumeLevel))

# end = time.time()
# elapsed_time_ms = (end - start) * 1000
# print(f"Elapsed time: {elapsed_time_ms:.2f} milliseconds")