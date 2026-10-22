import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import subprocess

from ..resource_path import resource_path


class RateProgram():
    
    def __init__(self, main_view:tk.Tk|tk.Frame, title:str = "Rate program", geometry:str = "600x270"):
        
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
        self.modal.configure(background="#000000")

        title_modal = tk.Label(
            self.modal,
            text="RATE OUR GAME",
            background="#000000",
            foreground="#A855D1",
            font=("Segoe UI", 20, "bold"),
        )
        title_modal.pack(pady=(12, 8))

        frame_modal_btn = tk.Frame(self.modal, background="#000000")
        frame_modal_btn.pack(fill="x", padx=12)
        
        label_terms = tk.Label(
            self.modal, 
            text="Hi bro, friend or enemy, I don't know, but I know that You should to give us a good calification for our game, but that is not obligatory, if You don't want to give us a great calification, don't worry, nothing bad happen :D.\n\nWell maybe you shouldn't trust us, forget the last, and We will wish You enjoy our game.\n\nPostdata:Don't worry, nothing bad will happen to your computer, enjoy the game ¯\\_(ツ)_/¯",
            wraplength=550,
            justify="left",
            font=("Segoe UI", 10),
            background="#000000",
            foreground="#E5DDEA",
        )
        
        btn1 = tk.Button(frame_modal_btn, text="1", pady=10, command=lambda: self.wrong(frame_modal_btn, label_terms))
        btn2 = tk.Button(frame_modal_btn, text="2", pady=10, command=lambda: self.wrong(frame_modal_btn, label_terms))
        btn3 = tk.Button(frame_modal_btn, text="3", pady=10, command=lambda: self.wrong(frame_modal_btn, label_terms))
        btn4 = tk.Button(frame_modal_btn, text="4", pady=10, command=lambda: self.wrong(frame_modal_btn, label_terms))
        btn5 = tk.Button(frame_modal_btn, text="5", pady=10, command=lambda: self.excelent(frame_modal_btn, label_terms))
        
        button_styles = (
            (btn1, "#351044", "#762A91"),
            (btn2, "#401450", "#762A91"),
            (btn3, "#4B1768", "#8736A3"),
            (btn4, "#5A1A70", "#8736A3"),
            (btn5, "#681D36", "#922747"),
        )
        for button, background, hover_background in button_styles:
            button.configure(
                background=background,
                foreground="#FFFFFF",
                activebackground=hover_background,
                activeforeground="#FFFFFF",
                font=("Segoe UI", 12, "bold"),
                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                cursor="hand2",
                padx=10,
                pady=8,
            )
            button.bind(
                "<Enter>",
                lambda _event, current=button, color=hover_background: current.configure(
                    background=color
                ),
            )
            button.bind(
                "<Leave>",
                lambda _event, current=button, color=background: current.configure(
                    background=color
                ),
            )
            button.pack(side="left", fill="x", expand=True, padx=6, pady=4)

        label_terms.pack(fill="x", padx=20, pady=(10, 14))
        
    def wrong(self, frame:tk.Frame, label:tk.Label):
        frame.pack_forget()
        label.pack_forget()
        
        img = Image.open(
            resource_path("src", "frontend", "media", "memes", "deception.jpg")
        )
        img1 = img.resize((500,180),  Image.Resampling.LANCZOS)
        self.wrong_image = ImageTk.PhotoImage(img1)
        
        label = tk.Label(self.modal, image=self.wrong_image, background="#000000")
        label.pack()
    
    def excelent(self, frame:tk.Frame, label:tk.Label):
        frame.pack_forget()
        label.pack_forget()
        
        img = Image.open(
            resource_path("src", "frontend", "media", "memes", "winner.jpg")
        )
        img1 = img.resize((500,180),  Image.Resampling.LANCZOS)
        self.good_image = ImageTk.PhotoImage(img1)
        
        label = tk.Label(self.modal, image=self.good_image, background="#000000")
        label.pack()