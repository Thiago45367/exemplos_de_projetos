from tkinter import *
menu_inicial = Tk()

def teste():
    print ("Botão Funcionando!")



menu_inicial.title ("Meu primeiro programa")
#menu_inicial.geometry ("500x250")#muda o tamanho da janela
menu_inicial.geometry ("500x250+500+200")#muda o tamanho e posição da janela
menu_inicial.resizable(False, False)
#menu_inicial.minsize (400,200) #menor tamanho permitido da janela
#menu_inicial.maxsize (600,300) #maior tamanho permitido da janela
#menu_inicial.state("iconic") #começa minimizada
#menu_inicial.state ("zoomed")#maximizada

menu_inicial.iconbitmap("icone.ico")
menu_inicial['bg'] = '#32a852'



#botão
botao = Button (menu_inicial, text = "ok", command = teste )
botao.pack()

menu_inicial.mainloop()
