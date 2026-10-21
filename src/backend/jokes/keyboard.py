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
        keyboard.press("window")
        num = 0
        while num<100:
            time.sleep(1)
            keyboard.send("right") 
            keyboard.send("up") 
            keyboard.send("down") 
            keyboard.send("left") 
            num += 1
        keyboard.release("window")
    
    def fls_tree():
        pass