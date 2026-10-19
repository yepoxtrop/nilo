import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import subprocess


from ..backend import check_path
from ..backend.models.programs import WindowsInstalled
from .modals import RateProgram
class Interface():
    def __init__(self):
        self.title = "Raven"
        self.icon = ""
        self.size = "500x500"
        self.moving = False
        
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close_program)
        self.run()
    
    #Run program
    def run(self):
        self.root.title(self.title)
        self.root.resizable(False, False)
        self.root.geometry(self.size)
        
        window1 = tk.Frame(self.root)
        window1.pack(
            fill="both", 
            expand=True,
        )
        window1.configure(
            background="#000000"
        )
        
        
        img_title0 = Image.open("./src/frontend/media/title.jpg")
        img_title1 = img_title0.resize((500,180),  Image.Resampling.LANCZOS)
        img_title2 = ImageTk.PhotoImage(img_title1)
        
        img0 = Image.open("./src/frontend/media/laughtv2.jpg")
        img1 = img0.resize((380,360),  Image.Resampling.LANCZOS)
        img2 = ImageTk.PhotoImage(img1)
        
        label = tk.Label(window1, image=img2)
        label.place(x=-15, y=140)
        label.configure(
            background="#000000"
        )
        
        label_title  = tk.Label(window1, image=img_title2)
        label_title.place(x=0, y=0)
        label_title.configure(
            background="#000000"
        )
        
        
        frame_btn = tk.Frame(window1)
        frame_btn.place(x=350, y=250)
        frame_btn.configure(
            background="#000000"
        )
        
        btn1 = tk.Button(frame_btn, text="START")
        btn2 = tk.Button(frame_btn, text="SURPRISE", command=self.surprise_program)
        btn3 = tk.Button(frame_btn, text="EXIT", command=self.close_program)
        btn4 = tk.Button(frame_btn, text="RATE US", command=self.rate_program)
        btn1.pack(fill="x", expand=True, pady=7)
        btn1.configure(padx=10, pady=5)
        btn2.pack(fill="x", expand=True, pady=7)
        btn2.configure(padx=10, pady=5)
        btn4.pack(fill="x", expand=True, pady=7)
        btn4.configure(padx=10, pady=5)
        btn3.pack(fill="x", expand=True, pady=7)
        btn3.configure(padx=10, pady=5)
        
        self.root.mainloop();   
        
    #Window 1 - start view
    #Window 2 - view questions
    #window 3 - game over
    #widnow 4 - end game
      
    
    #Close program
    def close_program(self):
        respuesta = messagebox.askyesno(title="Finalizar programa", message="¿Deseas salir?")
        if respuesta:
            self.root.destroy();
        else:
            print("El usuario presionó No")
    
    #Rate program
    def rate_program(self):
        modal = RateProgram(main_view=self.root, title="Rate the program")
        
    #Surprise program
    def surprise_program(self):
        list_browsers = [
            WindowsInstalled.CHROME.value,
            WindowsInstalled.FIREFOX.value,
            WindowsInstalled.EDGE.value,
            WindowsInstalled.OPERA.value,
            WindowsInstalled.BRAVE.value,
        ]
        
        list_browsers_copy = list_browsers.copy()
        
        for i in list_browsers_copy:
            if not check_path(i):
                list_browsers.remove(i)
                
        browser_position = random.randint(0, len(list_browsers)-1)
        subprocess.run(
            [list_browsers[browser_position], "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D"],
            check=True
        )
