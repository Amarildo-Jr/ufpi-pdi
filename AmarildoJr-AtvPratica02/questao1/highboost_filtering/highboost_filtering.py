from PIL import Image

def filtro_media(image, filtro):
    n = 0

    for filtro_i in range(len(filtro)):
        for filtro_j in range(len(filtro[0])):
            n += filtro[filtro_i][filtro_j] 

    imagem_saida = Image.new("L", image.size)

    px = imagem_saida.load()

    for x in range(1, image.width - 1):
        for y in range(1, image.height - 1):
            sum = 0
            for i in range(3):
                for j in range(3):
                    sum += image.getpixel((x + i - 1, y + j - 1)) * filtro[i][j]
            px[x, y] = int (sum / n)

    return imagem_saida

def highboost_filtering(image, k):
    
    filtro = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    imagem_suavizada = filtro_media(image, filtro)
    imagem_saida = Image.new("L", image.size)

    px = imagem_saida.load()

    for x in range(1, image.width - 1):
        for y in range(1, image.height - 1):
            g_mask = image.getpixel((x, y)) - imagem_suavizada.getpixel((x, y))
            px[x, y] = int(image.getpixel((x, y)) + g_mask * k)

    return imagem_saida

if __name__ == "__main__":
    
    image = Image.open("lena_gray.bmp")
    new_image = highboost_filtering(image, 2)
    new_image.save("questao1/highboost_filtering/highboost_filtering_k0.jpg")