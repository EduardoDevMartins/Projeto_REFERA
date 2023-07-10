import tkinter as tk
from tkinter import Menu

import pyperclip


def copiar_texto(event):
    widget_selecionado = event.widget
    indice_selecionado = widget_selecionado.curselection()
    if indice_selecionado:
        texto_selecionado = widget_selecionado.get(indice_selecionado)
        pyperclip.copy(texto_selecionado)


def alternar_categoria(event):
    widget_selecionado = event.widget
    indice_selecionado = widget_selecionado.curselection()
    if indice_selecionado:
        categoria_selecionada = widget_selecionado.get(indice_selecionado)
        if categoria_selecionada == categoria_expandida.get():
            # Categoria selecionada está expandida, recolher
            categoria_expandida.set("")
            lista_frases.pack_forget()
        else:
            # Categoria selecionada está recolhida, expandir
            categoria_expandida.set(categoria_selecionada)
            mostrar_frases(categoria_selecionada)


def alternar_subcategoria(event):
    widget_selecionado = event.widget
    indice_selecionado = widget_selecionado.curselection()
    if indice_selecionado:
        subcategoria_selecionada = widget_selecionado.get(indice_selecionado)
        if subcategoria_selecionada == subcategoria_expandida.get():
            # Subcategoria selecionada está expandida, recolher
            subcategoria_expandida.set("")
            lista_frases.pack_forget()
        else:
            # Subcategoria selecionada está recolhida, expandir
            subcategoria_expandida.set(subcategoria_selecionada)
            mostrar_frases(subcategoria_selecionada)


def mostrar_frases(categoria):
    frases = category_phrases.get(categoria, {})
    lista_frases.delete(0, tk.END)
    for subcategoria, lista in frases.items():
        lista_frases.insert(tk.END, f"{subcategoria}:")
        for frase in lista:
            lista_frases.insert(tk.END, f"  {frase}")
    lista_frases.pack()


def ao_clicar(event):
    if event.widget == lista_categorias:
        alternar_categoria(event)
    elif event.widget == lista_subcategorias:
        alternar_subcategoria(event)


def ao_selecionar(event):
    widget_selecionado = event.widget
    indice_selecionado = widget_selecionado.curselection()
    if indice_selecionado:
        texto_selecionado = widget_selecionado.get(indice_selecionado)
        pyperclip.copy(texto_selecionado)
        widget_selecionado.selection_clear(0, tk.END)
        widget_selecionado.selection_set(indice_selecionado)


def adicionar_dialogo_categoria():
    def adicionar_categoria():
        nova_categoria = entrada_nova_categoria.get().strip()
        if nova_categoria:
            lista_categorias.insert(tk.END, nova_categoria)
            category_phrases[nova_categoria] = {}
            entrada_nova_categoria.delete(0, tk.END)
            dialogo_categoria.destroy()

    dialogo_categoria = tk.Toplevel(janela)
    dialogo_categoria.title("Adicionar Categoria")
    dialogo_categoria.lift(janela)

    label_nova_categoria = tk.Label(dialogo_categoria, text="Nova Categoria:")
    label_nova_categoria.pack()
    entrada_nova_categoria = tk.Entry(dialogo_categoria)
    entrada_nova_categoria.pack()

    botao_adicionar_categoria = tk.Button(
        dialogo_categoria, text="Adicionar", command=adicionar_categoria)
    botao_adicionar_categoria.pack()


def adicionar_dialogo_subcategoria():
    def adicionar_subcategoria():
        nova_subcategoria = entrada_nova_subcategoria.get().strip()
        categoria_selecionada = lista_categorias.get(
            lista_categorias.curselection())
        if nova_subcategoria and categoria_selecionada:
            category_phrases[categoria_selecionada][nova_subcategoria] = []
            mostrar_frases(categoria_selecionada)
            entrada_nova_subcategoria.delete(0, tk.END)
            dialogo_subcategoria.destroy()

    dialogo_subcategoria = tk.Toplevel(janela)
    dialogo_subcategoria.title("Adicionar Subcategoria")
    dialogo_subcategoria.lift(janela)

    categoria_selecionada = lista_categorias.get(
        lista_categorias.curselection())
    if categoria_selecionada:
        label_categoria = tk.Label(dialogo_subcategoria, text="Categoria:")
        label_categoria.pack()
        label_categoria_selecionada = tk.Label(
            dialogo_subcategoria, text=categoria_selecionada)
        label_categoria_selecionada.pack()

        label_nova_subcategoria = tk.Label(
            dialogo_subcategoria, text="Nova Subcategoria:")
        label_nova_subcategoria.pack()
        entrada_nova_subcategoria = tk.Entry(dialogo_subcategoria)
        entrada_nova_subcategoria.pack()

        botao_adicionar_subcategoria = tk.Button(
            dialogo_subcategoria, text="Adicionar", command=adicionar_subcategoria)
        botao_adicionar_subcategoria.pack()


