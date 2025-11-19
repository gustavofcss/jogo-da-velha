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
    global jogador
    tabuleiro[linha][coluna] = jogador
    if jogador == 'X':
        jogador = 'O'
    else:
        jogador = 'X'

jogada(1,1)
jogada(1,2)
exibeTabuleiro()