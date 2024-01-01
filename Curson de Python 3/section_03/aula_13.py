nome = 'Jacobel Lindton'
altura = 1.97
peso = 1090
imc = ...

imc = peso / (altura ** 2)

frase = f'{nome} tem {altura: .2f} de altura, pesa {peso: ,.2f} quilos e seu IMC é {imc:.2f}'

print(frase)