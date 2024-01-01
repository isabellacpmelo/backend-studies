# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condioes precisam ser verdadeiras
# or - Qualquer uma das condicoes precisa ser verdadeira
# not - Inverte o resultado da condicao

# São considerados falsy: False, None, 0, 0.0, '', (), [], {}
# None é usado para representar um valor nulo

# Exemplos
print(bool(None), bool(False), bool(0), bool(0.0), bool(''), bool(()), bool([]), bool({}), sep='\n')

# And
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and (senha_digitada == senha_permitida):
    print('Entrar')
else:
    print('Sair')