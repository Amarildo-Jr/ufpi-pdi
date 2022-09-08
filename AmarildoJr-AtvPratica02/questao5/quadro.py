from PIL import Image

from funcoes_aux import *

def preencher_buracos(imagem, elemento_estruturante, centro):
    imagem_saida = fechamento(imagem, elemento_estruturante, centro)
    return imagem_saida

def separar_elementos_cor(imagem, cor):
    imagem_saida = Image.new("RGB", imagem.size, "white")
    pixels = imagem.load()

    for i in range(imagem.width):
        for j in range(imagem.height):
            if pixels[i, j] == cor:
                imagem_saida.putpixel((i, j), cor)

    return imagem_saida

def preencher_regioes(imagem, cor):
    imagem_saida = imagem.copy()

    pixels = imagem.load()
    
    for x in range(imagem.width):
        for y in range(imagem.height):
            buraco_dir = False
            buraco_esq = False
            buraco_cima = False
            buraco_baixo = False
            pixel_buraco = []
            if pixels[x, y] == cor:
                primeira_exe = True
                for i in range(x+1, imagem.width):
                    if pixels[i, y] != cor:
                        pass
                    else:
                        if primeira_exe:
                            break
                        else:
                            buraco_dir = True
                            pixel_buraco.append(i)
                            break
                    primeira_exe = False

                if buraco_dir:
                    primeira_exe = True
                    for j in range(y+1, imagem.height):
                        if pixels[x, j] != cor:
                            pass
                        else:
                            if primeira_exe:
                                break
                            else:
                                buraco_baixo = True
                                pixel_buraco.append(j)
                                break
                        primeira_exe = False

                if buraco_dir and buraco_baixo:
                    for i in range(x, pixel_buraco[0]):
                        for j in range(y, pixel_buraco[1]):
                            imagem_saida.putpixel((i, j), cor)
                pixel_buraco.clear()

    return imagem_saida
                

def letra_a(imagem):
    elemento_est = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    centro = (1, 1)

    elementos_separados = separar_elementos_cor(imagem, (0, 0, 0))
    # elementos_separados.save("questao5/elementos_pretos_separados.png")

    buracos_preenchidos = preencher_buracos(elementos_separados, elemento_est, centro)
    
    imagem_final = somar_imagens(imagem, buracos_preenchidos)

    return imagem_final

def letra_b(imagem):
    elemento_est = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    centro = (1, 1)

    elementos_separados = separar_elementos_cor(imagem, (0, 0, 0))
    return elementos_separados

def letra_c(imagem):

    elementos_verdes = separar_elementos_cor(imagem, (0, 255, 0))
    elementos_azuis = separar_elementos_cor(imagem, (0, 0, 255))
    elementos_amarelos = separar_elementos_cor(imagem, (255, 255, 0))

    amarelos_preenchidos = preencher_regioes(elementos_amarelos, (255, 255, 0))
    amarelos_preenchidos.show()


if __name__ == "__main__":

    imagem = Image.open("quadro.png").convert("RGB")

    letra_a(imagem).save("questao5/letra_a_obj_pretos_preenchidos.png")
    letra_b(imagem).save("questao5/letra_b_obj_pretos_separados.png")
    letra_c(imagem)
    