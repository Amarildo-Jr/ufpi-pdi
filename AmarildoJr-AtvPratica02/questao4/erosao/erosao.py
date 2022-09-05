from PIL import Image

import sys
sys.path.insert(0, "questao3")
sys.path.insert(1, "questao4/dilatacao")


from operacoes_morfologicas import diferenca
from dilatacao import max_intensidade

def erosao(image, elemento_estruturante, centro):
    imagem_saida = Image.new("L", image.size)

    intensidade_max = max_intensidade(image)
    for x in range(imagem_saida.width):
        for y in range(imagem_saida.height):
            if image.getpixel((x, y)) == intensidade_max:
                elemento_est_encontrado = True
                for i in range(len(elemento_estruturante)):
                    for j in range(len(elemento_estruturante[i])):
                        # imagem_saida.putpixel((x + i - centro[0], y + j - centro[1]), 0)
                        if elemento_estruturante[i][j] == 1:
                            if not image.getpixel((x + i - centro[0], y + j - centro[1])) == intensidade_max:
                                elemento_est_encontrado = False
                        
                if elemento_est_encontrado:
                    imagem_saida.putpixel((x, y), intensidade_max)
    return imagem_saida

if __name__ == "__main__":
    # 3x3
    # elemento_est = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # centro = (1, 1)

    # imagem = Image.open("questao4/retangulo_buracos.bmp").convert("L")

    # imagem_saida = erosao(imagem, elemento_est, centro)
    # imagem_saida.save("questao4/erosao/retangulo_buracos_erodido_3x3.jpg")

    imagem1 = Image.open("questao4/retangulo_buracos.bmp").convert("L")
    imagem2 = Image.open("questao4/erosao/retangulo_buracos_erodido_3x3.jpg").convert("L")
    # imagem2 = Image.open("questao4/erosao/retangulo_buracos_erodido_3x3.jpg").convert("L")
    diferenca(imagem1, imagem2).save("questao4/erosao/retangulo_buracos_diferenca.jpg")