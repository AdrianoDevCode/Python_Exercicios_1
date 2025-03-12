from math import sin, cos, tan, radians
a = float(input('Digite um ángulo qualquer: '))
r = radians(a)
s = sin(a)
c = cos(a)
t = tan(a)
print(f'O ângulo de {a}º tem:')
print(f'Seno: {s:.2f}')
print(f'Cosseno: {c:.2f}')
print(f'Tangente: {t:.2f}')


