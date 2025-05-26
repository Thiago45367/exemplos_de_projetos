from tkinter import *
from tkinter import messagebox
menu_inicial = Tk()

def executar():
    messagebox.showinfo("Informação!", "Função executar chamada")

def cancelar():
    messagebox.askokcancel("Pergunta", "Tem Certeza?")    


menu_inicial.title("Exemplo de interface")
menu_inicial.resizable(False, False)
menu_inicial.geometry("300x250+500+100")
menu_inicial.iconbitmap("icone.ico")

#colocar rótulos(label)
label1 = Label (menu_inicial, text = "Primeiro Rótulo", bg = "yellow", fg = "blue", font = "Times 20 bold")
label1.pack()

#botão
botao = Button (menu_inicial, text = "Executar", bg = "green", fg = "red", font = "Times 20 bold", command = executar)
botao.pack()

label1 = Label (menu_inicial, text = "Segundo Rótulo", bg = "black", fg = "yellow", font = "Times 18 bold")
label1.pack()

botao = Button (menu_inicial, text = "Cancelar", bg = "blue", fg = "green", font = "Times 20 bold", command = cancelar)
botao.pack()



menu_inicial.mainloop()
