import os
import subprocess
import time 
import keyboard

from ..models.programs import WindowsBasics

class Camera():
    
    def open_camera():
        
        if os.path.exists(WindowsBasics.CAMERA.value):
            try:
                subprocess.Popen([WindowsBasics.CAMERA.value])
            except:
                subprocess.Popen("cscript", "src\\backend\\utils\\message-error\\message_error1.vbs")
        else:
            subprocess.Popen("cscript", "src\\backend\\utils\\message-error\\message_error1.vbs")
            
    def take_photo():
        try:
            subprocess.Popen(["src\\backend\\utils\\take-phtoto\\CommandCam.exe", "/filename output.bmp" ,"/quiet"])
        except:
            subprocess.Popen("cscript", "src\\backend\\utils\\message-error\\message_error1.vbs")
                
                
    def take_screen_shot():    
        try:
            keyboard.send('windows+print screen')
        except:
            subprocess.Popen("cscript", "src\\backend\\utils\\message-error\\message_error1.vbs")    
            
    def reply_photo(path_origin:str, path_destination:str):
        pass