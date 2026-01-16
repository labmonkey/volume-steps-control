from pycaw.pycaw import AudioUtilities, AudioDevice, AudioSession
from pycaw.constants import DEVICE_STATE, EDataFlow
from typing import Optional

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def GetActiveDevices() -> list[AudioDevice]:
    vals = AudioUtilities.GetDeviceEnumerator().EnumAudioEndpoints(
        EDataFlow.eRender.value, DEVICE_STATE.ACTIVE.value
    )

    count = vals.GetCount()
    devices = []

    for i in range(0, count):
        devices.append(AudioUtilities.CreateDevice(vals.Item(i)))
    return devices


def GetActiveDevice(name) -> AudioDevice:
    for device in GetActiveDevices():
        if GetDeviceName(device) == name:
            return device
    return None


def GetDeviceName(device) -> Optional[str]:
    """
    Normally device.FriendlyName could be used (more unique) but at same time the name might contain language specific names and letters that cause issues
    """
    if isinstance(device, AudioSession):
        return device.Process.name()
    elif isinstance(device, AudioDevice):
        return device.properties.get("{B3F8FA53-0004-438E-9003-51A46E139BFC} 6")
    return None


def GetDefaultDevice() -> AudioDevice:
    return AudioUtilities.GetSpeakers()


def GetProcesses() -> list[AudioSession]:
    sessions = []
    for session in AudioUtilities.GetAllSessions():
        if session.Process is not None:
            sessions.append(session)
    return sessions


def GetProcess(name) -> AudioSession:
    for session in GetProcesses():
        if GetDeviceName(session) == name:
            return session
    return None


def GetMasterVolume(device) -> Optional[int]:
    volume = GetMasterVolumeInternal(device)
    print("Getting volume of '%s' : %s" % (GetDeviceName(device), volume))
    return volume

def GetMasterVolumeInternal(device) -> Optional[int]:
    if isinstance(device, AudioSession):
        volume = int(round(device.SimpleAudioVolume.GetMasterVolume(), 2) * 100)
        return volume
    elif isinstance(device, AudioDevice):
        volume = int(round(device.EndpointVolume.GetMasterVolumeLevelScalar(), 2) * 100)
        return volume
    return None

def SetMasterVolume(device, targetVolume):
    if isinstance(device, AudioSession):
        realVolume = targetVolume / 100
        print(
            "Setting volume of '%s' : %s (%s)"
            % (GetDeviceName(device), targetVolume, realVolume)
        )
        return device.SimpleAudioVolume.SetMasterVolume(realVolume, None)
    elif isinstance(device, AudioDevice):
        realVolume = targetVolume / 100
        print(
            "Setting volume of '%s' : %s (%s)"
            % (GetDeviceName(device), targetVolume, realVolume)
        )
        return device.EndpointVolume.SetMasterVolumeLevelScalar(realVolume, None)
    return None
