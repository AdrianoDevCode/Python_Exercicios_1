from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o segundo cateto adjacente: '))
hy = hypot(co, ca)
print(f'O comprimento da hipotenusa é {hy:.2f}')
