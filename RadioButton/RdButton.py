import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

frame = tk.Tk()
frame.geometry('400x320')
frame.resizable(False, False)
frame.title('Exemplo Radio Button')
frame.tk.call('wm', 'iconphoto', frame._w, tk.PhotoImage(file = '..\Images\python-logo-only.png'))


def mostrarEscolha():
    showinfo(title = 'Resultado', message = f'Voce escolheu {tam_selecionado.get()}')

lblPergunta = ttk.Label(text = 'Escolha o tamanho: ')
lblPergunta.pack(fill = 'x', padx = 15,  pady = 5)

tam_selecionado = tk.StringVar(frame, value = 'M')

tamanhos = (('Pequeno', 'P'), 
            ('Médio', 'M'),
            ('Grande', 'G'),
            ('Extra Grande', 'XG'),
            ('Extra Extra Grande', 'XXG'))

for tamanho in tamanhos:
    rd = ttk.Radiobutton(frame, 
                        text = tamanho[0],
                        value = tamanho[1],
                        variable = tam_selecionado)
    rd.pack(fill = 'x', padx = 15,  pady = 5) #Padding

btnEscolha = ttk.Button(frame, 
                        text = 'Ler tamanho', 
                        command = mostrarEscolha)
btnEscolha.pack(fill = 'x', padx = 15, pady = 15)

frame.mainloop()