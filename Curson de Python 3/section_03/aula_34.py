"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador < 10:
    print(f'{contador} - Print antes do while')
    contador = contador + 1
    print(f'{contador} - Print depois do while')

print('Acabou!')