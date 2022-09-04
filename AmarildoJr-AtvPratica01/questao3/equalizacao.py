from PIL import Image, ImageChops
import sys

sys.path.insert(0, "questao2")
sys.path.insert(1, "questao3")

from histograma_acumulado import histograma_acumulado

def equalizar(imagem):
    im = Image.open(imagem)
    h_equalizado = histograma_acumulado(imagem)
    pixels = im.width * im.height
    for i in range(0, len(h_equalizado)):
        h_equalizado[i] = round(h_equalizado[i] / pixels * 255)
    return h_equalizado

def mostrar_imagem(imagem, histograma, titulo):
    im = Image.open(imagem)
    im_saida = Image.new(mode = "L", size = im.size)
    for i in range (im.size[0]):
        for j in range (im.size[1]):
            im_saida.putpixel((i, j), histograma[im.getpixel((i, j))])
    im_saida.save(f"questao3/equalizacao-{titulo}")

if  __name__ == "__main__":
    lena_gray = "lena_gray.bmp"
    image1 = "image1.png"

    lena_gray_eq = "questao3/equalizacao-lena_gray.bmp"
    image1_eq = "questao3/equalizacao-image1.png"

    mostrar_imagem(lena_gray, equalizar(lena_gray), lena_gray)
    mostrar_imagem(image1, equalizar(image1), image1)

    mostrar_imagem(lena_gray_eq, equalizar(lena_gray_eq), "eq2_lena_gray.bmp")
    mostrar_imagem(image1_eq, equalizar(image1_eq), "eq2_image1.png")

    # Subtraindo a imagem equalizada com a imagem que foi equalizada 2x
    diferenca_lg = ImageChops.subtract (Image.open(lena_gray_eq), Image.open("questao3/equalizacao-eq2_lena_gray.bmp"))
    diferenca_lg.save("questao3/diferenca-eq-lena_gray.bmp")

    # Subtraindo a imagem 2x equalizada com a imagem que foi equalizada
    diferenca_lg = ImageChops.subtract (Image.open("questao3/equalizacao-eq2_lena_gray.bmp"), Image.open(lena_gray_eq))
    diferenca_lg.save("questao3/diferenca-eq2-lena_gray.bmp")

    # Subtraindo a imagem equalizada com a imagem que foi equalizada 2x
    diferenca_image1 = ImageChops.subtract (Image.open(image1_eq), Image.open("questao3/equalizacao-eq2_image1.png"))
    diferenca_image1.save("questao3/diferenca-eq-image1.png")

    # Subtraindo a imagem 2x equalizada com a imagem que foi equalizada
    diferenca_image1 = ImageChops.subtract (Image.open("questao3/equalizacao-eq2_image1.png"), Image.open(image1_eq), )
    diferenca_image1.save("questao3/diferenca-eq2-image1.png")
