viagemkm = float(input('Digite a distância em km da viagem: '))

if viagemkm <= 200:
    tarifa = viagemkm * 0.50  # Preço por km para viagens até 200 km
else:
    tarifa = viagemkm * 0.45  # Preço por km para viagens acima de 200 km

print(f'A distância da sua viagem é de {viagemkm} km, e o preço da passagem será de R${tarifa:.2f}')
