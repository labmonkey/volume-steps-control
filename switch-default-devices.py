import sys
import subprocess
import time
import os

# start = time.time()

## CONFIGURATION VARIABLES ##

# Path to the https://www.nirsoft.net/utils/sound_volume_command_line.html tool (Note it is the CLI version).
exePath = "%userprofile%\\svcl-x64\\svcl.exe"
# Name of your headphones device as seen by using the https://www.nirsoft.net/utils/sound_volume_view.html tool (Note this is the GUI version)
headphonesName = "Arctis Nova 7"
# Name of your speakers device as seen by using the https://www.nirsoft.net/utils/sound_volume_view.html tool (Note this is the GUI version)
speakersName = "Realtek(R) Audio"
# Name of your default device as seen by using the https://www.nirsoft.net/utils/sound_volume_view.html tool (Note this is the GUI version)
defaultName = "DefaultRenderDevice"
# Do you want to output all sound to 'speakers' or 'headphones' or mixed mode 'hybrid'
deviceMode = sys.argv[1]

## END OF CONFIGURATION VARIABLES ##

# ## DO NOT TOUCH FROM THIS POINT ##

# In case you use change-volume-steps.py scipt then default device cache will have to be reset
cachePath = f"{os.path.expanduser('~')}\\.volumecache"  # The cache files are stored in user home directory
if not os.path.exists(cachePath):
    defaultVolumeName = "".join(x for x in defaultName if x.isalnum())

    os.remove(rf"{cachePath}\{defaultVolumeName}")

## Prepare commands
if deviceMode == "speakers":
    commandSetAll = f'{exePath} /SetDefault "{speakersName}" all'
    # Below can be modified to any application names or even more commands
    commandSetFirefox = f'{exePath} /SetAppDefault "{speakersName}" all firefox.exe'
    commandSetChrome = f'{exePath} /SetAppDefault "{speakersName}" all chrome.exe'
if deviceMode == "headphones":
    commandSetAll = f'{exePath} /SetDefault "{headphonesName}" all'
    # Below can be modified to any application names or even more commands
    commandSetFirefox = f'{exePath} /SetAppDefault "{headphonesName}" all firefox.exe'
    commandSetChrome = f'{exePath} /SetAppDefault "{headphonesName}" all chrome.exe'
if deviceMode == "hybrid":
    # The idea of hybrid mode is that by default all my music (from web browsers) is playing on speakers but everything else (games) on the headphones
    commandSetAll = f'{exePath} /SetDefault "{headphonesName}" all'
    # Below can be modified to any application names or even more commands
    commandSetFirefox = f'{exePath} /SetAppDefault "{speakersName}" all firefox.exe'
    commandSetChrome = f'{exePath} /SetAppDefault "{speakersName}" all chrome.exe'

print(commandSetAll)
print(commandSetFirefox)
print(commandSetChrome)

subprocess.run(
    commandSetAll, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
)
subprocess.run(
    commandSetFirefox,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)
subprocess.run(
    commandSetChrome,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

# end = time.time()
# elapsed_time_ms = (end - start) * 1000
# print(f"Elapsed time: {elapsed_time_ms:.2f} milliseconds")
