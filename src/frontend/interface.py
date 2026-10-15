import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Interface():
    def __init__(self):
        self.title = "Raven"
        self.icon = ""
        self.size = "500x500"
        self.moving = False
        
        self.run()
    
    def run(self):
        root = tk.Tk()
        root.title(self.title)
        root.resizable(True, True)
        root.geometry(self.size)
        
        window1 = tk.Frame(root)
        window1.pack(
            fill="both", 
            expand=True,
        )
        window1.configure(
            background="#000000"
        )
        
        img0 = Image.open("./src/frontend/media/laughtv2.jpg")
        img1 = img0.resize((400,400),  Image.Resampling.LANCZOS)
        img2 = ImageTk.PhotoImage(img1)
        
        label = tk.Label(window1, image=img2)
        label.place(x=-15, y=100)
        label.configure(
            background="#000000"
        )
        
        btn1 = tk.Button(window1, text="START");
        btn1.pack()
        
        root.mainloop();        
        
ejemplo = Interface();