import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import subprocess

class RateProgram():
    
    def __init__(self, main_view:tk.Tk|tk.Frame, title:str = "Rate program", geometry:str = "600x230"):
        
        self.main_view = main_view;
        self.title = title
        self.geomtry = geometry
        self.modal = tk.Toplevel(self.main_view)
        
        self.show_modal();
        
        
        
    def show_modal(self):
        self.modal.grab_set()
        self.modal.title(self.title)
        self.modal.geometry(self.geomtry)
        self.modal.resizable(False, False)
        
        title_modal = tk.Label(self.modal, text="RATE OUR GAME")
        title_modal.configure(font=("Arial", 20))
        title_modal.pack();
        
        frame_modal_btn = tk.Frame(self.modal)
        frame_modal_btn.pack(fill="x")
        
        label_terms = tk.Label(
            self.modal, 
            text="Hi bro, friend or enemy, I don't know, but I know that You should to give us a good calification for our game, but that is not obligatory, if You don't want to give us a great calification, don't worry, nothing bad happen :D.\n\nWell maybe you shouldn't trust us, forget the last, and We will wish You enjoy our game.\n\nPostdata:Don't worry, nothing bad will happen to your computer, enjoy the game ¯\\_(ツ)_/¯",
            wraplength=580,
            justify="left",
            font=("Arial", 10)
        )
        
        btn1 = tk.Button(frame_modal_btn, text="1", pady=10, command=lambda: self.wrong(frame_modal_btn, label_terms))
        btn2 = tk.Button(frame_modal_btn, text="2", pady=10, command=lambda: self.wrong(frame_modal_btn, label_terms))
        btn3 = tk.Button(frame_modal_btn, text="3", pady=10, command=lambda: self.wrong(frame_modal_btn, label_terms))
        btn4 = tk.Button(frame_modal_btn, text="4", pady=10, command=lambda: self.wrong(frame_modal_btn, label_terms))
        btn5 = tk.Button(frame_modal_btn, text="5", pady=10, command=lambda: self.excelent(frame_modal_btn, label_terms))
        
        btn1.pack(side="left", fill="x", expand=True, padx=10)
        btn2.pack(side="left", fill="x", expand=True, padx=10)
        btn3.pack(side="left", fill="x", expand=True, padx=10)
        btn4.pack(side="left", fill="x", expand=True, padx=10)
        btn5.pack(side="left", fill="x", expand=True, padx=10)
        
        label_terms.pack(pady=10)
        
    def wrong(self, frame:tk.Frame, label:tk.Label):
        frame.pack_forget()
        label.pack_forget()
        
        img = Image.open("./src/frontend/media/memes/deception.jpg")
        img1 = img.resize((500,180),  Image.Resampling.LANCZOS)
        self.wrong_image = ImageTk.PhotoImage(img1)
        
        label = tk.Label(self.modal, image=self.wrong_image)
        label.pack()
    
    def excelent(self, frame:tk.Frame, label:tk.Label):
        frame.pack_forget()
        label.pack_forget()
        
        img = Image.open("./src/frontend/media/memes/winner.jpg")
        img1 = img.resize((500,180),  Image.Resampling.LANCZOS)
        self.good_image = ImageTk.PhotoImage(img1)
        
        label = tk.Label(self.modal, image=self.good_image)
        label.pack()