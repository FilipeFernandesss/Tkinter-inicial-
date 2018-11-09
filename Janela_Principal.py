#importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from Segunda_janela import Segunda_Janela

#Classe Janela_Principal
class Janela_principal(Tk):
    #Método construtor
    def __init__(self):
        #Executar o metodo da classe mae
        super().__init__()
        #Ajustar tamanho
        self.geometry('300x300+200+200')
        #Colocar um titulo
        self.title('Janela Principal')


        #Widgets da tela
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_ok = Button(self, width=10, text='OK', command=self.btn_ok_click)
        self.lbl_ok = Label(self, text='Teste')
        self.txt_ok = Entry(self)


        ##Posicionando os widgets
        self.btn_close.place(x=10, y=250)
        self.btn_ok.place(x=140, y=250)
        self.lbl_ok.place(x=140, y=200)
        self.txt_ok.place(x=140, y=150)

        # == Menu ==
        #Criando um menu
        self.menu = Menu(self)
        #Criando um item de menu e subitens
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label='Segunda Janela', command=self.criar_segunda_janela)
        self.menu_principal.add_command(label='comando 2', command=self.menu_click)
        self.menu_principal.add_command(label='comando 3', command=self.menu_click)
        self.menu_principal.add_separator()
        self.menu_principal.add_command(label='sair', command=self.destroy)

        self.menu.add_cascade(label='Principal', menu=self.menu_principal)

        #Mostrando o menu
        self.config(menu=self.menu)

    #Método para fechar a janela
    def destroy(self):
        #Janela de confirmaçao
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()

    #Método para o btn_ok
    def btn_ok_click(self):
        #Mudar o texto do lbl_ok
        self.lbl_ok['text'] = self.txt_ok.get()

    #Método para o click no item de menu
    def menu_click(self):
        messagebox.showinfo('Menu', 'Clicou no item de menu')

    #Método para criar a segunda janela
    def criar_segunda_janela(self):
        Segunda_Janela(self)