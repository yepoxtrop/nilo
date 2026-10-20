import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import subprocess
import random

from ...backend import check_path
from ...backend.models.programs import WindowsInstalled
from ...backend.models.questions import QuestionMultiple, QuestionSimple

from ..modals import RateProgram
from .question import QuestionView

class IndexView():
    
    def __init__(self, main_view:tk.Tk, lifes:int, questions:int):
        
        self.main_view = main_view;
        self.lifes = lifes;
        self.questions = questions;
        
        self.show_view();
        
    def show_view(self):
        self.index = tk.Frame(self.main_view)
        self.index.pack(
            fill="both", 
            expand=True,
        )
        self.index.configure(
            background="#000000"
        )
        
        img_title0 = Image.open("./src/frontend/media/title.jpg")
        img_title1 = img_title0.resize((500,180),  Image.Resampling.LANCZOS)
        self.img_title = ImageTk.PhotoImage(img_title1)
        
        img0 = Image.open("./src/frontend/media/laughtv2.jpg")
        img1 = img0.resize((380,360),  Image.Resampling.LANCZOS)
        self.img_pet_game = ImageTk.PhotoImage(img1)
        
        label = tk.Label(self.index, image=self.img_pet_game)
        label.place(x=-15, y=140)
        label.configure(
            background="#000000"
        )
        
        label_title  = tk.Label(self.index, image=self.img_title)
        label_title.place(x=0, y=0)
        label_title.configure(
            background="#000000"
        )
        
        
        frame_btn = tk.Frame(self.index)
        frame_btn.place(x=350, y=250)
        frame_btn.configure(
            background="#000000"
        )
        
        btn1 = tk.Button(frame_btn, text="START", command=self.start_game)
        btn2 = tk.Button(frame_btn, text="SURPRISE", command=self.surprise_program)
        btn3 = tk.Button(frame_btn, text="EXIT", command=self.close_program)
        btn4 = tk.Button(frame_btn, text="RATE US", command=self.rate_program)
        button_styles = (
            (btn1, "#4B1768", "#762A91"),
            (btn2, "#351044", "#762A91"),
            (btn4, "#351044", "#762A91"),
            (btn3, "#681D36", "#922747"),
        )
        for button, background, hover_background in button_styles:
            button.configure(
                background=background,
                foreground="#FFFFFF",
                activebackground=hover_background,
                activeforeground="#FFFFFF",
                font=("Segoe UI", 11, "bold"),
                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                cursor="hand2",
                padx=18,
                pady=9,
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
            button.pack(fill="x", expand=True, pady=7)
        
    #Close program
    def close_program(self):
        respuesta = messagebox.askyesno(title="Finalizar programa", message="¿Deseas salir?")
        if respuesta:
            self.main_view.destroy();
        else:
            print("El usuario presionó No")
    
    #Rate program
    def rate_program(self):
        modal = RateProgram(main_view=self.main_view, title="Rate the program")
        
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
    
    def start_game(self):
        list_questions = []
        
        random_number = random.randint(1, self.questions)
        questions_multiple = random_number
        questions_simple = self.questions - questions_multiple
        
        for i in range(questions_multiple):
            while True:
                number = random.randint(0, len(QuestionMultiple.QUESTION.value)-1)
                question = QuestionMultiple.QUESTION.value[number]
                if not question in list_questions:
                    list_questions.append(question)
                    break
                
        for i in range(questions_simple):        
            while True:
                number = random.randint(0, len(QuestionSimple.QUESTION.value)-1)
                question = QuestionSimple.QUESTION.value[number]
                if not question in list_questions:
                    list_questions.append(question)
                    break
                
        
        self.close_view()
        self.question_view = QuestionView(
            main_view=self.main_view,
            lifes=self.lifes,
            questions=self.questions,
            list_questions=list_questions
        )
    
    def close_view(self):
        self.index.pack_forget();