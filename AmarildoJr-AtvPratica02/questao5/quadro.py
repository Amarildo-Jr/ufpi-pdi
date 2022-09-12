from PIL import Image

from funcoes_aux import *

def preencher_buracos(imagem, elemento_estruturante, centro):
    imagem_saida = fechamento(imagem, elemento_estruturante, centro)
    return imagem_saida

def separar_elementos_cor(imagem, cor):
    imagem_saida = Image.new("RGB", imagem.size, "white")
    pixels = imagem.load()

    for x in range(imagem.width):
        for y in range(imagem.height):
            if pixels[x, y] == cor:
                imagem_saida.putpixel((x, y), cor)

    return imagem_saida

def remover_elementos_cor(imagem, cor):
    imagem_saida = Image.new("RGB", imagem.size, "white")
    pixels = imagem.load()

    for x in range(imagem.width):
        for y in range(imagem.height):
            if pixels[x, y] != cor:
                imagem_saida.putpixel((x, y), pixels[x, y])

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
                    if pixels[i, y] == cor:
                        if primeira_exe:
                            primeira_exe = False
                            continue
                        else:
                            buraco_dir = True
                            pixel_buraco.append(i)
                            break

                if buraco_dir:
                    primeira_exe = True
                    for j in range(y+1, imagem.height):
                        if pixels[i, y] == cor:
                            if primeira_exe:
                                primeira_exe = False
                                continue
                            else:
                                buraco_baixo = True
                                pixel_buraco.append(j)
                                break

                if buraco_dir and buraco_baixo:
                    
                    primeira_exe = True
                    for j in range(y-1, 0, -1):
                        if pixels[i, y] == cor:
                            if primeira_exe:
                                primeira_exe = False
                                continue
                            else:
                                buraco_cima = True
                                pixel_buraco.append(j)
                                break

                if buraco_dir and buraco_baixo and buraco_cima:

                    primeira_exe = True
                    for i in range(x-1, 0, -1):
                        if pixels[i, y] == cor:
                            if primeira_exe:
                                primeira_exe = False
                                continue
                            else:
                                buraco_esq = True
                                pixel_buraco.append(i)
                                break
                        primeira_exe = False
                
            if buraco_dir and buraco_baixo and buraco_esq and buraco_cima:
                for i in range(pixel_buraco[3], pixel_buraco[0]):
                    for j in range(pixel_buraco[2], pixel_buraco[1]):
                        imagem_saida.putpixel((i, j), cor)
            pixel_buraco.clear()

    return imagem_saida

def imagem_fronteira(im, adjacencia, cor):
    im = im.convert("RGB")
    im_saida = Image.new(mode = "RGB", size = (im.width, im.height), color = (255, 255, 255))

    nome_arquivo = f"fronteira-adj{adjacencia}.png"

    px = im.load()
    for i in range(0, im.height):
        for j in range(0, im.width):
            if px[i, j] == cor:
                if px[i, j + 1] == (255, 255, 255) or px[i, j - 1] == (255, 255, 255) or px[i + 1, j] == (255, 255, 255) or px[i - 1, j] == (255, 255, 255):
                    im_saida.putpixel((i, j), cor)
                    # im_saida.putpixel((i, j), (255, 255, 255, 255))
                elif adjacencia == 8:
                        if px[i + 1, j + 1] == (255, 255, 255) or px[i - 1, j - 1] == (255, 255, 255) or px[i + 1, j - 1] == (255, 255, 255) or px[i - 1, j + 1] == (255, 255, 255):
                            im_saida.putpixel((i, j), cor)
                            # im_saida.putpixel((i, j), (255, 255, 255, 255))
    # im_saida.save(f"questao5/{nome_arquivo}")
    return im_saida

def fronteira(imagem):
    elemento_est = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    centro = (2, 2)

    imagem_saida = erosao(imagem, elemento_est, centro)
    imagem_saida = diferenca(imagem, imagem_saida)

    return imagem_saida


def letra_a(imagem):
    elemento_est = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    centro = (2, 2)

    elementos_separados = separar_elementos_cor(imagem, (0, 0, 0))
    # elementos_separados.save("questao5/elementos_pretos_separados.png")

    buracos_preenchidos = preencher_buracos(elementos_separados, elemento_est, centro)
    
    imagem_final = somar_imagens(imagem, buracos_preenchidos)

    return imagem_final

def letra_b(imagem):
    elementos_separados = remover_elementos_cor(imagem, (0, 0, 0))
    return elementos_separados

def letra_c(imagem):
    imagem = imagem.convert("RGB")

    # # preenchendo buracos verdes
    elementos_verdes = separar_elementos_cor(imagem, (0, 255, 0))
    verdes_preenchidos = preencher_regioes(elementos_verdes, (0, 255, 0))
    # verdes_preenchidos.show()


    elementos_azuis = separar_elementos_cor(imagem, (0, 0, 255))
    azuis_preenchidos = preencher_regioes(elementos_azuis, (0, 0, 255))
    # azuis_preenchidos.show()


    elementos_amarelos = separar_elementos_cor(imagem, (255, 255, 0))
    amarelos_preenchidos = preencher_regioes(elementos_amarelos, (255, 255, 0))
    # amarelos_preenchidos.show()
    
    soma = somar_imagens(imagem, azuis_preenchidos)
    soma = somar_imagens(soma, amarelos_preenchidos)
    soma = somar_imagens(soma, verdes_preenchidos)
    
    return soma



if __name__ == "__main__":

    imagem = Image.open("quadro.png").convert("RGB")

    # letra_a(imagem).save("questao5/letra_a_obj_pretos_preenchidos.png")
    # letra_b(imagem).save("questao5/letra_b_obj_pretos_removidos.png")
    letra_c(imagem).save("questao5/letra_c_obj_preenchidos.png")
    