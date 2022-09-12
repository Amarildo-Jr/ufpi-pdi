from PIL import Image

def filtro_media(imagem, mascara):
    n = 0

    for mascara_i in range(len(mascara)):
        for mascara_j in range(len(mascara[0])):
            n += mascara[mascara_i][mascara_j] 

    imagem_saida = Image.new("L", imagem.size)

    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            sum = 0
            for i in range(3):
                for j in range(3):
                    sum += imagem.getpixel((x + i - 1, y + j - 1)) * mascara[i][j]
            imagem_saida.putpixel((x, y), int (sum / 9))

    return imagem_saida

def mediana(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        return (lista[len(lista) // 2] + lista[len(lista) // 2 - 1]) / 2
    else:
        return lista[len(lista) // 2]

def filtro_mediana(imagem):
    imagem_saida = Image.new("L", imagem.size)
    
    px = imagem.load()

    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            lista = []
            for i in range(3):
                for j in range(3):
                    lista.append(px[x + i - 1, y + j - 1])
            imagem_saida.putpixel((x, y), mediana(lista))
    
    return imagem_saida


if __name__ == "__main__":
    imagem = Image.open("lena_ruido.bmp")

    mascara = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    # mascara = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # mascara = [[1, 3, 1], [3, 16, 3], [1, 3, 1]]
    # mascara = [[0, 1, 0], [1, 4, 1], [0, 1, 0]]

    imagem_media = filtro_media(imagem, mascara)
    imagem_media.save("questao2/media-5.jpg")

    # imagem_suavizada = Image.open("questao2/media-32.jpg")
    # imagem_mediana = filtro_media(imagem_suavizada, mascara)
    # imagem_mediana.save("questao2/media-32-2x.jpg")
