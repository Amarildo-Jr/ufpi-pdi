from PIL import Image
from grafico import grafico

def histograma(imagem):
    histograma = [0] * 256
    im = Image.open(imagem)
    px = im.load()
    for i in range(0, im.height):
        for j in range(0, im.width):
            histograma[px[i, j]] += 1
    return histograma

if __name__ == "__main__":

    h = histograma("lena_gray.bmp")

    intensidades = []
    for i in range (0, len(h)):
        intensidades.append(i)

    grafico(intensidades, h, "Histograma \"lena_gray.png\"", 'histograma-lena_gray.png')