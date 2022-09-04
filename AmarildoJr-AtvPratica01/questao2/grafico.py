import matplotlib.pyplot as plt

def grafico(eixo_x, eixo_y, titulo, nome_arquivo):
    plt.bar(eixo_x, eixo_y, color="blue", width = 1)
    plt.xticks([0, 50, 100, 150, 200, 250])
    plt.ylabel("Quantidade de pixels")
    plt.xlabel("Intensidade")
    plt.title(titulo)
    plt.savefig('questao2/' + nome_arquivo, format='png')