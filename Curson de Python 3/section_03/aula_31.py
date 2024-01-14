"""
Exercicio 1
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número e par ou impar. Caso o usuário não digite um número inteiro, informe que não e um numero inteiro.
"""

"""
Exercicio 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, mostre a saudacão apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

"""
Exercicio 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome e muito curto". Se tiver entre 5 e 6 letras, escreva "Seu nome e normal". Se tiver 7 ou mais letras, escreva "Seu nome e muito grande"
"""

# Exercicio 1
numero = input('Digite um numero inteiro: ')

try :
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('Seu numero e par')
    else:
        print('Seu numero e impar')
except:
    print('Isso não e um numero inteiro')

# Exercicio 2
hora = input('Digite a hora atual: ')

try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite')
    else:
        print('Hora invalida')
except:
    print('Isso não e um horário')

# Exercicio 3
nome = input('Qual é o seu nome? ')

try:
    if len(nome) <= 4:
        print('Seu nome e muito curto')
    elif len(nome) >= 5 and len(nome) <= 6:
        print('Seu nome e normal')
    else:
        print('Seu nome e muito grande')
except:
    print('Isso não e um nome')