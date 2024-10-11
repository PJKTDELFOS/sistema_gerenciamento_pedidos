# def cnpj(cnpj):
#     return '{}.{}.{}/{}-{}'.format(
#         cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])
# def ler_cnpj(cnpjn):
#     return f' o cnpj é {cnpj(cnpjn)}'
# def validacao_CNPJ():
#     while True:
#         try:
#             cnpjn = input('Digite o Cnpj: ')
#             if len(cnpjn) != 14 or not cnpjn.isdigit():
#                 raise ValueError('CNPJ inválido')
#             return cnpjn
#         except ValueError as e:
#             print(e)
#             print('Porfavor ,tente novamente.\n')
#
#
# cnpjn = validacao_CNPJ()
# cnpj = ler_cnpj(cnpjn)
# print(cnpj)
'validação cnpj atualizada'
# def ler_CNPJ(numero):
#     while True:
#         try:
#             return cnpj(numero)
#         except ValueError as e:
#             print(f'erro{e}, tente Novamente')
#             numero = input("Digite o CNPJ (14 dígitos):")
# def cnpj(cnpj):
#     if cnpj is None:
#         raise  ValueError('o cnpj nao foi fornecido')
#     if len(cnpj) !=14 or not cnpj.isdigit():
#         raise ValueError('O CNPJ fornecido deve ter 14 dígitos numéricos')
#     return "{}.{}.{}-{}/{}".format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])
#
#
# numero=input('numero:')
#
# cnnpj=ler_CNPJ(numero)
# print(cnnpj)


# def frase(a,b,c,d,e):
#     return f'{a},{b},{c},{d},{e}'
#
#
# def valor_atual(valor):
#     valor=frase(a,b,c,d,e)
#     while valor_atual is None or valor_atual=='':
#         valor=frase(a,b,c,d,e)
#     return valor
#
#
# a=input("palavra a ")
# b=input("palavra b ")
# c=input("palavra c ")
# d=input("palavra d ")
# e=input("palavra e ")
#
# valor_atual(frase(a,b,c,d,e))



def frase(a, b, c, d, e):
    return f'{a},{b},{c},{d},{e}'

# Função auxiliar para solicitar nova entrada se a palavra for None ou vazia
def solicita_input(variavel_nome, valor_atual):
    while valor_atual is None or valor_atual == "":
        valor_atual = input(f"Insira novamente {variavel_nome}: ")
    return valor_atual

# Solicitar entradas inicialmente
a = input("palavra a ")
b = input("palavra b ")
c = input("palavra c ")
d = input("palavra d ")
e = input("palavra e ")

# Verificar se alguma variável está como None ou vazia e pedir novamente
a = solicita_input("palavra a", a)
b = solicita_input("palavra b", b)
c = solicita_input("palavra c", c)
d = solicita_input("palavra d", d)
e = solicita_input("palavra e", e)

# Chamar a função com os valores finais
print(frase(a, b, c, d, e))
