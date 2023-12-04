from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, DEVICE_STATE, AudioDevice
from pycaw.constants import (
    DEVICE_STATE,
    STGM,
    AudioDeviceState,
    CLSID_MMDeviceEnumerator,
    EDataFlow,
    ERole,
    IID_Empty,
)
import comtypes
import psutil
from _ctypes import COMError

from pycaw.api.audioclient import ISimpleAudioVolume
from pycaw.api.audiopolicy import IAudioSessionControl2, IAudioSessionManager2
from pycaw.api.endpointvolume import IAudioEndpointVolume
from pycaw.api.mmdeviceapi import IMMDeviceEnumerator, IMMEndpoint

def GetActiveDevices():
    vals = AudioUtilities.GetDeviceEnumerator().EnumAudioEndpoints(
        EDataFlow.eAll.value, DEVICE_STATE.ACTIVE.value
    ) 

    count = vals.GetCount()
    devices = []

    for i in range(0, count):
        devices.append(AudioUtilities.CreateDevice(vals.Item(i)))
    return devices

def GetActiveDevice(name):
    for device in GetActiveDevices():
        if device.FriendlyName == name:
            return device
    return None

devices = AudioUtilities.GetSpeakers()
test= AudioUtilities.CreateDevice(devices)
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(AudioDevice)

print(volume.GetMasterVolumeLevelScalar())

def GetProcess(name):
    for session in AudioUtilities.GetAllSessions():
        if session.Process is not None and session.Process.name() == name:
            return session
    return None

def main():
    for device in GetActiveDevices():
        print(device)

    # speakers = GetActiveDevice("Głośniki (Realtek(R) Audio)")
    # headphones = GetActiveDevice("Słuchawki (Arctis Nova 7)")
    # discord = GetProcess("Discord.exe")

    # print(speakers, speakers.EndpointVolume.GetMasterVolumeLevelScalar())
    # print(headphones, headphones.EndpointVolume.GetMasterVolumeLevelScalar())
    # if (discord is not None):
    #     print(discord, discord.SimpleAudioVolume.GetMasterVolume())

    # SetMasterVolumeLevelScalar


# speakers.SetMasterVolumeLevel(-15.0, None)

# Słuchawki (Arctis Nova 7)
# Głośniki (Realtek(R) Audio)
# if device.state is not DEVICE_STATE.ACTIVE.value:
#     continue
# interface = device.Activate(
# IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))

# print(device.EndpointVolume)

# # Control volume
# #volume.SetMasterVolumeLevel(-0.0, None) #max
# #volume.SetMasterVolumeLevel(-5.0, None) #72%
# volume.SetMasterVolumeLevel(-15.0, None) #51%

if __name__ == "__main__":
    main()
