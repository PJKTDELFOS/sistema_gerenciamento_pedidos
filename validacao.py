def cnpj(cnpj):
    return '{}.{}.{}/{}-{}'.format(
        cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:]
    )


def ler_cnpj(cnpjn):
    return f' o cnpj é {cnpj(cnpjn)}'


def validacao():
    while True:
        try:
            cnpjn = input('Digite o Cnpj: ')
            if len(cnpjn) != 14 or not cnpjn.isdigit():
                raise ValueError('CNPJ inválido')
            return cnpjn
        except ValueError as e:
            print(e)
            print('Porfavor ,tente novamente.\n')


cnpjn = validacao()
cnpj = ler_cnpj(cnpjn)
print(cnpj)