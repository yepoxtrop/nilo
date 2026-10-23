import keyboard
import time
import subprocess
import webbrowser

from ..models.programs import WindowsBasics, WindowsInstalled
from ..utils.logs import Logs
from ..utils.resource_path import resource_path


class KeyboardCommand():
    
    @staticmethod
    def tab_loop(number:int = 100):
        keyboard.press("alt") 
        num = 0
        while num<number:
            time.sleep(0.01)
            keyboard.send("tab") 
            num += 1

        keyboard.release("alt")
    
    @staticmethod
    def move_window(number:int = 10):
        
        try:
            subprocess.Popen([WindowsBasics.EXPLORER.value])
        except OSError as error:
            Logs.error("No se pudo abrir el Explorador para la broma move_window", error)
            subprocess.Popen(["start","explorer.exe"])
        KeyboardCommand.tab_loop(number=1)
        time.sleep(1)
        
        keyboard.press("win")
        num = 0
        while num<number:
            time.sleep(1)
            keyboard.send("right") 
            keyboard.send("up") 
            keyboard.send("down") 
            keyboard.send("left") 
            num += 1
        keyboard.release("win")
        
    @staticmethod
    def min_view(number:int = 10):
        keyboard.press("win")
        num = 0
        while num<number:
            time.sleep(1)
            keyboard.send("d")
            num += 1
        keyboard.release("win")
        
    @staticmethod
    def min_win():
        keyboard.send("win+;")
    
    @staticmethod
    def virtual_keyboard():
        keyboard.send("win+Ctrl+o")
        time.sleep(1)
        keyboard.press("ctrl")
        keyboard.press("alt")
        keyboard.press("shift")
        
        time.sleep(5)
        keyboard.release("ctrl")
        keyboard.release("alt")
        keyboard.release("shift")
        
    @staticmethod
    def configure():
        keyboard.send("win+I")
        
    @staticmethod
    def zoom_view():
        try:
            try:
                subprocess.Popen([WindowsInstalled.ZOOM.value])
            except:
                keyboard.send("win+plus")
                
            time.sleep(5)
            zoom_steps = 9
            for _ in range(zoom_steps):
                keyboard.send("win+plus")
                time.sleep(0.1)

            time.sleep(5)
            for _ in range(zoom_steps):
                keyboard.send("win+subtract")
                time.sleep(0.1)
        except Exception as error:
            Logs.error("Falló la broma zoom_view", error)
            error_script = resource_path(
                "src", "backend", "utils", "message-error", "message_error7.vbs"
            )
            subprocess.Popen(["cscript", "//nologo", str(error_script), "Magnify.exe"])
    
    @staticmethod
    def query_random():
        webbrowser.open_new("https://www.google.com/search?q=hola+bro+como+estás?+Bro+Ayudame+a+brickear+una+play+5&sca_esv=1abbeb06ea3e1696&sxsrf=APpeQnv2Q8GyDhnRye6ZU4HPGB29A27kXQ%3A1792766530028&source=hp&ei=QXLbavKsPPG2wt0P68vGkA8&iflsig=ABILxe8AAAAAatuAUn63yOdHsHuTLF6C_7vj1duStKmG&ved=0ahUKEwiy0b3hr9CXAxVxm7AFHeulEfIQ4dUDCCk&uact=5&oq=hola+nrp&gs_lp=Egdnd3Mtd2l6Ighob2xhIG5ycDIFECEYoAEyBRAhGKABMgUQIRigATIFECEYnwUyBRAhGJ8FMgUQIRifBTIFECEYnwUyBRAhGJ8FSLMPUABY6QpwAHgAkAEAmAHRAaAB_giqAQUwLjcuMbgBA8gBAPgBAZgCCKACkArCAgQQIxgnwgIKEAAYgAQYigUYQ8ICCxAAGIAEGLEDGIMBwgIIEAAYgAQYsQPCAhEQLhiABBixAxjHARivARiOBcICDhAuGIAEGLEDGMcBGNEDwgIOEAAYgAQYigUYjQYYsQPCAhAQABiABBiKBRhDGLEDGIMBwgIIEC4YgAQYsQPCAgUQABiABMICCBAAGIAEGLQHwgIKEAAYgAQYsQMYCsICBRAuGIAEwgIGEAAYFhgewgIFEAAY7wXCAggQABiABBiiBJgDAJIHBTAuNi4yoAeaRbIHBTAuNi4yuAeQCsIHBzItMi41LjHIB2qACAE&sclient=gws-wiz")
        
    @staticmethod
    def fls_tree():
        keyboard.send("win+r")
        time.sleep(0.5)
        keyboard.write("cmd")
        keyboard.send("enter")
        time.sleep(1)
        keyboard.write("cd C:\\")
        keyboard.send("enter")
        keyboard.write("tree")
        keyboard.send("enter")