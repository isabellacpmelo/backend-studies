""" while/else """

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break
    print(letra)
    i += 1
else:
    print('Não encontrou espaco na string!') # executado apenas se o while for executado

print('Fora do while')