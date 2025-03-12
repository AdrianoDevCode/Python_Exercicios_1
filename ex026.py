frase = input("Digite uma frase: ").strip().upper()  # Remove espaços extras e converte para maiúsculas

# Conta quantas vezes "A" aparece na frase
quantidade_a = frase.count("A")

# Posição da primeira ocorrência (somamos 1 para ajustar para posição humana)
primeira_posicao = frase.find("A") + 1

# Posição da última ocorrência (somamos 1 pelo mesmo motivo)
ultima_posicao = frase.rfind("A") + 1

# Exibe os resultados
print(f"A letra 'A' aparece {quantidade_a} vezes.")
print(f"A primeira ocorrência está na posição {primeira_posicao}.")
print(f"A última ocorrência está na posição {ultima_posicao}.")
