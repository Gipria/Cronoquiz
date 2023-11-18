import tkinter as tk
from PIL import Image, ImageTk

# Função para verificar a resposta selecionada
def verificar_resposta(resposta_correta):
    resposta_selecionada = var_resposta.get()
    if resposta_selecionada == resposta_correta:
        avancar()

# Função para avançar para a próxima pergunta
def avancar():
    global index
    if index < len(perguntas) - 1:
        index += 1
        mostrar_pergunta()

# Função para mostrar a pergunta atual
def mostrar_pergunta():
    pergunta = perguntas[index]
    imagem_path = pergunta['imagem']
    img = Image.open(imagem_path)
    img = img.resize((largura_imagem, altura_imagem), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    canvas_imagem.create_image(0, 0, anchor="nw", image=img)
    canvas_imagem.image = img

    label_pergunta.config(text=pergunta['pergunta'])
    for i in range(len(botoes_resposta)):
        botoes_resposta[i].config(text=pergunta['respostas'][i], state="normal")

# Criação da janela principal
root = tk.Tk()
root.title("Jogo de Perguntas e Respostas")

# Obtenha a largura e a altura da tela do dispositivo
largura_janela = root.winfo_screenwidth()
altura_janela = root.winfo_screenheight()

# Defina a largura e altura da janela
root.geometry(f"{largura_janela}x{altura_janela}")

# Configure a janela para que não seja redimensionável
root.resizable(False, False)

# Defina a largura da área de imagem para 70% da largura da janela
largura_imagem = int(0.7 * largura_janela)
altura_imagem = altura_janela

# Crie um frame para as perguntas e respostas com um fundo colorido
frame_perguntas = tk.Frame(root, width=largura_janela - largura_imagem, height=altura_janela, background="lightblue")
frame_perguntas.pack(side="right", fill="both", expand=True)

# Definição das perguntas e respostas
perguntas = [
    {
        'imagem': 'imagem1.png',
        'pergunta': "1) A 'Carta de Pero Vaz de Caminha', escrita em 1500, é considerada como um dos documentos fundadores da Terra Brasilis e reflete, em seu texto, valores gerais da cultura renascentista, dentre os quais se destaca: a visão do índio como pertencente ao universo não religioso, tendo em conta sua antropofagia; a informação sobre os preconceitos desenvolvidos pelo renascimento no que tange à impossibilidade de se formar nos trópicos uma civilização católica e moderna; a identificação do Novo Mundo como uma área de insucesso devido à elevada temperatura que nada deixaria produzir; a observação da natureza e do homem do Novo Mundo como resultado da experiência da nova visão de homem, característica do século XV; a consideração da natureza e do homem como inferiores ao que foi projetado por Deus na Gênese",
        'respostas': ['a) a visão do índio como pertencente ao universo não religioso, tendo em conta sua antropofagia;',
                      'b) a informação sobre os preconceitos desenvolvidos pelo renascimento no que tange à impossibilidade de se formar nos trópicos uma civilização católica e moderna;',
                      'c) a identificação do Novo Mundo como uma área de insucesso devido à elevada temperatura que nada deixaria produzir;',
                      'd) a observação da natureza e do homem do Novo Mundo como resultado da experiência da nova visão de homem, característica do século XV;',
                      'e) a consideração da natureza e do homem como inferiores ao que foi projetado por Deus na Gênese'],
        'resposta_correta': 3,
    },
    {
        'imagem': 'imagem2.png',
        'pergunta': '2) Quanto é 5 + 5?',
        'respostas': ['1', '3', '10', '4'],
        'resposta_correta': 2,
    },
]

# Inicialização de variáveis
index = 0

# Crie um Canvas para a imagem
canvas_imagem = tk.Canvas(frame_perguntas, width=largura_imagem, height=altura_imagem)
canvas_imagem.pack(side="left")

# Crie um Frame para a imagem
frame_imagem = tk.Frame(frame_perguntas, width=largura_imagem, height=altura_imagem)
frame_imagem.pack(side="left")

# Carregue a imagem e redimensione
imagem_path = perguntas[index]['imagem']
img = Image.open(imagem_path)
img = img.resize((largura_imagem, altura_imagem), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

canvas_imagem.create_image(0, 0, anchor="nw", image=img)
canvas_imagem.image = img

# Crie um Frame para o texto à direita
frame_texto = tk.Frame(frame_perguntas, width=largura_janela - largura_imagem, height=altura_imagem)
frame_texto.pack(side="left")

# Label para a pergunta
label_pergunta = tk.Label(frame_texto, text=perguntas[index]['pergunta'], justify="left", anchor="w", wraplength=largura_janela - largura_imagem, font=("Helvetica", 12), bg="lightblue")
label_pergunta.pack()

# Variável para armazenar a resposta selecionada
var_resposta = tk.IntVar()

# Função para selecionar a resposta
def selecionar_resposta(i):
    var_resposta.set(i)

# Crie os botões de resposta como botões de seleção (Radiobutton) com efeitos de cor
botoes_resposta = []
for i in range(len(perguntas[index]['respostas'])):
    resposta = perguntas[index]['respostas'][i]
    radio_btn = tk.Radiobutton(
