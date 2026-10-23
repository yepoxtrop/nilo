import os
import subprocess
import time 

from ..models.programs import WindowsBasics
from ..utils.logs import Logs
from ..utils.resource_path import resource_path


def _show_error() -> None:
    error_script = resource_path(
        "src", "backend", "utils", "message-error", "message_error1.vbs"
    )
    subprocess.Popen(["cscript", "//nologo", str(error_script)])

class Explorer():
    
    @staticmethod
    def open_explorer(folder:str|None = None, number_repeat:int = 10):
        
        if os.path.exists(WindowsBasics.EXPLORER.value):
            
            number = 0;
            try:
                
                if folder is None:
                    
                    while number<number_repeat:
                        subprocess.Popen(
                            [WindowsBasics.EXPLORER.value],
                        )
                        number += 1;
                else:
                    
                    while number<number_repeat:
                        
                        subprocess.Popen(
                            [WindowsBasics.EXPLORER.value, folder],
                        )
                        number += 1;
            except Exception as error:
                Logs.error("No se pudo abrir el Explorador en la broma open_explorer", error)
                _show_error()
        else:
            
            number = 0;
            try:
                
                if folder is None:
                    
                    while number<number_repeat:
                        subprocess.run(
                            ["explorer.exe"],
                        )
                        number += +1;
                else:
                    
                    while number<number_repeat:
                        subprocess.Popen(
                            ["explorer.exe", folder],
                        )
                        number += +1;
            except Exception as error:
                Logs.error("No se pudo abrir el Explorador en la broma open_explorer", error)
                _show_error()

    # Este es el más jugueton
    
    @staticmethod
    def stop_explorer():
        
        # Detiene
        subprocess.Popen(
            ["taskkill",  "/F", "/IM","explorer.exe"]
        )
        
        time.sleep(2)
        
        #Vetenana alerta
        _show_error()
        time.sleep(7)
        
        #Inicia
        try:
            if os.path.exists(WindowsBasics.EXPLORER.value):
                subprocess.Popen([WindowsBasics.EXPLORER.value])
            else:
                subprocess.Popen(["start", "explorer.exe"])
        except Exception as error:
            Logs.error("No se pudo reiniciar el Explorador en la broma stop_explorer", error)
            subprocess.Popen(["start", "explorer.exe"])

        #Ejecuta ventanas de sys32
        Explorer.open_explorer(folder="C:\\Windows\\System32", number_repeat=2)
        
        