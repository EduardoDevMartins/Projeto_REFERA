import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext


class AplicativoArvoreTalentos:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Árvore de Talentos")

        style = ttk.Style()
        style.configure("Title.TLabel", foreground="black",
                        background="orange", font=("Arial", 22))

        self.categorias = ['Sair', 'Vazamento',
                           'Ar-condicionado', 'Elétrica', 'Caça Vazamento']

        self.label_titulo = ttk.Label(
            self.window, text="Selecione a categoria desejada:", style="Title.TLabel")
        self.label_titulo.pack()

        self.botoes_categorias = []
        for i, categoria in enumerate(self.categorias):
            botao = tk.Button(self.window, text=categoria,
                              command=lambda c=i: self.selecionar_categoria(c))
            botao.pack(side=tk.LEFT)
            self.botoes_categorias.append(botao)

        self.janela_resultado = None

        self.window.protocol("WM_DELETE_WINDOW", self.on_fechar_janela)

    def selecionar_categoria(self, indice_categoria):
        self.desabilitar_botoes()

        if indice_categoria == 0:
            self.window.destroy()
        else:
            self.janela_resultado = tk.Toplevel(self.window)
            self.janela_resultado.title("Resultado")
            self.janela_resultado.configure(bg="orange")
            self.centralizar_janela(self.janela_resultado)
            self.janela_resultado.protocol(
                "WM_DELETE_WINDOW", self.fechar_janela_resultado)

            self.categoria_atual = indice_categoria
            self.pergunta_atual = 0
            self.respostas = []

            self.mostrar_proxima_pergunta()

    def mostrar_proxima_pergunta(self):
        perguntas = {
            1: {
                "pergunta": "Selecione o tipo de residência:",
                "opcoes": ["CASA", "APARTAMENTO"]
            },
            2: {
                "pergunta": "O relógio continua girando com o registro desligado?",
                "opcoes": ["SIM", "NÃO"]
            },
            3: {
                "pergunta": "Você encontrou algum vazamento aparente?",
                "opcoes": ["SIM", "NÃO"]
            },
            # Adicione mais perguntas aqui de acordo com a categoria selecionada
        }

        informacoes_pergunta = perguntas.get(self.pergunta_atual + 1)
        if informacoes_pergunta:
            label_pergunta = tk.Label(
                self.janela_resultado, text=informacoes_pergunta["pergunta"], bg="white", fg="black", font=("Arial", 14))
            label_pergunta.pack()

            self.mostrar_opcoes(informacoes_pergunta["opcoes"])
        else:
            resultado = self.obter_resultado()
            self.mostrar_resultado(resultado)

    def mostrar_opcoes(self, opcoes):
        frame_opcoes = tk.Frame(self.janela_resultado, bg="white")
        frame_opcoes.pack()

        for opcao in opcoes:
            botao_opcao = tk.Button(
                frame_opcoes, text=opcao, command=lambda r=opcao: self.enviar_resposta(r))
            botao_opcao.pack(side=tk.LEFT)

    def enviar_resposta(self, resposta):
        self.respostas.append(resposta)
        self.pergunta_atual += 1

        self.mostrar_proxima_pergunta()

    def obter_resultado(self):
        resultado = ""
        if self.categoria_atual == 1:  # Vazamento
            tipo_residencia = self.respostas[0]
            status_registro = self.respostas[1]
            verificar_vazamento = self.respostas[2]

            if tipo_residencia == "CASA":
                if status_registro == "SIM":
                    if verificar_vazamento == "SIM":
                        resultado = 'REPARAR O VAZAMENTO'
                    elif verificar_vazamento == "NÃO":
                        resultado = 'ACIONAR CACA VAZAMENTO'
                elif status_registro == "NÃO":
                    resultado = 'Verificar possível erro da concessionária, caso negativo, instalar válvula para supressão de ar'
            elif tipo_residencia == "APARTAMENTO":
                resultado = 'ACIONAR CACA VAZAMENTO'

        return resultado

    def mostrar_resultado(self, resultado):
        label_resultado = tk.Label(self.janela_resultado, text="Resultado Final:",
                                   bg="white", fg="black", font=("Arial", 20))
        label_resultado.pack()

        texto_resultado = scrolledtext.ScrolledText(
            self.janela_resultado, width=50, height=10, bg="white", fg="black", font=("Arial", 13))
        texto_resultado.insert(tk.END, resultado)
        texto_resultado.pack()

        botao_copiar = ttk.Button(self.janela_resultado, text="Copiar",
                                  command=lambda: self.copiar_para_area_transferencia(resultado), style="Copy.TButton")
        botao_copiar.pack()

    def copiar_para_area_transferencia(self, texto):
        self.window.clipboard_clear()
        self.window.clipboard_append(texto)
        self.window.update()

    def desabilitar_botoes(self):
        for botao in self.botoes_categorias:
            botao.configure(state=tk.DISABLED)

    def habilitar_botoes(self):
        for botao in self.botoes_categorias:
            botao.configure(state=tk.NORMAL)

    def on_fechar_janela(self):
        if self.janela_resultado is not None:
            self.janela_resultado.destroy()
            self.janela_resultado = None
        self.window.clipboard_clear()
        self.window.destroy()

    def fechar_janela_resultado(self):
        if self.janela_resultado is not None:
            self.janela_resultado.destroy()
            self.janela_resultado = None
        self.habilitar_botoes()

    def centralizar_janela(self, janela):
        janela.update_idletasks()
        largura = janela.winfo_width()
        altura = janela.winfo_height()

        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()

        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2

        janela.geometry(f"+{x}+{y}")


app = AplicativoArvoreTalentos()
app.window.mainloop()
