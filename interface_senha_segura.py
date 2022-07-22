#importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
import random
from string import digits
from string import punctuation
from string import ascii_letters
from time import sleep
import pyperclip as pc 


#Criar janela
jan = Tk()
jan.title("Gerador de Senhas")
jan.geometry("1000x500")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

#==========imagem===========
imagem = PhotoImage(file="imagem/imagem.png")

#=========== Widgets =============
LeftFrame = Frame(jan, width=300, height=500, bg="BLACK", relief="raise")
LeftFrame.pack(side=LEFT)

imagemLabel = Label(LeftFrame, image=imagem, bg="BLACK")
imagemLabel.place(x=20, y=130)

RightFrame = Frame(jan, width=680, height=600, bg="BLACK", relief="raise")
RightFrame.pack(side=RIGHT)

TituloLabel = Label(LeftFrame, text="Senha.Segura", bg="BLACK", fg="White", font="Arial 20")
TituloLabel.place(x=60, y=10)
TituloLabel = Font(family="Lucida Grande", size=70, font="arial")

pa1Label = Label(RightFrame, text="Palavra chave 1:", bg="BLACK", fg="White", font="Arial 20")
pa1Label.place(x=5, y=100)

pa1Entry = ttk.Entry(RightFrame, width=50)
pa1Entry.place(x=220, y=110)  
pa2Label = Label(RightFrame, text="Palavra chave 2:", bg="BLACK", fg="White", font="Arial 20")
pa2Label.place(x=5, y=150)

pa2Entry = ttk.Entry(RightFrame, width=50)
pa2Entry.place(x=220, y=160)

senhaLabel = Label(RightFrame, text="Senha Gerarada:", bg="BLACK", fg="White", font="Arial 20")
senhaLabel.place(x=210, y=256)

#senhaEntry = ttk.Entry(RightFrame, width=50)
#senhaEntry.place(x=180, y=350)
senha_final = 0  

def Gerar():  #executa funçao do botao GERAR SENHA
    senha_gerLabel = Label(RightFrame, text= '', bg="BLACK", fg="White", font="Arial 15", width=200)
    senha_gerLabel.place(x=210, y=320) #para "limpar" senha anterior
    global senha_final  #permite usar variaveis globais dentro de uma função
    pa1 = pa1Entry.get()
    pa2 = pa2Entry.get()
    
    #GERANDO SENHA
    symbols = ascii_letters + digits + punctuation
    secure_random = random.SystemRandom()
    password = "".join(secure_random.choice(symbols)
                       for i in range(5))
    symbols = ascii_letters + digits + punctuation
    secure_random = random.SystemRandom()
    password1 = "".join(secure_random.choice(symbols)
                       for i in range(5))
    senha_gerada = password + pa1 + pa2 + password1
    print(senha_gerada)
    senha_final = senha_gerada
    senha_gerLabel = Label(RightFrame, text=senha_gerada, bg="BLACK", fg="White", font="Arial 15")
    senha_gerLabel.place(x=210, y=320)


def Copiar():
    pc.copy(senha_final) 
    copy = pc.paste() 

   
#===Botoes====
GerarButton = ttk.Button(RightFrame, text="GERAR SENHA", width=30, command=Gerar)
GerarButton.place(x=130, y=400)

CopyButton = ttk.Button(RightFrame, text="COPIAR SENHA", width=30, command=Copiar)
CopyButton.place(x=330, y=400)



#----------------------------------WWW--------------


jan.mainloop()
