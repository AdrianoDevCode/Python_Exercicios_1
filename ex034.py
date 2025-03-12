salario = float(input('Digite o seu salário para correção : '))
if salario > 1250.00:
    salario10 = (salario * 0.10) + salario
    print(f'Seu salário de {salario:.2f}R$ passou a ser de {salario10:.2f}')
else:
    salario15 = (salario * 0.15) + salario
    print(f'Seu salário de {salario:.2f}R$ passou a ser de {salario15:.2f}')
