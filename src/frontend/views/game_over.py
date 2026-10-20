import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import subprocess
import time

from ...backend import check_path
from ...backend.models.programs import WindowsInstalled
from ...backend.models.questions import QuestionMultiple, QuestionSimple

class GameOverView():
    
    def __init__(self, main_view:tk.Tk):
        self.main_view = main_view;
        self.show_game_over_view();
        
    def show_game_over_view(self):
        self.game_over = tk.Frame(self.main_view)
        self.game_over.pack(
            fill="both", 
            expand=True,
        )
        self.game_over.configure(
            background="#000000"
        )
        
        img_game0 = Image.open("./src/frontend/media/loser.jpg")
        img_game1 = img_game0.resize((600,300),  Image.Resampling.LANCZOS)
        self.img_game = ImageTk.PhotoImage(img_game1)
                
        self.label = tk.Label(self.game_over, image=self.img_game)
        self.label.image = self.img_game
        self.label.place(x=-100, y=200)
        self.label.configure(
            background="#000000"
        )
        
        
        img_game_title0 = Image.open("./src/frontend/media/title2.jpg")
        img_game_title1 = img_game_title0.resize((400,200),  Image.Resampling.LANCZOS)
        self.img_game_title = ImageTk.PhotoImage(img_game_title1)
                
        self.label_game_title = tk.Label(self.game_over, image=self.img_game_title)
        self.label_game_title.image = self.img_game_title
        self.label_game_title.place(x=50, y=30)
        self.label_game_title.configure(
            background="#000000"
        )