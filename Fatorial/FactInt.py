import tkinter as tk

window = tk.Tk()
window.geometry('390x200')

lblNum = tk.Label(window, text = 'Qual número?', 
                 font = ('Castellar', 14))
lblNum.place(x = 20, y = 20)
campoNumero = tk.Entry(window, font = ('Castellar', 14))
campoNumero.place(x = 20, y = 60)
lblRes = tk.Label(window, text = 'Resultado...', 
                 font = ('Castellar', 11))
lblRes.place(x = 20, y = 100)

def getFactorial() -> None:
    fact = int(campoNumero.get())
    result = 1

    for n in range(fact, 0, -1):
        result *= n

    lblRes['text'] = result
    
btnFatorial = tk.Button(window, command = getFactorial,text = 'Calcular', 
                 font = ('Castellar', 14))
btnFatorial.place(x = 20, y = 140)

window.mainloop()