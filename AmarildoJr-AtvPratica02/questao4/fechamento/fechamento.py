from PIL import Image

import sys
sys.path.insert(0, "questao3")
sys.path.insert(1, "questao4/dilatacao")
sys.path.insert(2, "questao4/erosao")
# from operacoes_morfologicas import diferenca


from dilatacao import dilatacao
from erosao import erosao

def fechamento(imagem, elemento_estruturante, centro):
    imagem_dilatada = dilatacao(imagem, elemento_estruturante, centro)
    imagem_saida = erosao(imagem_dilatada, elemento_estruturante, centro)
    return imagem_saida

if __name__ == "__main__":
    # 3x3
    elemento_est = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    centro = (1, 1)
    
    imagem = Image.open("questao4/retangulo_buracos.bmp").convert("L")

    imagem_saida = fechamento(imagem, elemento_est, centro)
    imagem_saida.save("questao4/fechamento/retangulo_buracos_fechamento_3x3.jpg")

    imagem1 = Image.open("questao4/retangulo_buracos.bmp").convert("L")
    # imagem2 = Image.open("questao4/fechamento/conectados_fechamento_3x3.jpg").convert("L")
    imagem2 = Image.open("questao4/fechamento/retangulo_buracos_fechamento_3x3.jpg").convert("L")
    # diferenca(imagem2, imagem1).save("questao4/fechamento/retangulo_buracos_diferenca.jpg")