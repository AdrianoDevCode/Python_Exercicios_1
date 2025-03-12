produto = float(input('Digite o preço do produto: '))
desconto = produto * 0.05
real = produto - desconto
print('Parabéns seu produto de {}R$ reais recebeu um desconto de 5% e ficou valendo apenas: {}'.format(produto, real))