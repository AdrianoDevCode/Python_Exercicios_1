#Resolvido com inteiro/ operadores matemáticos.
n = int(input("Digite um número de 0 até 9999: "))

unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10

print(f"Seu número é {n}")
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
