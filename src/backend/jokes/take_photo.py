import os
import shutil
import subprocess
import time 
import keyboard
from pathlib import Path

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
        Camera.reply_photo("pics", str(Path.home() / "Desktop"))
                
                
    def take_screen_shot():    
        try:
            keyboard.send('windows+print screen')
        except:
            subprocess.Popen("cscript", "src\\backend\\utils\\message-error\\message_error1.vbs")    
        time.sleep(1)
        Camera.reply_photo(
            str(Path.home() / "Pictures" / "Screenshots"),
            str(Path.home() / "Desktop"),
        )
            
    def reply_photo(path_origin:str, path_destination:str):
        origin = Path(path_origin)
        destination = Path(path_destination)
        image_extensions = {".bmp", ".gif", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}

        if not origin.is_dir():
            Camera._show_photo_error(f"No existe la carpeta de origen: {origin}")
            return

        photos = [
            path for path in origin.iterdir()
            if path.is_file() and path.suffix.lower() in image_extensions
        ]
        if not photos:
            Camera._show_photo_error(f"No se encontraron fotos en la carpeta: {origin}")
            return

        latest_photo = max(photos, key=lambda path: path.stat().st_mtime_ns)
        destination.mkdir(parents=True, exist_ok=True)
        existing_names = {path.name.casefold() for path in destination.iterdir()}
        copies_made = 0
        copy_number = 1

        while copies_made < 15:
            copy_name = f"{latest_photo.stem}_{copy_number}{latest_photo.suffix}"
            copy_number += 1
            if copy_name.casefold() in existing_names:
                continue

            shutil.copy2(latest_photo, destination / copy_name)
            existing_names.add(copy_name.casefold())
            copies_made += 1

    def _show_photo_error(message: str):
        
        subprocess.Popen(["cscript", "src\\backend\\utils\\message-error\\message_error6.vbs"])
