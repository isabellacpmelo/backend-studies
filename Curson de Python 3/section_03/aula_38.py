"""
Iterando strings com while
"""

nome = 'Isabella Melo' # Strings são iteraveis, ou seja, podemos percorrer seus caracteres

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

indice = 0
novo_nome = ''

while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)