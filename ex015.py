dias = int(input('Quantos dias foram alugados? '))
km = float(input('Quantos Km foram percorridos? '))
ckm = km * 0.15
cdia =  dias * 60
aluguel = ckm + cdia
print('Baseado no km rodado {}Km foi cobrado {}R$, e no(s) dia(s) alugado(s) {} dias por {}R$ , o total a pagar é:{:.2f}R$'.format(km, ckm,  dias, cdia, aluguel))