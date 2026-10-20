

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import subprocess
import time

from ...backend import check_path
from ...backend.models.programs import WindowsInstalled
from ...backend.models.questions import QuestionMultiple, QuestionSimple


class WinGameView():
    
    def __init__(self, main_view:tk.Tk):
        self.main_view = main_view;
        self.show_win_game_view();
        
    def show_win_game_view(self):
        self.win_game = tk.Frame(self.main_view)
        self.win_game.pack(
            fill="both", 
            expand=True,
        )
        self.win_game.configure(
            background="#000000"
        )
        
        img_game0 = Image.open("./src/frontend/media/winner.jpg")
        img_game1 = img_game0.resize((500,300),  Image.Resampling.LANCZOS)
        self.img_game = ImageTk.PhotoImage(img_game1)
                
        self.label = tk.Label(self.win_game, image=self.img_game)
        self.label.image = self.img_game
        self.label.place(x=0, y=200)
        self.label.configure(
            background="#000000"
        )
        
        
        img_game_title0 = Image.open("./src/frontend/media/title3.jpg")
        img_game_title1 = img_game_title0.resize((400,200),  Image.Resampling.LANCZOS)
        self.img_game_title = ImageTk.PhotoImage(img_game_title1)
                
        self.label_game_title = tk.Label(self.win_game, image=self.img_game_title)
        self.label_game_title.image = self.img_game_title
        self.label_game_title.place(x=50, y=30)
        self.label_game_title.configure(
            background="#000000"
        )