def adicionar_dialogo_frase():
    def adicionar_frase():
        nova_frase = entrada_nova_frase.get().strip()
        categoria_selecionada = lista_categorias.get(
            lista_categorias.curselection())
        subcategoria_selecionada = lista_subcategorias.get(
            lista_subcategorias.curselection())
        if nova_frase and categoria_selecionada and subcategoria_selecionada:
            category_phrases[categoria_selecionada][subcategoria_selecionada].append(
                nova_frase)
            mostrar_frases(categoria_selecionada)
            entrada_nova_frase.delete(0, tk.END)
            dialogo_frase.destroy()

    dialogo_frase = tk.Toplevel(janela)
    dialogo_frase.title("Adicionar Frase")
    dialogo_frase.lift(janela)

    categoria_selecionada = lista_categorias.curselection()
    subcategoria_selecionada = lista_subcategorias.curselection()

    if categoria_selecionada and subcategoria_selecionada:
        label_categoria = tk.Label(dialogo_frase, text="Categoria:")
        label_categoria.pack()
        label_categoria_selecionada = tk.Label(
            dialogo_frase, text=lista_categorias.get(categoria_selecionada))
        label_categoria_selecionada.pack()

        label_subcategoria = tk.Label(dialogo_frase, text="Subcategoria:")
        label_subcategoria.pack()
        label_subcategoria_selecionada = tk.Label(
            dialogo_frase, text=lista_subcategorias.get(subcategoria_selecionada))
        label_subcategoria_selecionada.pack()

        label_nova_frase = tk.Label(dialogo_frase, text="Nova Frase:")
        label_nova_frase.pack()
        entrada_nova_frase = tk.Entry(dialogo_frase)
        entrada_nova_frase.pack()

        botao_adicionar_frase = tk.Button(
            dialogo_frase, text="Adicionar", command=adicionar_frase)
        botao_adicionar_frase.pack()


janela = tk.Tk()
janela.title("ATALHOS REFERA")
janela.attributes('-topmost', True)

lista_categorias = tk.Listbox(janela, width=20)
lista_categorias.pack(side=tk.LEFT, fill=tk.Y)

lista_subcategorias = tk.Listbox(janela, width=1)
lista_subcategorias.pack(side=tk.LEFT, fill=tk.Y)


category_phrases = {
    "Persiana": {
        "Fita cortada": [
            "Será feito a abertura da caixa da persiana para retirada da fita rompida e colocação da nova fita. Vamos executar testes após a troca para verificar o correto funcionamento.",
        ],
        "Persiana Presa": [
            "Será realizado o reparo no funcionamento da caixa da persiana, incluso a regulagem do painel, defeito do mecanismo de abertura da persiana.",
        ],
    },
    "Hidráulica": {
        "Troca completa registro": [
            "Por conta de ser um registro muito antigo será necessário sua substituição completa. Será retirado uma parte do azulejo para efetuar troca após isso a instalação de um azulejo similar ( pode conter variação de cor), e acabamento com rejunte.Garantimos um trabalho preciso e eficiente, restaurando o funcionamento adequado do sistema hidráulico.",
        ],
        "Troca do reparo registro": [
            "O problema está na parte interna do registro, é necessário efetuar a troca do reparo desses registros para corrigir o fluxo de água e evitar infiltrações internas.",
        ],
    },
}

for categoria in category_phrases:
    lista_categorias.insert(tk.END, categoria)

categoria_expandida = tk.StringVar()
subcategoria_expandida = tk.StringVar()

lista_categorias.bind("<Button-1>", ao_clicar)
lista_subcategorias.bind("<Button-1>", ao_clicar)

lista_frases = tk.Listbox(janela, width=50)
lista_frases.bind("<Double-Button-1>", copiar_texto)
lista_frases.bind("<Return>", copiar_texto)

lista_categorias.pack()
lista_subcategorias.pack()

menu_bar = Menu(janela)
menu_arquivo = Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Adicionar Categoria",
                         command=adicionar_dialogo_categoria)
menu_arquivo.add_command(label="Adicionar Subcategoria",
                         command=adicionar_dialogo_subcategoria)
menu_arquivo.add_command(label="Adicionar Frase",
                         command=adicionar_dialogo_frase)
menu_bar.add_cascade(label="Opções", menu=menu_arquivo)
janela.config(menu=menu_bar)

janela.mainloop()


# Comando para tornar o aquivo em executavel: python -m PyInstaller --onefile oi.py
