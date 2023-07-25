import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import datetime


class Transacao:
    def __init__(self, descricao, valor, tipo, data, data_vencimento=None):
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo  # 'receita' ou 'despesa'
        self.data = data
        self.data_vencimento = data_vencimento


class ControleFinanceiro:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def calcular_saldo(self):
        saldo = 0
        for transacao in self.transacoes:
            if transacao.tipo == 'receita':
                saldo += transacao.valor
            else:
                saldo -= transacao.valor
        return saldo

    def consultar_contas_pagar(self):
        contas_pagar = []
        for transacao in self.transacoes:
            if transacao.tipo == 'despesa':
                contas_pagar.append(transacao)
        return contas_pagar

    def consultar_contas_receber(self):
        contas_receber = []
        for transacao in self.transacoes:
            if transacao.tipo == 'receita':
                contas_receber.append(transacao)
        return contas_receber

    def consultar_por_data(self, data):
        transacoes_data = []
        for transacao in self.transacoes:
            if transacao.data.date() == data.date():
                transacoes_data.append(transacao)
        return transacoes_data

    def gerar_grafico_mensal(self):
        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        receitas_mensais = [0] * 12
        despesas_mensais = [0] * 12

        for transacao in self.transacoes:
            mes = transacao.data.month - 1
            if transacao.tipo == 'receita':
                receitas_mensais[mes] += transacao.valor
            else:
                despesas_mensais[mes] += transacao.valor

        plt.bar(meses, receitas_mensais, label='Receitas')
        plt.bar(meses, despesas_mensais, label='Despesas')
        plt.xlabel("Meses")
        plt.ylabel("Valor (R$)")
        plt.title("Gráfico de Receitas e Despesas Mensais")
        plt.legend()
        plt.show()


def adicionar_transacao():
    descricao = descricao_entry.get()
    valor = float(valor_entry.get())
    tipo = tipo_var.get()
    data = datetime.datetime.now()

    if tipo == 'receita':
        data_vencimento = datetime.datetime.strptime(
            data_vencimento_entry.get(), "%d/%m/%Y")
    else:
        data_vencimento = None

    transacao = Transacao(descricao, valor, tipo, data, data_vencimento)
    controle.adicionar_transacao(transacao)
    messagebox.showinfo("Sucesso", "Transação adicionada com sucesso!")


def calcular_saldo():
    saldo = controle.calcular_saldo()
    messagebox.showinfo("Saldo", f"Saldo atual: R$ {saldo}")


def consultar_contas_pagar():
    contas_pagar = controle.consultar_contas_pagar()
    messagebox.showinfo("Contas a Pagar", formatar_transacoes(contas_pagar))


def consultar_contas_receber():
    contas_receber = controle.consultar_contas_receber()
    messagebox.showinfo("Contas a Receber",
                        formatar_transacoes(contas_receber))


def formatar_transacoes(transacoes):
    texto = ""
    for transacao in transacoes:
        texto += f"{transacao.descricao}: R$ {transacao.valor} ({transacao.data})\n"
    return texto


def formatar_transacoes_por_data(transacoes):
    texto = ""
    for transacao in transacoes:
        texto += f"{transacao.descricao}: R$ {transacao.valor} ({transacao.data})\n"
        if transacao.data_vencimento:
            texto += f"  Vencimento: {transacao.data_vencimento.strftime('%d/%m/%Y')}\n"
    return texto


def consultar_por_data():
    data = datetime.datetime.strptime(data_consulta_entry.get(), "%d/%m/%Y")
    transacoes_data = controle.consultar_por_data(data)
    messagebox.showinfo("Transações na Data",
                        formatar_transacoes_por_data(transacoes_data))


def gerar_grafico():
    controle.gerar_grafico_mensal()


controle = ControleFinanceiro()

window = tk.Tk()
window.title("Controle Financeiro")

descricao_label = tk.Label(window, text="Descrição:")
descricao_label.pack()
descricao_entry = tk.Entry(window)
descricao_entry.pack()

valor_label = tk.Label(window, text="Valor:")
valor_label.pack()
valor_entry = tk.Entry(window)
valor_entry.pack()

tipo_label = tk.Label(window, text="Tipo:")
tipo_label.pack()
tipo_var = tk.StringVar(window)
tipo_var.set('receita')
tipo_optionmenu = tk.OptionMenu(window, tipo_var, 'receita', 'despesa')
tipo_optionmenu.pack()

data_vencimento_label = tk.Label(
    window, text="Data de Vencimento (DD/MM/AAAA):")
data_vencimento_label.pack()
data_vencimento_entry = tk.Entry(window)
data_vencimento_entry.pack()

adicionar_button = tk.Button(
    window, text="Adicionar Transação", command=adicionar_transacao)
adicionar_button.pack()

calcular_saldo_button = tk.Button(
    window, text="Calcular Saldo", command=calcular_saldo)
calcular_saldo_button.pack()

contas_pagar_button = tk.Button(
    window, text="Consultar Contas a Pagar", command=consultar_contas_pagar)
contas_pagar_button.pack()

contas_receber_button = tk.Button(
    window, text="Consultar Contas a Receber", command=consultar_contas_receber)
contas_receber_button.pack()

data_consulta_label = tk.Label(window, text="Data de Consulta (DD/MM/AAAA):")
data_consulta_label.pack()
data_consulta_entry = tk.Entry(window)
data_consulta_entry.pack()

consultar_por_data_button = tk.Button(
    window, text="Consultar por Data", command=consultar_por_data)
consultar_por_data_button.pack()

gerar_grafico_button = tk.Button(
    window, text="Gerar Gráfico Mensal", command=gerar_grafico)
gerar_grafico_button.pack()

window.mainloop()
