import os
import tkinter as tk
from tkinter import messagebox


def calcular():
    opcao = opcao_var.get()

    if opcao == 1:  # 5% porcento selecionado
        take_rate = 5
        messagebox.showinfo('Opção selecionada',
                            'VOCÊ ESTÁ USANDO 5% DE TAKE RATE')
    elif opcao == 2:
        take_rate = 7
        messagebox.showinfo('Opção selecionada',
                            'VOCÊ ESTÁ USANDO 7% DE TAKE RATE')
    elif opcao == 3:
        take_rate = 10
        messagebox.showinfo('Opção selecionada',
                            'VOCÊ ESTÁ USANDO 10% DE TAKE RATE')
    elif opcao == 4:
        take_rate = 15
        messagebox.showinfo('Opção selecionada',
                            'VOCÊ ESTÁ USANDO 15% DE TAKE RATE')
    else:
        messagebox.showerror('Opção Inválida', 'Selecione uma opção válida.')
        return

    Take_Rate_refera = float(Take_Rate_refera_entry.get())
    Valor_prestador = float(Valor_prestador_entry.get())
    Take_Rate_imobiliaria = float(Take_Rate_imobiliaria_entry.get())

    valor_refera = Valor_prestador * (Take_Rate_refera / 100)
    valor_imobiliaria = Valor_prestador * (Take_Rate_imobiliaria / 100)
    valor_total = valor_refera + valor_imobiliaria + Valor_prestador
    valor_pricing = Valor_prestador * (take_rate / 100)
    novo_valor_refera = valor_pricing + valor_refera
    novo_valor_prestador = Valor_prestador - valor_pricing
    novo_take_rate_refera = (novo_valor_refera / novo_valor_prestador) * 100
    novo_take_rate_refera_porcentagem = "{:.2f}%".format(novo_take_rate_refera)
    novo_take_rate_imobiliaria = (
        valor_imobiliaria / novo_valor_prestador) * 100
    novo_take_rate_imobiliaria_porcentagem = "{:.2f}%".format(
        novo_take_rate_imobiliaria)
    desconto_pricing = Valor_prestador - novo_valor_prestador

    resultado = f'''
VALOR PRESTADOR: R$ {novo_valor_prestador:.2f}
TARIFA DA INTERMEDIÁRIA: {novo_take_rate_imobiliaria_porcentagem}
TARIFA DA REFERA: {novo_take_rate_refera_porcentagem}
Desconto Pricing: RS {desconto_pricing:.2f}'''

    messagebox.showinfo('Resultado', resultado)


window = tk.Tk()
window.title('Calculadora TAKE RATE PRICING')
window.geometry('300x300')


opcao_var = tk.IntVar()
opcao_var.set(0)

titulo_label = tk.Label(window, text='Selecione a porcentagem desejada:')
titulo_label.pack()

porcentagens = [('5%', 1), ('7%', 2), ('10%', 3), ('15%', 4)]

for valor, opcao in porcentagens:
    radio_button = tk.Radiobutton(
        window, text=valor, variable=opcao_var, value=opcao)
    radio_button.pack()

Valor_prestador_label = tk.Label(window, text='TOTAL PRESTADOR')
Valor_prestador_label.pack()
Valor_prestador_entry = tk.Entry(window, justify='center')
Valor_prestador_entry.pack()

Take_Rate_imobiliaria_label = tk.Label(
    window, text='TARIFA DA INTERMEDIÁRIA')
Take_Rate_imobiliaria_label.pack()
Take_Rate_imobiliaria_entry = tk.Entry(window, justify='center')
Take_Rate_imobiliaria_entry.pack()

Take_Rate_refera_label = tk.Label(
    window, text='TARIFA DA REFERA')
Take_Rate_refera_label.pack()
Take_Rate_refera_entry = tk.Entry(window, justify='center')
Take_Rate_refera_entry.pack()


calcular_button = tk.Button(window, text='Executar', command=calcular)
calcular_button.pack()

window.mainloop()
