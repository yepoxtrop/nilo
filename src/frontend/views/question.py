import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import subprocess
import time

from ...backend import check_path
from ...backend.jokes import JOKES
from ...backend.models.programs import WindowsInstalled
from ...backend.models.questions import QuestionMultiple, QuestionSimple
from ..resource_path import resource_path
from .game_over import GameOverView
from .win_game import WinGameView

class QuestionView():
    
    def __init__(self, main_view:tk.Tk, lifes:int, questions:int, list_questions:list):
        self.main_view = main_view
        self.lifes = lifes
        self.questions = questions
        self.list_questions = list_questions
        self.question = tk.Frame(self.main_view)
        self.timer_id = None
        
        if self.lifes>0 and self.questions>0:
            self.show_question()
            self.timer_id = self.question.after(1000, self.time_out)
        elif self.lifes == 0:
            self.game_over_view = GameOverView(main_view=self.main_view)
            self.question.destroy()
        elif self.lifes > 0 and self.questions == 0:
            self.win_game_view = WinGameView(main_view=self.main_view)
            self.question.destroy()
    
    def show_question(self):
        
        self.question.pack(
            fill="both", 
            expand=True,
        )
        self.time = 300
        self.question.configure(
            background="#000000"
        )
        
        img_frame0 = Image.open(
            resource_path("src", "frontend", "media", "frame.png")
        )
        img_frame = img_frame0.resize((200, 100), Image.Resampling.LANCZOS).convert("RGBA")
        
        img_shield0 = Image.open(
            resource_path("src", "frontend", "media", "shield_wbk.png")
        )
        img_shield = img_shield0.resize((100, 100), Image.Resampling.LANCZOS).convert("RGBA")
        
        img_header = Image.new("RGBA", (240, 100), (0, 0, 0, 0))
        img_header.alpha_composite(img_frame, dest=(40, 0))
        img_header.alpha_composite(img_shield, dest=(0, 0))
        self.img_header = ImageTk.PhotoImage(img_header)

        label_header = tk.Label(
            self.question,
            image=self.img_header,
            background="#000000",
            borderwidth=0,
            highlightthickness=0,
        )
        label_header.place(x=0, y=15)
        
        label_lifes = tk.Label(self.question, text=self.lifes)
        label_lifes.configure(
            background="#000000",
            fg="#ffffff",
            font=("Segoe UI", 35, "bold"),
        )
        label_lifes.place(x=95, y=27)
        
        img_time0 = Image.open(
            resource_path("src", "frontend", "media", "watch.png")
        )
        img_time1 = img_time0.resize((100,100),  Image.Resampling.LANCZOS)
        self.img_time = ImageTk.PhotoImage(img_time1)
        
        label_watch = tk.Label(self.question, image=self.img_time)
        label_watch.place(x=270, y=15)
        label_watch.configure(
            background="#000000"
        )
        
        self.label_seconds = tk.Label(self.question, text=f"{self.time}")
        self.label_seconds.configure(
            background="#000000",
            fg="#ffffff",
            font=("Segoe UI", 35, "bold"),
        )
        self.label_seconds.place(x=370, y=27)
        
        #Frame contenedor
        content_frame = tk.Frame(self.question)
        content_frame.configure(
            background="#000000"
        )
        content_frame.place(
            x=10,
            y=150,
            width=480
        )
        
        #Frame para la pregunta
        frame_question = tk.Frame(content_frame)
        frame_question.configure(
            background="#1B1022",
            highlightbackground="#762A91",
            highlightthickness=2,
            padx=16,
            pady=14,
        )
        frame_question.pack(fill="x", padx=8, pady=(8, 12))
        label_question = tk.Label(
            frame_question,
            text=self.list_questions[0][0],
            background="#1B1022",
            foreground="#FFFFFF",
            font=("Segoe UI", 14, "bold"),
            justify="center",
            wraplength=420,
        )
        label_question.pack(fill="x")
        
        #Frame para la respuesta o las posibles respuestas
        frame_options = tk.Frame(content_frame)
        frame_options.configure(
            background="#140A1A",
            highlightbackground="#4B1768",
            highlightthickness=2,
            padx=8,
            pady=8,
        )
        frame_options.pack(fill="x", padx=8, pady=(0, 8))
        if len(self.list_questions[0])>2:
            btn_option1 = tk.Button(frame_options, text=self.list_questions[0][1][0], command=lambda:self.validate_answer(kind="multiple", button_reference=btn_option1))
            btn_option2 = tk.Button(frame_options, text=self.list_questions[0][2][0], command=lambda:self.validate_answer(kind="multiple", button_reference=btn_option2))
            btn_option3 = tk.Button(frame_options, text=self.list_questions[0][3][0], command=lambda:self.validate_answer(kind="multiple", button_reference=btn_option3))
            btn_option4 = tk.Button(frame_options, text=self.list_questions[0][4][0], command=lambda:self.validate_answer(kind="multiple", button_reference=btn_option4))
            
            for column in range(2):
                frame_options.grid_columnconfigure(column, weight=1, uniform="options")
            for row in range(2):
                frame_options.grid_rowconfigure(row, weight=1, uniform="options")

            for button, row, column, background in (
                (btn_option1, 0, 0, "#4B1768"),
                (btn_option2, 0, 1, "#351044"),
                (btn_option3, 1, 0, "#351044"),
                (btn_option4, 1, 1, "#4B1768"),
            ):
                button.configure(
                    background=background,
                    foreground="#FFFFFF",
                    activebackground="#762A91",
                    activeforeground="#FFFFFF",
                    font=("Segoe UI", 11, "bold"),
                    relief="flat",
                    borderwidth=0,
                    highlightthickness=0,
                    cursor="hand2",
                    padx=10,
                    pady=12,
                    wraplength=185,
                    justify="center",
                )
                button.bind(
                    "<Enter>",
                    lambda _event, current=button: current.configure(
                        background="#762A91"
                    ),
                )
                button.bind(
                    "<Leave>",
                    lambda _event, current=button, color=background: current.configure(
                        background=color
                    ),
                )
                button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
            
            
        elif len(self.list_questions[0])==2:
            input_answer = tk.Entry(
                frame_options,
                background="#24152E",
                foreground="#FFFFFF",
                insertbackground="#FFFFFF",
                font=("Segoe UI", 12),
                relief="flat",
                borderwidth=0,
                highlightthickness=1,
                highlightbackground="#4B1768",
                highlightcolor="#762A91",
            )
            input_answer.pack(fill="x", padx=8, pady=(8, 12), ipady=8)

            button_send = tk.Button(
                frame_options,
                text="Enviar",
                command=lambda: self.validate_answer(
                    kind="simple",
                    value=input_answer,
                    button_reference=button_send,
                ),
                background="#4B1768",
                foreground="#FFFFFF",
                activebackground="#762A91",
                activeforeground="#FFFFFF",
                font=("Segoe UI", 11, "bold"),
                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                cursor="hand2",
                padx=20,
                pady=9,
            )
            button_send.bind(
                "<Enter>",
                lambda _event: button_send.configure(background="#762A91"),
            )
            button_send.bind(
                "<Leave>",
                lambda _event: button_send.configure(background="#4B1768"),
            )
            button_send.pack(pady=(0, 8))
            
    def validate_answer(self, kind:str, button_reference:tk.Button, value:tk.Entry|None = None):
        if kind == "simple":
            
            if self.list_questions[0][1].__eq__(value.get()):
                print("Respuesta correcta")
                self.good_answer()
            else:
                print("Respuesta Incorrecta")
                self.bad_answer()
        else:
            
            for i in range (1,5,1):
                
                if self.list_questions[0][i][0] == button_reference.cget("text"):
                    if self.list_questions[0][i][1]:
                        print("Respuesta Correcta")
                        self.good_answer()
                    else:
                        print("Respuesta Incorrecta")
                        self.bad_answer()
                    return
                        
    def time_out(self):
        self.timer_id = None
        self.time -= 1
        self.label_seconds.configure(text=str(self.time))
        if self.time <= 0:
            self.bad_answer()
            return
        self.timer_id = self.question.after(1000, self.time_out)
    
    def good_answer(self):
        self.list_questions.pop(0)
        self.close_view()
        self.question_view = QuestionView(
            main_view=self.main_view,
            lifes=self.lifes,
            questions=self.questions-1,
            list_questions=self.list_questions
        )
        
    def bad_answer(self):
        try:
            random.choice(JOKES)()
        finally:
            self.list_questions.pop(0)
            self.close_view()
            self.question_view = QuestionView(
                main_view=self.main_view,
                lifes=self.lifes-1,
                questions=self.questions-1,
                list_questions=self.list_questions
            )
    
    def close_view(self):
        if self.timer_id is not None:
            self.question.after_cancel(self.timer_id)
            self.timer_id = None
        self.question.destroy()