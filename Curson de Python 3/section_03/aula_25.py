"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da string
"""

variavel = 'Olá mundo'
print(len(variavel[4:7])) # o indice 7 não entra na string
print(variavel[0:len(variavel):2]) # pulando de 2 em 2
print(variavel[-1:-10:-1]) # inversão da string 
print(variavel[::-1]) # inversão da string 