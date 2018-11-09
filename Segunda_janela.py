from tkinter import *
from tkinter import messagebox

class Segunda_Janela(Toplevel):
    #Metodo Construtor
    def __init__(self, parent):
        #Chamar o init da classe mae
        super().__init__(parent)
        self.geometry('20x200+200+200')
        self.title('Segunda Janela')
        self.transient(parent)
        self.grab_set()

        #Widgets
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)

        #Possition
        self.btn_close.place(x=10, y=250)

    # Método para fechar a janela
    def destroy(self):
        # Janela de confirmaçao
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()