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
    if tabuleiro[linha][coluna] != ' ':
        print('Jogada inválida!')
        return jogador
    tabuleiro[linha][coluna] = jogador
    return 'O' if jogador == 'X' else 'X'


while True:
    print(f'Jogador da vez: {jogador}')
    linha = int(input('Digite a linha: '))
    coluna = int(input('Digite a coluna: '))
    jogador = jogada(linha, coluna)
    exibeTabuleiro