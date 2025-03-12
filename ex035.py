# Função para verificar se pode formar um triângulo
def pode_formar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Leitura das três retas
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

# Verificar se pode ou não formar um triângulo
if pode_formar_triangulo(a, b, c):
    print("As retas podem formar um triângulo!")
else:
    print("As retas NÃO podem formar um triângulo.")
