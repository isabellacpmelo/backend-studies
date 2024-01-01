a = 'A'
b = 'B'
c = 1.1
string = 'a={1} b={0} c={nome3:.2f}'

formato = string.format(a, b, nome3=c) # Tudo que vier depois de um parametro nomeado, precisa ser nome também

print(formato)