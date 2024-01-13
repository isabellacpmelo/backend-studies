"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

condicao = False

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    passou_no_if = None
    print('Nao faça algo')

if passou_no_if is None:
    print('Nao passou no if')
    print(passou_no_if, passou_no_if is None)
else:
    print('Passou no if')
    print(passou_no_if, passou_no_if is not None)
