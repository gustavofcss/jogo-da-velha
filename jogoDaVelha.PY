tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

jogador = 'X'

def exibeTabuleiro():
    for linha in tabuleiro:
        print(f'{linha[0]} | {linha[1]} | {linha[2]}')
        print('- - - - -')
        
def jogada(linha, coluna):
    tabuleiro[linha][coluna] = jogador
    if jogador == 'X':
        return 'O'
    else:
        return 'X'

jogador = jogada(1,1)
jogador = jogada(1,2)
exibeTabuleiro()