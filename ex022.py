nome = str(input('Digite o seu nome completo: ')).strip() #Strip já vai eliminar os espaços vazios antes da primeira palavra e depois da ultima
print('Analisando o seu nome...')
print(f'Seu nome em maiúsculas é: {nome}')
print(f'Seu nome em minúsculas é: {nome}')
#print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')}')
separa = nome.split()
print(f'Seu primeiro nome é: {separa[0]} e ele possui {len(separa[0])} letras')

