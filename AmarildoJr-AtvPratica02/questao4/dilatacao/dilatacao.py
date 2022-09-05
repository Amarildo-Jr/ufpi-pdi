from PIL import Image

import sys
sys.path.insert(0, "questao3")
from operacoes_morfologicas import diferenca

def max_intensidade(imagem):
    max = 0
    for x in range(imagem.width):
        for y in range(imagem.height):
            if imagem.getpixel((x, y)) > max:
                max = imagem.getpixel((x, y))
    return max

def dilatacao(image, elemento_estruturante, centro):
    imagem_saida = Image.new("L", image.size)

    intensidade_max = max_intensidade(image)

    for x in range(imagem_saida.width):
        for y in range(imagem_saida.height):
            if(image.getpixel((x, y)) == intensidade_max):
                for i in range(len(elemento_estruturante)):
                    for j in range(len(elemento_estruturante[i])):
                        if(elemento_estruturante[i][j] == 1):
                            imagem_saida.putpixel((x + i - centro[0], y + j - centro[1]), intensidade_max)
    
    return imagem_saida


if __name__ == "__main__":
    # 3x3
    elemento_est = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    centro = (1, 1)

    # 5x3
    # elemento_est = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # centro = (2, 1)

    # 3x5
    # elemento_est = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    # centro = (1, 2)

    # imagem = Image.open("questao4/retangulo_buracos.bmp").convert("L")

    # imagem_saida = dilatacao(imagem, elemento_est, centro)
    # imagem_saida.save("questao4/dilatacao/retangulo_buracos_dilatado_3x3.jpg")

    # imagem1 = Image.open("questao4/retangulo.bmp").convert("L")
    # imagem2 = Image.open("questao4/dilatacao/retangulo_dilatado_3x3.jpg").convert("L")
    # imagem2 = Image.open("questao4/dilatacao/retangulo_buracos_dilatado_3x3.jpg").convert("L")
    # diferenca(imagem2, imagem1).save("questao4/dilatacao/retangulo_diferenca.jpg")