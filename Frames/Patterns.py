from tkinter import *
import tkinter as tk
from Bank import BankSystem as bs


class Pattern():
    def __init__(self):
        # self.text = self.text
        
        self.UpperButtton = ''
    def WindowsPattern(self):
        
        # x, y = self.WindowName.winfo_screenwidth(), self.WindowName.winfo_screenheight()
        self.x, self.y = 900, 450
        self.lpad =self.x / 3
        self.mpad =self.y / 30
        self.xpad =self.x / 35
        self.ypad =self.y / 30
        self.WindowName.title(self.title)
        self.WindowName.geometry = f"900x450"
    
    def First_Window(self):
        self.LabelsPattern() 
        self.ButtonsPattern()

    def Second_Window(self):
        self.LabelsPattern()
        self.Input_Card_Password(4)
        self.ButtonsPattern()
    
    # def Telefon_Window(self):
    #     self.LabelsPattern()
       
    #     self.ButtonsPattern()

    def ButtonsPattern(self):
        btnname = []
        for i in range(len(self.buttons)):
            count = 1
            btnname.append(f'btn{count + 1}')
            btnname[i] = tk.Button(text=self.buttons[i], width=50, height=2, command=self.commands[i]).grid(padx=self.xpad, pady=self.ypad)
        btn_back = tk.Button(text=self.btn_back_text, width=50, height=2, command=self.BackCommad).grid(padx=self.xpad, pady=self.ypad)

    def LabelsPattern(self):
        lblname = []
        for j in range(len(self.labels)):
            count = 1
            lblname.append(f'lbl{count + 1}')
            lblname[j] = tk.Label(text= self.labels[j], font= 25).grid(padx= self.lpad, pady= self.mpad)

    def Input_Card_Password(self,l=4):
        def limit(text,l):
            if len(text.get()) >= l:
                text.set(text.get()[:l])
        Entry(self.WindowName, show="*", width = l+3, textvariable = self.text).grid(padx=self.x / 4, pady=self.y / 15)
        self.text.trace("w", lambda*x: limit(self.text,l))
        self.WindowName.bind('<Return>', lambda x:self.WindowName.destroy())  
        return self.text.get()

    
    def passs(self):
        pass

