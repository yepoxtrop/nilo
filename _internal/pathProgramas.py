import os;

pathProgramas = [
    #os.path.join("C:\\","Program Files","WindowsApps","Microsoft.Windows.Photos_2025.11080.28001.0_x64__8wekyb3d8bbwe","Photos.exe"),
    os.path.join("C:\\","Program Files","WindowsApps","Microsoft.WindowsCamera_2025.2505.2.0_x64__8wekyb3d8bbwe","WindowsCamera.exe"), #Canara
    os.path.join("C:\\","Program Files","WindowsApps","Microsoft.WindowsNotepad_11.2507.26.0_x64__8wekyb3d8bbwe","Notepad","Notepad.exe"), #Notepad
    os.path.join("C:\\","Program Files","WindowsApps","Microsoft.Paint_11.2508.361.0_x64__8wekyb3d8bbwe","PaintApp","mspaint.exe"), #paint
    os.path.join("C:\\","Windows","explorer.exe"), #Explorador de archivos
    
    #Navegadores
    os.path.join("C:\\","Program Files","Google", "Chrome" ,"Application", "chrome.exe"), #Chrome
    os.path.join("C:\\","Program Files","Mozilla Firefox", "firefox.exe"), #Firefox
    os.path.join("C:\\","Users",f"{os.getenv("USERNAME")}", "AppData","Local","Programs","Opera GX","opera.exe"), #Opera GX
    os.path.join("C:\\","Program Files (x86)","Microsoft","Edge","Application","msedge.exe"), #Edge
    os.path.join("C:\\","Program Files","BraveSoftware","Brave-Browser","Application","brave.exe") #Brave
]