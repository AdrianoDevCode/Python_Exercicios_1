#Resolvido como STRING
n = input('Digite um número de 0 até 9999: ')

n = n.zfill(4)


print(f'Seu número é {n}')
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')
