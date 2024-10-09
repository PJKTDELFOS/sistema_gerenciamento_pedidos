import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog


def conectar():
    return sqlite3.connect('contratos.db')


def criar_tabela():
    con = conectar()
    cursor = con.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contratos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        CONTRATANTE TEXT NOT NULL,
        NUMERO_CONTRATO TEXT NOT NULL,
        PROCESSO_ORIGEM TEXT NOT NULL,
        VIGENCIA TEXT NOT NULL,
        DATA_INICIAL TEXT NOT NULL,
        DATA_FINAL TEXT NOT NULL,
        VALOR_TOTAL FLOAT NOT NULL,
        EXECUTADO FLOAT NOT NULL,
        EXECUTAVEL FLOAT NOT NULL
    )
    ''')
    con.commit()
    con.close()


def inserir_contrato(CONTRATANTE, NUMERO_CONTRATO, PROCESSO_ORIGEM, VIGENCIA, DATA_INICIAL, DATA_FINAL, VALOR_TOTAL):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        'INSERT INTO contratos (CONTRATANTE, NUMERO_CONTRATO, PROCESSO_ORIGEM, VIGENCIA, DATA_INICIAL, DATA_FINAL, VALOR_TOTAL, EXECUTADO, EXECUTAVEL) VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?)',
        (CONTRATANTE, NUMERO_CONTRATO, PROCESSO_ORIGEM, VIGENCIA, DATA_INICIAL, DATA_FINAL, VALOR_TOTAL, VALOR_TOTAL)
    )
    con.commit()
    con.close()


def att_contrato(id, contratante, numero_contrato, processo_origem, vigencia, data_inicial, data_final, valor_total):
    con = conectar()
    cursor = con.cursor()
    cursor.execute('''UPDATE contratos
                      SET CONTRATANTE = ?, NUMERO_CONTRATO = ?, PROCESSO_ORIGEM = ?, VIGENCIA = ?, DATA_INICIAL = ?, DATA_FINAL = ?, VALOR_TOTAL = ?
                      WHERE id = ?''',
                   (contratante, numero_contrato, processo_origem, vigencia, data_inicial, data_final, valor_total, id))
    con.commit()
    con.close()


def executado_executavel(id, EXECUTADO):
    con = conectar()
    cursor = con.cursor()
    cursor.execute('SELECT EXECUTADO, VALOR_TOTAL FROM contratos WHERE id = ?', (id,))
    resultado = cursor.fetchone()
    if resultado:
        executado_atual, valor_total = resultado
        novo_executado = executado_atual + EXECUTADO
        executavel = valor_total - novo_executado
        cursor.execute('UPDATE contratos SET EXECUTADO = ?, EXECUTAVEL = ? WHERE id = ?',
                       (novo_executado, executavel, id))
        con.commit()
    con.close()


def visualizar():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM contratos")
    resultado = cursor.fetchall()
    con.close()
    return resultado


def deletar_registros():
    con = conectar()
    cursor = con.cursor()
    cursor.execute('DELETE FROM contratos;')
    con.commit()
    con.close()


class ContratosApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gerenciamento de Contratos")

        self.create_widgets()

    def create_widgets(self):
        # Botão para criar tabela
        tk.Button(self.master, text="Criar Tabela", command=self.criar_tabela).pack(pady=10)

        # Botão para inserir contrato
        tk.Button(self.master, text="Inserir Contrato", command=self.inserir_contrato).pack(pady=10)

        # Botão para atualizar contrato
        tk.Button(self.master, text="Atualizar Contrato", command=self.atualizar_contrato).pack(pady=10)

        # Botão para adicionar valor executado
        tk.Button(self.master, text="Adicionar Valor Executado", command=self.adicionar_executado).pack(pady=10)

        # Botão para visualizar contratos
        tk.Button(self.master, text="Visualizar Contratos", command=self.visualizar_contratos).pack(pady=10)

        # Botão para deletar registros
        tk.Button(self.master, text="Deletar Registros", command=self.deletar_registros).pack(pady=10)

    def criar_tabela(self):
        criar_tabela()
        messagebox.showinfo("Info", "Tabela criada com sucesso!")

    def inserir_contrato(self):
        contratante = simpledialog.askstring("Entrar", "Nome do Contratante:")
        numero_contrato = simpledialog.askstring("Entrar", "Número do Contrato:")
        processo_origem = simpledialog.askstring("Entrar", "Processo de Origem:")
        vigencia = simpledialog.askstring("Entrar", "Vigência:")
        data_inicial = simpledialog.askstring("Entrar", "Data Inicial (YYYY-MM-DD):")
        data_final = simpledialog.askstring("Entrar", "Data Final (YYYY-MM-DD):")
        valor_total = simpledialog.askfloat("Entrar", "Valor Total do Contrato:")

        if None not in (contratante, numero_contrato, processo_origem, vigencia, data_inicial, data_final, valor_total):
            inserir_contrato(contratante, numero_contrato, processo_origem, vigencia, data_inicial, data_final,
                             valor_total)

            messagebox.showinfo("Info", "Contrato inserido com sucesso!")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

    def atualizar_contrato(self):
        id = simpledialog.askinteger("Entrar", "ID do Contrato:")
        contratante = simpledialog.askstring("Entrar", "Novo Nome do Contratante:")
        numero_contrato = simpledialog.askstring("Entrar", "Novo Número do Contrato:")
        processo_origem = simpledialog.askstring("Entrar", "Novo Processo de Origem:")
        vigencia = simpledialog.askstring("Entrar", "Nova Vigência:")
        data_inicial = simpledialog.askstring("Entrar", "Nova Data Inicial (YYYY-MM-DD):")
        data_final = simpledialog.askstring("Entrar", "Nova Data Final (YYYY-MM-DD):")
        valor_total = simpledialog.askfloat("Entrar", "Novo Valor Total do Contrato:")

        if None not in (
        id, contratante, numero_contrato, processo_origem, vigencia, data_inicial, data_final, valor_total):
            att_contrato(id, contratante, numero_contrato, processo_origem, vigencia, data_inicial, data_final,
                         valor_total)
            messagebox.showinfo("Info", "Contrato atualizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

    def adicionar_executado(self):
        id = simpledialog.askinteger("Entrar", "ID do Contrato:")
        executado = simpledialog.askfloat("Entrar", "Valor Executado:")

        if id is not None and executado is not None:
            executado_executavel(id, executado)
            messagebox.showinfo("Info", "Valores executados atualizados com sucesso!")
        else:
            messagebox.showerror("Erro", "ID e Valor Executado são obrigatórios!")

    def visualizar_contratos(self):
        registros = visualizar()
        if registros:
            resultado = "\n".join(
                f'ID: {registro[0]}, Contratante: {registro[1]}, Número: {registro[2]}, Processo: {registro[3]}, '
                f'Vigência: {registro[4]}, Data Inicial: {registro[5]}, Data Final: {registro[6]}, Valor Total: R$ {registro[7]:.2f}, '
                f'Executado: R$ {registro[8]:.2f}, Executável: R$ {registro[9]:.2f}'
                for registro in registros)
            messagebox.showinfo("Contratos", resultado)
        else:
            messagebox.showinfo("Contratos", "Nenhum registro encontrado.")

    def deletar_registros(self):
        resposta = messagebox.askyesno("Confirmar", "Deseja realmente apagar todos os registros?")
        if resposta:
            deletar_registros()
            messagebox.showinfo("Info", "Todos os registros foram deletados.")


if __name__ == '__main__':
    root = tk.Tk()
    app = ContratosApp(root)
    root.mainloop()
