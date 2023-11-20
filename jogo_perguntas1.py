import tkinter as tk
from tkinter import PhotoImage
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

    try:
        # Se a versão do Pillow for 8.0.0 ou superior
        img = img.resize((largura_imagem, altura_imagem), resample=Image.ANTIALIAS)
    except AttributeError:
        # Se a versão do Pillow for anterior a 8.0.0
        try:
            img = img.resize((largura_imagem, altura_imagem), Image.ANTIALIAS)
        except:
            # Caso a exceção ocorra, tente com um método de redimensionamento padrão
            img = img.resize((largura_imagem, altura_imagem))

    img = ImageTk.PhotoImage(img)

    canvas_imagem.create_image(0, 0, anchor="nw", image=img)
    canvas_imagem.image = img

    label_pergunta.config(text=pergunta['pergunta'])
    for i, resposta in enumerate(pergunta['respostas']):
        botoes_resposta[i].config(text=resposta, value=i)

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
        'imagem': 'images/imagem1.png',
        'pergunta': "1) A 'Carta de Pero Vaz de Caminha', escrita em 1500, é considerada como um dos documentos fundadores da Terra Brasilis e reflete, em seu texto, valores gerais da cultura renascentista, dentre os quais se destaca: a visão do índio como pertencente ao universo não religioso, tendo em conta sua antropofagia; a informação sobre os preconceitos desenvolvidos pelo renascimento no que tange à impossibilidade de se formar nos trópicos uma civilização católica e moderna; a identificação do Novo Mundo como uma área de insucesso devido à elevada temperatura que nada deixaria produzir; a observação da natureza e do homem do Novo Mundo como resultado da experiência da nova visão de homem, característica do século XV; a consideração da natureza e do homem como inferiores ao que foi projetado por Deus na Gênese",
        'respostas': ['a) a visão do índio como pertencente ao universo não religioso, tendo em conta sua antropofagia;',
                      'b) a informação sobre os preconceitos desenvolvidos pelo renascimento no que tange à impossibilidade de se formar nos trópicos uma civilização católica e moderna;',
                      'c) a identificação do Novo Mundo como uma área de insucesso devido à elevada temperatura que nada deixaria produzir;',
                      'd) a observação da natureza e do homem do Novo Mundo como resultado da experiência da nova visão de homem, característica do século XV;',
                      'e) a consideração da natureza e do homem como inferiores ao que foi projetado por Deus na Gênese'],
        'resposta_correta': 3,
    },
    {
        'imagem': 'images/imagem2.png',
        'pergunta': "2) Enquanto os portugueses escutavam a missa com muito 'prazer e devoção', a praia encheu-se de nativos. Eles sentavam-se lá surpresos com a complexidade do ritual que observavam ao longe. Quando D. Henrique acabou a pregação, os indígenas se ergueram e começaram a soprar conchas e buzinas, saltando e dançando (…) Náufragos Degredados e Traficantes (Eduardo Bueno). Este contato amistoso entre brancos e índios era preservado:",
        'respostas': [
            'a) pela Igreja, que sempre respeitou a cultura indígena no decurso da catequese.',
            'b) até o início da colonização quando o índio, vitimado por doenças, escravidão e extermínio, passou a ser descrito como sendo selvagem, indolente e canibal.',
            'c) pelos colonos que escravizaram somente o africano na atividade produtiva de exportação.',
            'd) em todos os períodos da História Colonial Brasileira, passando a figura do índio para o imaginário social como "o bom selvagem e forte colaborador da colonização".',
            'e) sobretudo pelo governo colonial, que tomou várias medidas para impedir o genocídio e a escravidão.'],
        'resposta_correta': 1,
    },
    {
        'imagem': 'images/imagem3.png',
        'pergunta': "2) Enquanto os portugueses escutavam a missa com muito 'prazer e devoção', a praia encheu-se de nativos. Eles sentavam-se lá surpresos com a complexidade do ritual que observavam ao longe. Quando D. Henrique acabou a pregação, os indígenas se ergueram e começaram a soprar conchas e buzinas, saltando e dançando (…) Náufragos Degredados e Traficantes (Eduardo Bueno). Este contato amistoso entre brancos e índios era preservado:",
        'respostas': [
            'a) pela Igreja, que sempre respeitou a cultura indígena no decurso da catequese.',
            'b) até o início da colonização quando o índio, vitimado por doenças, escravidão e extermínio, passou a ser descrito como sendo selvagem, indolente e canibal.',
            'c) pelos colonos que escravizaram somente o africano na atividade produtiva de exportação.',
            'd) em todos os períodos da História Colonial Brasileira, passando a figura do índio para o imaginário social como "o bom selvagem e forte colaborador da colonização".',
            'e) sobretudo pelo governo colonial, que tomou várias medidas para impedir o genocídio e a escravidão.'],
        'resposta_correta': 2,
    }
]

# Inicialização de variáveis
index = 0

# Crie um Canvas para a imagem
canvas_imagem = tk.Canvas(root, width=largura_imagem, height=altura_imagem)
canvas_imagem.pack(side="left", fill="both", expand=True)

# Label para a pergunta
label_pergunta = tk.Label(frame_perguntas, text=perguntas[index]['pergunta'], justify="left", anchor="w", wraplength=largura_janela - largura_imagem, font=("Helvetica", 12), bg="lightblue")
label_pergunta.pack()

# Variável para armazenar a resposta selecionada
var_resposta = tk.IntVar()

# Botões de resposta
botoes_resposta = []
for i, resposta in enumerate(perguntas[index]['respostas']):
    btn = tk.Radiobutton(frame_perguntas, text=resposta, variable=var_resposta, value=i, justify="left", anchor="w", wraplength=largura_janela - largura_imagem, font=("Helvetica", 12), bg="lightblue")
    btn.pack(anchor="w", padx=10, pady=5)
    botoes_resposta.append(btn)

# Botão para verificar a resposta
btn_verificar = tk.Button(frame_perguntas, text="Verificar Resposta", command=lambda: verificar_resposta(perguntas[index]['resposta_correta']))
btn_verificar.pack()

# Inicialização da primeira pergunta
mostrar_pergunta()

# Execute o loop da interface
root.mainloop()