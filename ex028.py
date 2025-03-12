import random
import pygame

# Inicializando pygame
pygame.init()

# Gerando número aleatório
n = int(input('Tente adivinhar o número que eu estou pensando, de 0 a 5: '))
num = random.choice([0, 1, 2, 3, 4, 5])

# Exibindo resultado
print(f'O número que eu escolhi foi: {num} e o seu número foi: {n}')

if n == num:
    print('Você acertou na mosca!! PARABÉNS!!')

    # Carregando e tocando o áudio
    try:
        pygame.mixer.music.load('queen.mp3')
        pygame.mixer.music.play()

        input('Pressione Enter para continuar...')

    except pygame.error as e:
        print(f'Erro ao carregar o áudio: {e}')

else:
    print('Você errou XD')
    try:
        pygame.mixer.music.load('quepena.mp3')
        pygame.mixer.music.play()

        input('Pressione Enter para continuar...')
    except pygame.error as e:
        print(f'Erro ao carregar o áudio: {e}')



pygame.quit()
