# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip().upper()
if cupom not in descontos:
    print('Cupom inválido. Nenhum desconto aplicado.')
elif cupom == 'SEM_DESCONTO':
    print(f'{preco:.2f}')
elif cupom == 'DESCONTO10':
    print(f'{preco - (preco*0.10):.2f}')
elif cupom == 'DESCONTO20':
    print(f'{preco - (preco*0.20):.2f}')    


# TODO: Aplique o desconto se o cupom for válido: