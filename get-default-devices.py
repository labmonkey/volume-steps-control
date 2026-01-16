from src.storage import Storage
import sys

## CONFIGURATION VARIABLES ##

# Device name as seen by using the list-devices.py script
deviceName = sys.argv[1]

## END OF CONFIGURATION VARIABLES ##

# This will return the currently used mode. Useful when you have an UI with a button and want to display the state

storage = Storage("switch-default-devices")
key = "deviceMode"

if (storage.hasStorageValue(key)):
    value = storage.getStorageValue(key)
    if (value == deviceName):
        print(value)
        sys.exit(0)

sys.exit(1)