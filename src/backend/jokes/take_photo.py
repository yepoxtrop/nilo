import os
import shutil
import subprocess
import time 
import keyboard
from pathlib import Path

from ..models.programs import WindowsBasics
from ..utils.logs import Logs
from ..utils.resource_path import resource_path


def _run_message_script(script_name: str) -> None:
    script_path = resource_path(
        "src", "backend", "utils", "message-error", script_name
    )
    subprocess.Popen(["cscript", "//nologo", str(script_path)])

class Camera():
    
    @staticmethod
    def open_camera():
        
        if os.path.exists(WindowsBasics.CAMERA.value):
            try:
                subprocess.Popen([WindowsBasics.CAMERA.value])
            except OSError as error:
                Logs.error("No se pudo abrir la cámara", error)
                _run_message_script("message_error6.vbs")
        else:
            Logs.error(f"No se encontró la aplicación de cámara: {WindowsBasics.CAMERA.value}")
            _run_message_script("message_error6.vbs")
            
    @staticmethod
    def take_photo():
        try:
            camera_executable = resource_path(
                "src", "backend", "utils", "take-phtoto", "CommandCam.exe"
            )
            subprocess.Popen([str(camera_executable), "/filename output.bmp", "/quiet"])
        except OSError as error:
            Logs.error("No se pudo iniciar la captura de foto", error)
            _run_message_script("message_error1.vbs")
        Camera.reply_photo("pics", str(Path.home() / "Desktop"))
                
                
    @staticmethod
    def take_screen_shot():    
        try:
            keyboard.send('windows+print screen')
        except Exception as error:
            Logs.error("No se pudo tomar la captura de pantalla", error)
            _run_message_script("message_error1.vbs")
        time.sleep(1)
        Camera.reply_photo(
            str(Path.home() / "Pictures" / "Screenshots"),
            str(Path.home() / "Desktop"),
        )
        _run_message_script("message_error2.vbs")
            
    @staticmethod
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

    @staticmethod
    def _show_photo_error(message: str):
        Logs.error(message)
        _run_message_script("message_error6.vbs")
