"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
(Caractere)(><^)(quantidade)
> -> Esquerda
< -> Direita
^ -> Centro
Sinal - ou +
Ex.: 0>-100, .1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:T^10}.')
print(f'{1000.41238394821:0=+10,.1f}')

