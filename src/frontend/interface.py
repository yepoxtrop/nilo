import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import subprocess


from ..backend import check_path
from ..backend.models.programs import WindowsInstalled
from .modals import RateProgram
from .views import IndexView
class Interface():
    def __init__(self):
        self.title = "Raven"
        self.icon = ""
        self.size = "500x500"
        self.moving = False
        self.lifes = 5
        self.question = 20
        
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.resizable(False, False)
        self.root.geometry(self.size)
        self.root.configure(
            background="#000000"
        )
        
        self.root.protocol("WM_DELETE_WINDOW", self.close_program)
        
        self.Index_run()
        self.root.mainloop();  
    
    #Run Index view
    def Index_run(self):
        index_view = IndexView(main_view=self.root, questions=self.question, lifes=self.lifes)
        
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
