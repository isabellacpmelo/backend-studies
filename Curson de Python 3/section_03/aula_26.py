"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome conteém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba:
        "Desculpe, você deixou campos vazios."
"""

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')

if nome == '' or idade == '':
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f"Seu nome {'não tem' if nome.count(' ') == 0 else 'tem'} espaços")
    print(f'Seu nome tem "{len(nome)}" letras')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A última letra do seu nome é "{nome[-1]}"')
