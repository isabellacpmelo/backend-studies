"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

nome = 'Isabella'
preco = 1000.956345234
variavel = '%s, o preço e R$ %.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %04X' % (15, 15))