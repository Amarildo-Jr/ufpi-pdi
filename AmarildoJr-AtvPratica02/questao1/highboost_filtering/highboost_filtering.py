from PIL import Image

def filtro_media(imagem):
    filtro = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    imagem_saida = Image.new("L", imagem.size)

    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            sum = 0
            for i in range(3):
                for j in range(3):
                    sum += imagem.getpixel((x + i - 1, y + j - 1)) * filtro[i][j]
            imagem_saida.putpixel((x, y), int (sum / 9))

    return imagem_saida

def highboost_filtering(imagem, k):
    
    filtro = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    imagem_suavizada = filtro_media(imagem, filtro)
    imagem_saida = Image.new("L", imagem.size)

    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            mascara_g = imagem.getpixel((x, y)) - imagem_suavizada.getpixel((x, y))
            imagem_saida.putpixel((x, y), int(imagem.getpixel((x, y)) + mascara_g * k))

    return imagem_saida

if __name__ == "__main__":
    
    imagem = Image.open("lena_gray.bmp")
    imagem_saida = highboost_filtering(imagem, 2)
    imagem_saida.save("questao1/highboost_filtering/highboost_filtering_k0.jpg")