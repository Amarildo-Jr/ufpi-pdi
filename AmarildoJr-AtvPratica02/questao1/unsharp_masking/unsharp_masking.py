from PIL import Image

def filtro_media(image):
    filtro = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    imagem_saida = Image.new("L", image.size)

    px = imagem_saida.load()

    for x in range(1, image.width - 1):
        for y in range(1, image.height - 1):
            sum = 0
            for i in range(3):
                for j in range(3):
                    sum += image.getpixel((x + i - 1, y + j - 1)) * filtro[i][j]
            px[x, y] = int (sum / 9)

    return imagem_saida

def unsharp_masking(image):
    imagem_suavizada = filtro_media(image)
    imagem_saida = Image.new("L", image.size)

    px = imagem_saida.load()

    for x in range(1, image.width - 1):
        for y in range(1, image.height - 1):
            g_mask = image.getpixel((x, y)) - imagem_suavizada.getpixel((x, y))
            px[x, y] = int(image.getpixel((x, y)) + g_mask)

    return imagem_saida

if __name__ == "__main__":
    image = Image.open("lena_gray.bmp")
    new_image = unsharp_masking(image)
    new_image.save("questao1/unsharp_masking/unsharp_masking.jpg")