# Operadores in e not in
# Strings sao iteraveis, ou seja, podemos percorrer seus caracteres
# 0 1 2 3 4 5
# I s a b e l l a
# -6-5-4-3-2-1

nome = 'Isabella'
print(nome[3]) # de frente para tras
print(nome[-5]) # de tras para frente

print('a' in nome)
print('z' not in nome)

nome_user = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar no seu nome: ')

if encontrar in nome_user:
    print(f'{encontrar} está contido em {nome_user}')
else:
    print(f'{encontrar} não está contido em {nome_user}')