import os;
from enum import Enum;

class WindowsInstalled(Enum):
    
    CHROME = os.path.join(
        "C:\\",
        "Program Files",
        "Google",
        "Chrome",
        "Application",
        "chrome.exe"
    )
    
    EDGE = os.path.join(
        "C:\\",
        "Program Files (x86)",
        "Microsoft",
        "Edge",
        "Application",
        "msedge.exe"
    )
    
    FIREFOX = os.path.join(
        "C:\\",
        "Program Files",
        "Mozilla Firefox",
        "firefox.exe"
    )
    
    OPERA = os.path.join(
        os.path.expanduser("~"),
        "AppData",
        "Local",
        "Programs",
        "Opera GX",
        "opera.exe"
    )
    
    BRAVE = os.path.join(
        "C:\\",
        "Program Files",
        "BraveSoftware",
        "Brave-Browser",
        "Application",
        "brave.exe"
    )
    
    STEAM = os.path.join(
        "C:\\",
        "Program Files (x86)",
        "Steam",
        "steam.exe"
    )
        
    
    VCODE = os.path.join(
        os.path.expanduser("~"),
        "AppData",
        "Local",
        "Programs",
        "Microsoft VS Code",
        "Code.exe"
    )
        
    
    # INTELLJ = os.path.join(
        
    # )
    
    # PYCHARM = os.path.join(
        
    # )
    
    WORKBENCH = os.path.join(
        os.path.expanduser("~"),
        "AppData",
        "Local",
        "Programs",
        "MySQL",
        "MySQL Workbench",
        "MySQL Workbench.exe"
    )
        
    
    # ECLIPSE = os.path.join(
        
    # )
    
    # WORD = os.path.join(
        
    # )
    
    # EXCEL = os.path.join(
        
    # )
    
    # POWERPOINT = os.path.join(
        
    # )
    
    # ACCESS = os.path.join(
        
    # )
    
    # OUTLOOK = os.path.join(
        
    # )
    
    # PUBLISHER = os.path.join(
        
    # )
    
    # VICIO = os.path.join(
        
    # )