from PIL import Image

def filtro_prewitt(image):
    imagem_saida = Image.new("L", image.size)

    px = imagem_saida.load()
    
    return imagem_saida

if __name__ == "__main__":
    image = Image.open("lena_gray.bmp")
    new_image = filtro_prewitt(image)
    new_image.save("questao1/bordas/prewitt.jpg")