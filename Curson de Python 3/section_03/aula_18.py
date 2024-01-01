"""
Operadores de comparação (relacionais)
OP | Significado | Exemplo (True)
>  | Maior        | 10 > 5
>= | Maior igual  | 10 >= 10
<  | Menor        | 10 < 15
<= | Menor igual  | 10 <= 10
== | Igual        | 10 == 10
!= | Diferente    | 10 != 5
"""

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

print(maior, maior_ou_igual, menor, menor_ou_igual, igual, diferente, sep='\n')