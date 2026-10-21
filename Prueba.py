from src.backend.jokes import Explorer
import keyboard

# Explorer.stop_explorer()

# Función que quieres ejecutar
import keyboard
import time
#keyboard.send('win+ctrl+shift+b') 
#keyboard.send('alt+tab') 
#keyboard.send('win')

# keyboard.send('win+r')
# keyboard.write('powershell')
# keyboard.send('enter')

#keyboard.send('windows+print screen')
#keyboard.write('el que lo lea es gay')
# keyboard.send('enter')

# keyboard.write('cd C:\\')
# keyboard.send('enter')
# keyboard.write('tree')
# keyboard.send('enter')



#keyboard.send('shift+win+s')

keyboard.press("win")
num = 0
while num<100:
    time.sleep(1)
    keyboard.send("right") 
    keyboard.send("up") 
    keyboard.send("down") 
    keyboard.send("left") 
    num += 1
keyboard.release("win")


















