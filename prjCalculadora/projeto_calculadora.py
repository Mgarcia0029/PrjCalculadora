from tkinter import *

# Definindo configurações da janela
janela = Tk()
janela.title("Calculadora Python")
janela.geometry("400x405")
janela.config(bg="#1f1f1e")

# Criação dos frames do visor
frame_tela = Frame(janela, width=400, height=100, bg="#38576b")
frame_tela.grid(row=0, column=0)

# Criação dos frames do corpo da calculadora
frame_corpo = Frame(janela, width=400, height=305)
frame_corpo.grid(row=1, column=0)

# Criação do visor
valor_texto = StringVar()

app_visor = Label(frame_tela, textvariable=valor_texto, width=20, height=3, padx=7, relief=FLAT, anchor="e",
                  justify=RIGHT, font="Ivy 24", bg="#38576b", fg="#feffff")
app_visor.place(x=0, y=0)


# Coletando dados
valores_calculadora = ''


def entrada_valor(valor):
    global valores_calculadora
    valores_calculadora += str(valor)
    valor_texto.set(valores_calculadora)


# Botão calcular
def calcula_dados():
    global valores_calculadora
    try:
        resultado = eval(valores_calculadora)
        valor_texto.set(resultado)
        valores_calculadora = ''
    except:
        valor_texto.set("Erro")
        valores_calculadora = ''


# Botão limpar
def limpar_tela():
    global valores_calculadora
    valores_calculadora = ''
    valor_texto.set('')


# Criação dos botões
# linha 1
btnC = Button(frame_corpo, text="C", width=15, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=limpar_tela)
btnC.place(x=0, y=0)

btnPorcentagem = Button(frame_corpo, text="%", width=10, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('%'))
btnPorcentagem.place(x=165, y=0)

btnDivisao = Button(frame_corpo, text="/", width=10, height=2, bg="#ffab40", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('/'))
btnDivisao.place(x=280, y=0)

# linha 2
btn7 = Button(frame_corpo, text="7", width=8, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('7'))
btn7.place(x=-2, y=61)

btn8 = Button(frame_corpo, text="8", width=8, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('8'))
btn8.place(x=94, y=61)

btn9 = Button(frame_corpo, text="9", width=8, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('9'))
btn9.place(x=190, y=61)

btnMultiplica = Button(frame_corpo, text="*", width=10, height=2, bg="#FFAB40", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('*'))
btnMultiplica.place(x=280, y=61)

# linha 3
btn4 = Button(frame_corpo, text="4", width=8, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('4'))
btn4.place(x=-2, y=122)

btn5 = Button(frame_corpo, text="5", width=8, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('5'))
btn5.place(x=94, y=122)

btn6 = Button(frame_corpo, text="6", width=8, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('6'))
btn6.place(x=190, y=122)

btnSubtrai = Button(frame_corpo, text="-", width=10, height=2, bg="#FFAB40", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('-'))
btnSubtrai.place(x=280, y=122)

# linha 4
btn1 = Button(frame_corpo, text="1", width=8, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('1'))
btn1.place(x=-2, y=183)

btn2 = Button(frame_corpo, text="2", width=8, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('2'))
btn2.place(x=94, y=183)

btn3 = Button(frame_corpo, text="3", width=8, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('3'))
btn3.place(x=190, y=183)

btnSoma = Button(frame_corpo, text="+", width=10, height=2, bg="#FFAB40", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('+'))
btnSoma.place(x=280, y=183)

# linha 5
btn0 = Button(frame_corpo, text="0", width=18, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('0'))
btn0.place(x=-2, y=244)

btnPonto = Button(frame_corpo, text=".", width=8, height=2, bg="#ECEFF1", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrada_valor('.'))
btnPonto.place(x=190, y=244)

btnIgual = Button(frame_corpo, text="=", width=10, height=2, bg="#FFAB40", font='Consolas 15 bold', relief=RAISED, overrelief=RIDGE, command=calcula_dados)
btnIgual.place(x=280, y=244)

# Execução
janela.mainloop()
