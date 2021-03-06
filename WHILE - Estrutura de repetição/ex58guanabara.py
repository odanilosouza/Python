'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
computador = randint(0,10)
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite +=1
    if computador == jogador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')
print('Acertou com {} tentativas '.format(palpite))