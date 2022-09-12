from PIL import Image

import sys
sys.path.insert(0, "questao3")
sys.path.insert(1, "questao4/dilatacao")
sys.path.insert(2, "questao4/erosao")
# from operacoes_morfologicas import diferenca


from dilatacao import dilatacao
from erosao import erosao

def abertura(imagem, elemento_estruturante, centro):
    imagem_erodida = erosao(imagem, elemento_estruturante, centro)
    imagem_saida = dilatacao(imagem_erodida, elemento_estruturante, centro)
    return imagem_saida

if __name__ == "__main__":
    # 3x3
    elemento_est = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    centro = (1, 1)

    imagem = Image.open("questao4/retangulo.bmp").convert("L")

    imagem_saida = abertura(imagem, elemento_est, centro)
    imagem_saida.save("questao4/abertura/retangulo_abertura_3x3.jpg")

    # imagem = Image.open("questao4/conectados.bmp").convert("L")

    # imagem_saida = abertura(imagem, elemento_est, centro)
    # imagem_saida.save("questao4/abertura/conectados_abertura_3x3.jpg")