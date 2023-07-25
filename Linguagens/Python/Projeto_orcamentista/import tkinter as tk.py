import tkinter as tk
from tkinter import messagebox


def exibir_campos_servicos():
    if multiple_services_var.get() == 1:
        for label, entry in zip(servico_labels, servico_entries):
            label.grid()
            entry.grid()
    else:
        for label, entry in zip(servico_labels, servico_entries):
            label.grid_remove()
            entry.grid_remove()


def calcular(event=None):
    opcao = opcao_var.get()

    if opcao == 1:  # 5% porcento selecionado
        take_rate = 5
        messagebox.showinfo('Opção selecionada',
                            'VOCÊ ESTÁ USANDO 5% DE TAKE RATE')
    elif opcao == 2:
        take_rate = 7
        # messagebox.showinfo('Opção selecionada',
        #                     'VOCÊ ESTÁ USANDO 7% DE TAKE RATE')
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

    if multiple_services_var.get() == 1:
        num_servicos = int(num_servicos_entry.get())
        campos_servicos = len(servico_entries)

        if num_servicos > 0 and campos_servicos >= num_servicos:
            valor_servicos = []
            for i in range(num_servicos):
                valor_servico = float(servico_entries[i].get())
                valor_servicos.append(valor_servico)

            total_valor_servicos = sum(valor_servicos)

            if total_valor_servicos != Valor_prestador:
                messagebox.showerror(
                    'Erro', 'A soma dos valores dos serviços não é igual ao valor informado no campo "TOTAL PRESTADOR".')
                return

            desconto_por_servico = desconto_pricing / total_valor_servicos

            resultado += f'\n\n--- Desconto Dividido por Serviço ---\n'
            for i in range(num_servicos):
                desconto_servico = desconto_por_servico * valor_servicos[i]
                novo_valor_servico = valor_servicos[i] - desconto_servico
                resultado += f'Serviço {i+1}: R$ {novo_valor_servico:.2f} (Desconto: R$ {desconto_servico:.2f})\n'
        else:
            messagebox.showerror(
                'Erro', 'A quantidade de serviços informada não corresponde aos campos preenchidos.')
            return

    messagebox.showinfo('Resultado', resultado)
    limpar_campos()


def limpar_campos():
    Valor_prestador_entry.delete(0, tk.END)
    Take_Rate_imobiliaria_entry.delete(0, tk.END)
    Take_Rate_refera_entry.delete(0, tk.END)
    num_servicos_entry.delete(0, tk.END)
    for entry in servico_entries:
        entry.delete(0, tk.END)


window = tk.Tk()
window.title('Calculadora TAKE RATE PRICING')

# Definir cores
cor_fundo = '#FFFFFF'  # Cor de fundo
cor_texto = '#333333'  # Cor do texto
cor_botao = '#CCCCCC'  # Cor do botão
cor_borda = '#DDDDDD'  # Cor da borda

window.configure(bg=cor_fundo)

# Configurar o layout em grade
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

opcao_var = tk.IntVar()
opcao_var.set(2)  # Definindo a opção padrão como 2 (7%)

titulo_label = tk.Label(
    window, text='Selecione a porcentagem desejada:', bg=cor_fundo, fg=cor_texto)
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

porcentagens = [('5%', 1), ('7%', 2), ('10%', 3), ('15%', 4)]

row = 1
col = 0
for valor, opcao in porcentagens:
    radio_button = tk.Radiobutton(
        window, text=valor, variable=opcao_var, value=opcao, bg=cor_fundo, fg=cor_texto, selectcolor=cor_fundo)
    radio_button.grid(row=row, column=col, sticky='w', padx=10, pady=5)
    col += 1
    if col > 1:
        col = 0
        row += 1

Valor_prestador_label = tk.Label(
    window, text='TOTAL PRESTADOR', bg=cor_fundo, fg=cor_texto)
Valor_prestador_label.grid(row=row, column=0, sticky='e', padx=10, pady=5)
Valor_prestador_entry = tk.Entry(
    window, justify='center', bd=1, relief='solid')
Valor_prestador_entry.grid(row=row, column=1, sticky='w', padx=10, pady=5)
row += 1

Take_Rate_imobiliaria_label = tk.Label(
    window, text='TARIFA DA INTERMEDIÁRIA', bg=cor_fundo, fg=cor_texto)
Take_Rate_imobiliaria_label.grid(
    row=row, column=0, sticky='e', padx=10, pady=5)
Take_Rate_imobiliaria_entry = tk.Entry(
    window, justify='center', bd=1, relief='solid')
Take_Rate_imobiliaria_entry.grid(
    row=row, column=1, sticky='w', padx=10, pady=5)
row += 1

Take_Rate_refera_label = tk.Label(
    window, text='TARIFA DA REFERA', bg=cor_fundo, fg=cor_texto)
Take_Rate_refera_label.grid(row=row, column=0, sticky='e', padx=10, pady=5)
Take_Rate_refera_entry = tk.Entry(
    window, justify='center', bd=1, relief='solid')
Take_Rate_refera_entry.grid(row=row, column=1, sticky='w', padx=10, pady=5)
row += 1

multiple_services_var = tk.IntVar()
# Definindo a opção padrão como 0 (não selecionado)
multiple_services_var.set(0)
multiple_services_checkbox = tk.Checkbutton(
    window, text='Você possui múltiplos serviços?', variable=multiple_services_var, bg=cor_fundo, fg=cor_texto, command=exibir_campos_servicos)
multiple_services_checkbox.grid(
    row=row, column=0, columnspan=2, padx=10, pady=5)
row += 1

num_servicos_label = tk.Label(
    window, text='Quantos serviços?', bg=cor_fundo, fg=cor_texto)
num_servicos_label.grid(row=row, column=0, sticky='e', padx=10, pady=5)
num_servicos_entry = tk.Entry(window, justify='center', bd=1, relief='solid')
num_servicos_entry.grid(row=row, column=1, sticky='w', padx=10, pady=5)
row += 1

servico_labels = []
servico_entries = []
for i in range(10):  # Número máximo de campos para os valores dos serviços (pode ser ajustado conforme necessário)
    servico_label = tk.Label(
        window, text=f'Valor do Serviço {i+1}', bg=cor_fundo, fg=cor_texto)
    servico_label.grid(row=row, column=0, sticky='e', padx=10, pady=5)
    servico_entry = tk.Entry(window, justify='center', bd=1, relief='solid')
    servico_entry.grid(row=row, column=1, sticky='w', padx=10, pady=5)
    servico_labels.append(servico_label)
    servico_entries.append(servico_entry)
    row += 1

calcular_button = tk.Button(
    window, text='Executar', command=calcular, bd=1, relief='solid', bg=cor_botao, fg=cor_texto)
calcular_button.grid(row=row, column=0, columnspan=2, padx=10, pady=10)

# Bind para o evento <Return> (Enter) na janela principal
window.bind('<Return>', calcular)

window.mainloop()
