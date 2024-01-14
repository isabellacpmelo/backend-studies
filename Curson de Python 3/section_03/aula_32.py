"""
https://docs.python.org/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'thomas Jefferson'
#string[3] = 'ABC' # TypeError : 'str' object does not support item assignment
outra_variavel = f'{string[:3]}ABC{string[4:]}'

print(outra_variavel.capitalize())
print(outra_variavel.zfill(100))