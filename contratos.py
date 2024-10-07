import sqlite3
from openpyxl import workbook, load_workbook
import time
import numpy as np

def conectar():
    return sqlite3.connect('contratos.db')



def criar_tabela():
    con=conectar()
    cursor=con.cursor()
    cursor.execute('''
    create table if not exists contratos(
    id integer primary key autoincrement,
    CONTRATANTE text not null,
    NUMERO_CONTRATO text not null,
    PROCESSO_ORIGEM text not null,
    VIGENCIA text not null,
    DATA_INICIAL text not null,
    DATA_FINAL text not null,
    VALOR_TOTAL float not null,
    EXECUTADO float not null,
    EXECUTAVEL float not null
    )
    '''
    )
    con.commit()
    con.close()

def inserir_contrato(CONTRATANTE, NUMERO_CONTRATO, PROCESSO_ORIGEM, VIGENCIA, DATA_INICIAL, DATA_FINAL, VALOR_TOTAL):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        'insert into contratos (CONTRATANTE,NUMERO_CONTRATO,PROCESSO_ORIGEM,VIGENCIA,DATA_INICIAL,DATA_FINAL,'
        'VALOR_TOTAL,EXECUTADO,EXECUTAVEL)  values(?,?,?,?,?,?,?,?,?)',(CONTRATANTE, NUMERO_CONTRATO,
                                                                        PROCESSO_ORIGEM, VIGENCIA, DATA_INICIAL,
                                                                        DATA_FINAL, VALOR_TOTAL,0,VALOR_TOTAL)
    )

    con.commit()
    con.close()

def att_contrato(id,contratante,numero_contrato,processo_origem,vigencia,data_inicial,data_final,valor_total):
    con = conectar()
    cursor = con.cursor()
    cursor.execute( '''UPDATE contratos
        SET CONTRATANTE = ?,NUMERO_CONTRATO=? ,PROCESSO_ORIGEM = ?, VIGENCIA = ?, DATA_INICIAL = ?,
         DATA_FINAL = ?, VALOR_TOTAL = ?
        WHERE id = ?
    ''',(contratante,numero_contrato,processo_origem,vigencia,data_inicial,data_final,valor_total,id)

    )
    con.commit()
    con.close()

def executado_executavel(id,EXECUTADO):
    con = conectar()
    cursor = con.cursor()
    cursor.execute('select EXECUTADO,VALOR_TOTAL from '
                   'contratos WHERE id =?',(id,))
    resultado=cursor.fetchone()
    if resultado:
        executado_atual,valor_total=resultado
        novo_executado=executado_atual+EXECUTADO
        executavel=valor_total-novo_executado

        cursor.execute('''
                    UPDATE contratos
                    SET EXECUTADO = ?, EXECUTAVEL = ?
                    WHERE id = ?
                ''', (novo_executado, executavel, id))

        con.commit()

    con.close()

def visualizar():
    con=conectar()
    cursor=con.cursor()
    cursor.execute("select  * from  contratos")
    resultado=cursor.fetchall()
    con.close()
    return resultado

def deletar_registros():
    con=conectar()
    cursor=con.cursor()
    cursor.execute(' delete from  contratos;')
    con.commit()
    con.close()

def menu_contratos():
    while True:
        print("\nSistema de Gerenciamento de Contratos")
        print("1. Criar planilha")
        print("2. Inserir novo contrato")
        print("3. Atualizar contrato existente")
        print("4. Adicionar valor executado a um contrato")
        print("5. ver registros")
        print("6. apagar registro individual")
        print("7. apagar todos os registros")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao=='1':
            conectar()
            criar_tabela()

        elif opcao == '2':
            contratante = input("Digite o nome do contratante: ")
            numero_contrato = input("Digite o número do contrato: ")
            processo_origem = input("Digite o processo de origem: ")
            vigencia = input("Digite a vigência: ")
            data_inicial = input("Digite a data inicial (YYYY-MM-DD): ")
            data_final = input("Digite a data final (YYYY-MM-DD): ")
            valor_total = float(input("Digite o valor total do contrato: "))

            inserir_contrato(contratante, numero_contrato, processo_origem, vigencia, data_inicial, data_final, valor_total)
            print("Contrato inserido com sucesso!")

        elif opcao == '3':
            id = int(input("Digite o ID do contrato a ser atualizado: "))
            contratante = input("Digite o novo nome do contratante: ")
            numero_contrato = input("Digite o novo número do contrato: ")
            processo_origem = input("Digite o novo processo de origem: ")
            vigencia = input("Digite a nova vigência: ")
            data_inicial = input("Digite a nova data inicial (YYYY-MM-DD): ")
            data_final = input("Digite a nova data final (YYYY-MM-DD): ")
            valor_total = float(input("Digite o novo valor total do contrato: "))

            att_contrato(id, contratante, numero_contrato, processo_origem, vigencia, data_inicial, data_final, valor_total)
            print("Contrato atualizado com sucesso!")

        elif opcao == '4':
            id = int(input("Digite o ID do contrato para adicionar valor executado: "))
            executado = float(input("Digite o valor executado: "))

            executado_executavel(id, executado)
            print("Valores executados atualizados com sucesso!")
        elif opcao=='5':
            registros=visualizar()
            for registro in registros:
                print(f'id {registro[0]} contratante: {registro[1]} numero: {registro[2]}  processo {registro[3]}'
                      f'vigencia de {registro[4]}  indo de  {registro[5]} a {registro[6]} com valor total de '
                      f'R$ {registro[7]:.2f} tendo sido executado R$ {registro[8]:.2f} e restando R$ {registro[9]:.2f} '
                      f'a executar')

        elif opcao=='7':
            deletar=input('deseja mesmo limpar a tabela? ').strip(). upper()
            if deletar =='S':
                time.sleep(10)
                certeza=input('Caso Mude de ideia tem 10 segundos para cancelar: ').strip(). upper()
                if certeza =='S':
                    deletar_registros()

        elif opcao == '8':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ =='__main__':
    menu_contratos()





