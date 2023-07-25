import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import tkinter.scrolledtext as scrolledtext


class TalentTreeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Árvore de Talentos")

        style = ttk.Style()
        style.configure("Title.TLabel", foreground="black",
                        background="orange", font=("Arial", 22))

        self.df = self.carregar_dados_do_excel()
        self.categorias = self.df['Categoria'].unique()

        self.title_label = ttk.Label(
            self.window, text="Selecione a categoria desejada:", style="Title.TLabel")
        self.title_label.pack()

        self.category_buttons = []
        for i, category in enumerate(self.categorias):
            button = tk.Button(self.window, text=category,
                               command=lambda c=i+1: self.select_category(c))
            button.pack(side=tk.LEFT)
            self.category_buttons.append(button)

        self.result_window = None
        self.current_category = None
        self.current_question = 0
        self.answers = []

        self.window.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def carregar_dados_do_excel(self):
        df = pd.read_excel(
            r"C:\Users\Eduardo\Desktop\CaminhoDev\Linguagens\Python\Projeto_orcamentista\testes\perguntas_respostas.xlsx")
        return df

    def select_category(self, category_index):
        self.disable_buttons()

        if category_index == 0:
            self.window.destroy()
        else:
            self.current_category = self.categorias[category_index - 1]
            self.current_question = 0
            self.answers = []

            self.show_next_question()

    def show_next_question(self):
        filtered_df = self.df[self.df['Categoria'] == self.current_category]

        if not filtered_df.empty:
            filtered_df = filtered_df.reset_index(drop=True)
            if self.current_question < len(filtered_df):
                question_label = tk.Label(
                    self.window, text=filtered_df.loc[self.current_question, 'Pergunta'], bg="white", fg="black", font=("Arial", 14))
                question_label.pack()

                self.show_options(
                    str(filtered_df.loc[self.current_question, 'Resposta']),
                    str(filtered_df.loc[self.current_question, 'Caminho 1']),
                    str(filtered_df.loc[self.current_question, 'Caminho 2'])
                )
            else:
                result = self.get_result()
                self.show_result(result)

    def show_options(self, options, path_1, path_2):
        option_frame = tk.Frame(self.window, bg="white")
        option_frame.pack()

        for option in options.split(','):
            if '/' in option:
                sub_options = option.split('/')
                sub_frame = tk.Frame(option_frame, bg="white")
                sub_frame.pack()
                for sub_option in sub_options:
                    sub_option_button = tk.Button(
                        sub_frame, text=sub_option.strip(), command=lambda a=sub_option.strip(): self.submit_answer(a, path_1, path_2))
                    sub_option_button.pack(side=tk.LEFT)
            else:
                option_button = tk.Button(
                    option_frame, text=option.strip(), command=lambda a=option.strip(): self.submit_answer(a, path_1, path_2))
                option_button.pack(side=tk.LEFT)

    def submit_answer(self, answer, path_1, path_2):
        self.answers.append(answer)
        self.current_question += 1

        if answer == self.df.loc[self.current_question - 1, 'Resposta']:
            result = self.df.loc[self.current_question - 1, path_1]
        else:
            result = self.df.loc[self.current_question - 1, path_2]

        self.show_result(result)

    def show_result(self, result):
        result_window = tk.Toplevel(self.window)
        result_window.title("Resultado")
        result_window.configure(bg="white")

        result_label = tk.Label(result_window, text="Resultado Final:",
                                bg="white", fg="black", font=("Arial", 20))
        result_label.pack()

        result_text = scrolledtext.ScrolledText(
            result_window, width=50, height=10, bg="white", fg="black", font=("Arial", 13))
        result_text.insert(tk.END, result)
        result_text.pack()

        copy_button = ttk.Button(result_window, text="Copiar",
                                 command=lambda: self.copy_to_clipboard(result))
        copy_button.pack()

        result_window.protocol(
            "WM_DELETE_WINDOW", lambda: self.close_result_window(result_window))

    def copy_to_clipboard(self, text):
        self.window.clipboard_clear()
        self.window.clipboard_append(text)
        self.window.update()

    def disable_buttons(self):
        for button in self.category_buttons:
            button.configure(state=tk.DISABLED)

    def enable_buttons(self):
        for button in self.category_buttons:
            button.configure(state=tk.NORMAL)

    def on_window_close(self):
        if self.result_window is not None:
            self.result_window.destroy()
            self.result_window = None
        self.window.clipboard_clear()
        self.window.destroy()

    def close_result_window(self, result_window):
        if self.result_window is not None:
            self.result_window.destroy()
            self.result_window = None
        self.enable_buttons()
        result_window.destroy()


app = TalentTreeApp()
app.window.mainloop()
