import keyboard
import time

class KeyboardCommand():
    
    def tab_loop():
        keyboard.press("alt") 
        num = 0
        while num<100:
            time.sleep(0.01)
            keyboard.send("tab") 
            num += 1

        keyboard.release("alt")
    
    def move_window():
        keyboard.press("win")
        num = 0
        while num<15:
            time.sleep(1)
            keyboard.send("right") 
            keyboard.send("up") 
            keyboard.send("down") 
            keyboard.send("left") 
            num += 1
        keyboard.release("win")
        
    def min_view():
        keyboard.press("win")
        num = 0
        while num<15:
            time.sleep(1)
            keyboard.send("d")
            num += 1
        keyboard.release("win")
        
    def min_win():
        keyboard.send("win+;")
        
    def min_win():
        keyboard.send("win+;")
    
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
        
    def configure():
        keyboard.send("win+I")
        
    def zoom_view():
        zoom_steps = 9
        for _ in range(zoom_steps):
            keyboard.send("win+plus")
            time.sleep(0.1)

        time.sleep(5)
        for _ in range(zoom_steps):
            keyboard.send("win+subtract")
            time.sleep(0.1)
    
    def query_random():
        keyboard.press("win")
        keyboard.send("q")
        keyboard.release("win")
        keyboard.write("Cómo hago para piratear una play 5, yo sé que tu sabes que yo sé que sabes")
        keyboard.send("enter")
    
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
        