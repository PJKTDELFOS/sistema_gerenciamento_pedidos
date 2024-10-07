from gerenciamento_pedidos import menu_pedidos
from processos import menu_processos
from contratos import menu_contratos



def menu_comercial():
    while True:
        print("\nMenu:")
        print("1. PROCESSOS")
        print("2. PEDIDOS")
        print("3. CONTRATOS")
        print("4. SAIR")

        comercial = input("didite uma opção")

        if comercial=='1':
            menu_processos()
        elif  comercial=='2':
            menu_pedidos()
        elif comercial=='3':
            menu_contratos()
        elif comercial=='4':
            print('Programa Encerrando ')
            break





menu_comercial()









