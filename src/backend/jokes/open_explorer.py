import os
import subprocess
import time 

from ..models.programs import WindowsBasics

class Explorer():
    
    def open_explorer(folder:str|None = None):
        
        if os.path.exists(WindowsBasics.EXPLORER.value):
            
            number = 0;
            try:
                
                if folder is None:
                    
                    while number<11:
                        subprocess.Popen(
                            [WindowsBasics.EXPLORER.value],
                        )
                        number += 1;
                else:
                    
                    while number<11:
                        
                        subprocess.Popen(
                            [WindowsBasics.EXPLORER.value, folder],
                        )
                        number += 1;
            except:
                
                subprocess.Popen("cscript", "src\\backend\\utils\\message-error\\message_error1.vbs")
        else:
            
            number = 0;
            try:
                
                if folder is None:
                    
                    while number<11:
                        subprocess.run(
                            ["explorer.exe"],
                        )
                        number += +1;
                else:
                    
                    while number<11:
                        subprocess.Popen(
                            ["explorer.exe", folder],
                        )
                        number += +1;
            except:
                subprocess.Popen(["cscript", "src\\backend\\utils\\message-error\\message_error1.vbs"])

    # Este es el más jugueton
    
    def stop_explorer():
        
        # Detiene
        subprocess.Popen(
            ["taskkill",  "/F", "/IM","explorer.exe"]
        )
        
        time.sleep(2)
        
        #Vetenana alerta
        subprocess.Popen(["cscript", "src\\backend\\utils\\message-error\\message_error1.vbs"])
        time.sleep(7)
        
        #Inicia
        if os.path.exists(WindowsBasics.EXPLORER.value):
            subprocess.Popen(["start", WindowsBasics.EXPLORER.value])
        else:
            subprocess.Popen(["start", "explorer.exe"])
            
        #Ejecuta ventanas de sys32
        Explorer.open_explorer(folder="C:\\Windows\\System32")