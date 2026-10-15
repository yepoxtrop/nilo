import os;
from enum import Enum;

class WindowsBasics(Enum):
    
    CALCULATOR = os.path.join(
        "C:",
        "Windows",
        "System32",
        "calc.exe"
    )
    
    EXPLROER = os.path.join(
        "C:"
        "Windows"
        "explorer.exe"
    )
    
    NOTEPAD1 = os.path.join(
        "C:"
        "Windows"
        "System32"
        "notepad.exe"
    )
    
    NOTEPAD2 = os.path.join(
        "C:"
        "Windows"
        "notepad.exe"
    )
    
    NOTEPAD3 = os.path.join(
        "C:"
        "Users"
        "sarmi"
        "AppData"
        "Local"
        "Microsoft"
        "WindowsApps"
        "notepad.exe"
    )
    
    CMD = os.path.join(
        "C:"
        "Windows"
        "System32"
        "cmd.exe"
    )
    
    POWERSHELL = os.path.join(
        "C:"
        "Windows"
        "System32"
        "WindowsPowerShell"
        "v1.0"
        "powershell.exe"
    )
    
    CONTROL = os.path.join(
        "C:"
        "Windows"
        "System32"
        "control.exe"
    )
    
    NETWORK_ADAPTERS  = os.path.join(
        "C:"
        "Windows"
        "System32"
        "ncpa.cpl"
    )
    
    PAINT = os.path.join(
        "C:"
        "Users"
        "sarmi"
        "AppData"
        "Local"
        "Microsoft"
        "WindowsApps"
        "mspaint.exe"
    )
    
    CAMERA = os.path.join(
        "C:"
        "Program Files"
        "WindowsApps"
        "Microsoft.WindowsCamera_2026.2607.1.0_x64__8wekyb3d8bbwe"
        "WindowsCamera.exe"
    )
    