from tkinter import *
import tkinter as tk
from Patterns import Pattern
from Bank import BankSystem as bs

class Windows():
        def __init__(self):
                self.MainWindow= Pattern()
                self.Second = Pattern()
                self.MainSecond= Pattern()
                self.OplataTVWindow= Pattern()
                self.OstatokCheckWindow= Pattern()
                self.NalWindow= Pattern()
                self.OplataTelefonWindow= Pattern()

                Pattern.btn_back_text = 'Назад'
                self.back = Pattern().UpperButtton
                
                Pattern.BackCommad = self.BackButtons
                Pattern.SecondMain2 = self.SecondMain

        def WindowMain(self):
                self.MainWindow.WindowName = tk.Tk()
                self.MainWindow.title = 'Главное_Меню'
                self.MainWindow.buttons = ['Ввести карту']
                self.MainWindow.commands = [self.SecondWindow]
                self.MainWindow.labels = ['Беларусьбанк','Пожалуйста, вставьте вашу карту']
                Pattern.UpperButtton = 'MainWindow'
                self.MainWindow.btn_back_text = 'Выход'
                self.MainWindow.WindowsPattern()
                self.MainWindow.First_Window()
        def SecondWindow(self):
                if Pattern.UpperButtton == 'MainWindow':
                        self.MainWindow.WindowName.destroy()
                self.Second.WindowName = tk.Tk()
                self.Second.text = StringVar()
                self.Second.title = 'Проверка карточки'
                self.Second.buttons = ['Подтвердить']
                self.Second.commands = [self.check_password]
                self.Second.labels = ['Введите свой четырёхзначный код']
                Pattern.UpperButtton = 'Second'
                self.Second.WindowsPattern()
                self.Second.Second_Window()

        def SecondMain(self):
                if Pattern.UpperButtton == 'Second':
                        self.Second.WindowName.destroy()
                self.MainSecond.WindowName = tk.Tk()
                self.MainSecond.title = 'Добро пожаловать'
                self.MainSecond.labels = ['Операции по карточке']
                self.MainSecond.buttons = ["Оплата за ТВ", "Остаток на карте", "Снятие наличный", "Оплата телефона"]
                self.MainSecond.commands = [self.TVOplataWindow, self.CheckOstatokWindow, self.Nalichnie, self.TelefonOplataWindowlefon]
                Pattern.UpperButtton = 'MainSecond'
                self.MainSecond.WindowsPattern()
                self.MainSecond.First_Window()

        def TVOplataWindow(self):
                if Pattern.UpperButtton == 'MainSecond':
                        self.MainSecond.WindowName.destroy()
                self.OplataTVWindow.WindowName = tk.Tk()
                self.OplataTVWindow.title = 'Оплата ТВ'
                self.OplataTVWindow.buttons = ['Оплатить']
                self.OplataTVWindow.commands = [self.oplata_tv]
                self.OplataTVWindow.labels = ['Оплата за ТВ']
                Pattern.UpperButtton = 'OplataTVWindow'

                self.OplataTVWindow.WindowsPattern()
                self.OplataTVWindow.LabelsPattern()
                self.OplataTVWindow.lbl1 = tk.Label(text= "Введите ID пользователя", font= 25).grid(padx= 300, pady= 15)
                self.OplataTVWindow.ent1 = tk.Entry()
                self.OplataTVWindow.ent1.grid()
                self.OplataTVWindow.lbl2 = tk.Label(text= "Введите сумму для пополнения", font= 25).grid(padx= 300, pady= 15)
                self.OplataTVWindow.ent2 = tk.Entry()
                self.OplataTVWindow.ent2.grid()
                self.OplataTVWindow.ButtonsPattern()
        def oplata_tv(self):
                with open('transactions.txt', 'w', encoding="UTF8") as writer:
                        writer.write(str(f'popolnenie: {self.OplataTVWindow.ent2.get()}\n'))
                        writer.write(str(f'User ID: {self.OplataTVWindow.ent1.get()}\n'))
                self.BackButtons()
                return bs().oplata_TV()

        def CheckOstatokWindow(self):
                if Pattern.UpperButtton == 'MainSecond':
                        self.MainSecond.WindowName.destroy()
                self.OstatokCheckWindow.WindowName = tk.Tk()
                self.OstatokCheckWindow.title = 'Оплата ТВ'  #Нужно получить из банка 
                self.OstatokCheckWindow.buttons = []
                self.OstatokCheckWindow.commands = []
                self.OstatokCheckWindow.labels = ['Остаток на карте', f'{bs().balance}']
                Pattern.UpperButtton = 'OstatokCheckWindow'

                self.OstatokCheckWindow.WindowsPattern()
                self.OstatokCheckWindow.First_Window()

        def Nalichnie(self):
                if Pattern.UpperButtton == 'MainSecond':
                        self.MainSecond.WindowName.destroy()
                self.NalWindow.WindowName = tk.Tk()
                self.NalWindow.title = 'Снятие наличных'
                self.NalWindow.buttons = ['Выдать']
                self.NalWindow.commands = [self.Nalik]
                self.NalWindow.labels = ['Выдача наличных']
                Pattern.UpperButtton = 'NalWindow'

                self.NalWindow.WindowsPattern()
                self.NalWindow.LabelsPattern()
                self.NalWindow.ent1 = tk.Entry()
                self.NalWindow.ent1.grid()
                self.NalWindow.ButtonsPattern()
        
        def Nalik(self):
                with open('transactions.txt', 'w', encoding="UTF8") as writer:
                        writer.write(str(f'Количество снятых наличных: {self.NalWindow.ent1.get()}\n'))
                self.BackButtons()
                return bs().Nalik()

        def TelefonOplataWindowlefon(self):
                if Pattern.UpperButtton == 'MainSecond':
                        self.MainSecond.WindowName.destroy()
                self.OplataTelefonWindow.WindowName = tk.Tk()
                self.OplataTelefonWindow.title = 'Оплата телефона'
                self.OplataTelefonWindow.buttons = ['Оплатить']
                self.OplataTelefonWindow.commands = [self.oplata_telefon]
                self.OplataTelefonWindow.labels = ['Оплата телефона']
                Pattern.UpperButtton = 'OplataTelefonWindow'

                self.OplataTelefonWindow.WindowsPattern()
                self.OplataTelefonWindow.LabelsPattern()
                self.OplataTelefonWindow.lbl1 = tk.Label(text= "Введите номер телефона", font= 25).grid(padx= 300, pady= 15)
                self.OplataTelefonWindow.ent1 = tk.Entry()
                self.OplataTelefonWindow.ent1.grid()
                self.OplataTelefonWindow.lbl2 = tk.Label(text= "Введите сумму для заполнения", font= 25).grid(padx= 300, pady= 15)
                self.OplataTelefonWindow.ent2 = tk.Entry()
                self.OplataTelefonWindow.ent2.grid()
                self.OplataTelefonWindow.ButtonsPattern()
                
        def oplata_telefon(self):
                with open('transactions.txt', 'w', encoding="UTF8") as writer:
                        writer.write(str(f'popolnenie: {self.OplataTelefonWindow.ent2.get()}\n'))
                        writer.write(str(f'phone number: {self.OplataTelefonWindow.ent1.get()}\n'))
                self.BackButtons()
                return bs().oplata_telefon()


        def check_password(self):
                if self.Second.text.get()  == bs().pin_code:
                        self.SecondMain()
                else:
                        self.Second.text.set("")
                        
        def BackButtons(self):
                if Pattern.UpperButtton == 'MainWindow':
                        self.MainWindow.WindowName.destroy()

                elif Pattern.UpperButtton == 'Second':
                        self.Second.WindowName.destroy()
                        return self.WindowMain()

                elif Pattern.UpperButtton == 'MainSecond':
                        self.MainSecond.WindowName.destroy()
                        return self.SecondWindow()

                elif Pattern.UpperButtton == 'OplataTelefonWindow':
                        self.OplataTelefonWindow.WindowName.destroy()
                        return self.SecondMain()

                elif Pattern.UpperButtton == 'OplataTVWindow':
                        self.OplataTVWindow.WindowName.destroy()
                        return self.SecondMain()

                elif Pattern.UpperButtton == 'OstatokCheckWindow':
                        self.OstatokCheckWindow.WindowName.destroy()
                        return self.SecondMain()

                elif Pattern.UpperButtton == 'NalWindow':
                        self.NalWindow.WindowName.destroy()
                        return self.SecondMain()



if __name__ == "__main__":
        start = Windows()
        start.WindowMain()
        tk.mainloop()
        
        