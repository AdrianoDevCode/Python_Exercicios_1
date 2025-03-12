import pygame
pygame.init()
velocidade = float(input('Digite a velocidade máxima registrada: '))
velocidadepermitida = 80
valorporkm = 7

if velocidade <= 80:
        print(f'Sua velocidade máxima registrada foi de {velocidade}KM e está dentro da velocidade permitida.')
else:

    multa = (velocidade - velocidadepermitida) * valorporkm
    print(f'Sua velocidade máxima registrada foi de {velocidade}KM portanto, a multa no valor de {multa:.2f}R$ será enviada para o sua residência.')
    try:
        pygame.mixer.music.load('sirenpolice.mp3')
        pygame.mixer.music.play()

        input('Pressione Enter para continuar...')

    except pygame.error as e:
        print(f'Erro ao carregar o áudio: {e}')