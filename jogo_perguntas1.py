import tkinter as tk
from tkinter import PhotoImage, messagebox
from PIL import Image, ImageTk


# Função para verificar a resposta selecionada
def verificar_resposta(resposta_correta):
    resposta_selecionada = var_resposta.get()
    if resposta_selecionada == resposta_correta:
        avancar()
    else:
        exibir_mensagem_erro()


# Função para exibir uma mensagem de erro
def exibir_mensagem_erro():
    feedback_label.config(text="Resposta incorreta. Tente novamente.", fg="red")
    root.after(1000, limpar_mensagem_erro)


# Função para limpar a mensagem de erro
def limpar_mensagem_erro():
    feedback_label.config(text="")


# Função para avançar para a próxima pergunta ou mostrar botões de Sair/Salvar
def avancar():
    global index
    if index < len(perguntas) - 1:
        index += 1
        mostrar_pergunta()
    else:
        mostrar_ultima_imagem()


# Função para mostrar a última imagem
def mostrar_ultima_imagem():
    pergunta = perguntas[index]
    imagem_path = pergunta.get('imagem', 'images/imagem_padrao.png')
    img = Image.open(imagem_path)

    try:
        img = img.resize((largura_imagem, altura_imagem), resample=Image.ANTIALIAS)
    except AttributeError:
        try:
            img = img.resize((largura_imagem, altura_imagem), Image.ANTIALIAS)
        except:
            img = img.resize((largura_imagem, altura_imagem))

    img = ImageTk.PhotoImage(img)

    canvas_imagem.create_image(0, 0, anchor="nw", image=img)
    canvas_imagem.image = img

    # Ocultar frame de perguntas
    frame_perguntas.pack_forget()

    # Mostrar botão "Voltar à Página Anterior"
    btn_voltar.pack(side="top", pady=10)


# Função para voltar à página anterior
def voltar_pagina_anterior():
    global index
    # Mostrar frame de perguntas
    frame_perguntas.pack(side="right", fill="both", expand=True)
    btn_voltar.pack_forget()
    # Voltar à página anterior
    index -= 1
    mostrar_pergunta()


# Função para mostrar a pergunta atual
def mostrar_pergunta():
    if index < len(perguntas):
        pergunta = perguntas[index]
        imagem_path = pergunta['imagem']
        img = Image.open(imagem_path)

        try:
            img = img.resize((largura_imagem, altura_imagem), resample=Image.ANTIALIAS)
        except AttributeError:
            try:
                img = img.resize((largura_imagem, altura_imagem), Image.ANTIALIAS)
            except:
                img = img.resize((largura_imagem, altura_imagem))

        img = ImageTk.PhotoImage(img)

        canvas_imagem.create_image(0, 0, anchor="nw", image=img)
        canvas_imagem.image = img

        label_pergunta.config(text=pergunta['pergunta'])
        for i, resposta in enumerate(pergunta['respostas']):
            botoes_resposta[i].config(text=resposta, value=i)
    else:
        mostrar_ultima_imagem()


# Função para sair do jogo
def sair_do_jogo():
    root.destroy()


# Função para salvar o jogo (a ser implementada)
def salvar_jogo():
    # Implemente a lógica de salvar o jogo aqui
    pass


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
largura_imagem = int(0.75 * largura_janela)
altura_imagem = altura_janela

# Crie um frame para as perguntas e respostas com um fundo colorido
frame_perguntas = tk.Frame(root, width=largura_janela - largura_imagem, height=altura_janela, background="lightblue")
frame_perguntas.pack(side="right", fill="both", expand=True)

# Definição das perguntas e respostas
perguntas = [
    {
        'imagem': 'images/imagem1.png',
        'pergunta': "1) A 'Carta de Pero Vaz de Caminha', escrita em 1500, é considerada como um dos documentos fundadores da Terra Brasilis e reflete, em seu texto, valores gerais da cultura renascentista, dentre os quais se destaca: a visão do índio como pertencente ao universo não religioso, tendo em conta sua antropofagia; a informação sobre os preconceitos desenvolvidos pelo renascimento no que tange à impossibilidade de se formar nos trópicos uma civilização católica e moderna; a identificação do Novo Mundo como uma área de insucesso devido à elevada temperatura que nada deixaria produzir; a observação da natureza e do homem do Novo Mundo como resultado da experiência da nova visão de homem, característica do século XV; a consideração da natureza e do homem como inferiores ao que foi projetado por Deus na Gênese",
        'respostas': [
            'a) a visão do índio como pertencente ao universo não religioso, tendo em conta sua antropofagia;',
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
        'pergunta': "3)  A primeira capital do Brasil foi:                                                                   ",
        'respostas': [
            'a) São Paulo',
            'b) Rio de Janeiro',
            'c) Salvador',
            'd) São Luís',
            'e) Brasília'],
        'resposta_correta': 2,
    },
    {
        'imagem': 'images/imagem4.png',
        'pergunta': "4) O descobrimento do Brasil foi parte do plano imperial da Coroa Portuguesa, no século XV. Embora não houvesse interesse específico de expansão para o Ocidente…",
        'respostas': [
            'a) a posse de terras no Atlântico ocidental consolidava a hegemonia portuguesa neste Oceano',
            'b) o Brasil era uma alternativa mercantil ao comércio português no Oriente.',
            'c) o desvio da esquadra de Cabral seguia a mesma inspiração de Colombo para chegar às Índias.',
            'd) a procura de terras no Ocidente foi uma reação de Portugal ao Tratado de Tordesilhas, que o afastava da América.',
            'e) essa descoberta foi mero acaso, provocado pelas intempéries que desviaram a esquadra da rota da Índia.'],
        'resposta_correta': 0,
    },
    {
        'imagem': 'images/imagem5.png',
        'pergunta': "5) Qual foi a principal região do território brasileiro que os portugueses exploraram na fase Pré-colonial?",
        'respostas': [
            'a) A região da Floresta Amazônica, que possuía muitos animais selvagens.',
            'b) A região do Centro-oeste brasileiro, que possuía muitas minas de ouro.',
            'c) A região Sul do Brasil, pois não havia povos indígenas.',
            'd) A faixa litorânea, principalmente do Nordeste e Sudeste do Brasil, que possuía muito pau-brasil.',
            'e) Nenhuma das anteriores'],
        'resposta_correta': 3,
    },
    {
        'imagem': 'images/imagem6.png',

    }
]

# Inicialização de variáveis
index = 0

# Crie um Canvas para a imagem
canvas_imagem = tk.Canvas(root, width=largura_imagem, height=altura_imagem)
canvas_imagem.pack(side="left", fill="both", expand=True)

# Label para a pergunta
label_pergunta = tk.Label(frame_perguntas, text=perguntas[index]['pergunta'], justify="left", anchor="w",
                          wraplength=largura_janela - largura_imagem, font=("Helvetica", 12), bg="lightblue")
label_pergunta.pack()

# Variável para armazenar a resposta selecionada
var_resposta = tk.IntVar()

# Botões de resposta
botoes_resposta = []
for i, resposta in enumerate(perguntas[index]['respostas']):
    btn = tk.Radiobutton(frame_perguntas, text=resposta, variable=var_resposta, value=i, justify="left", anchor="w",
                         wraplength=largura_janela - largura_imagem, font=("Helvetica", 12), bg="lightblue")
    btn.pack(anchor="w", padx=10, pady=5)
    botoes_resposta.append(btn)

# Label para feedback
feedback_label = tk.Label(frame_perguntas, text="", justify="left", anchor="w",
                          wraplength=largura_janela - largura_imagem, font=("Helvetica", 12), bg="lightblue", fg="red")
feedback_label.pack()

# Botão para verificar a resposta
btn_verificar = tk.Button(frame_perguntas, text="Verificar Resposta",
                          command=lambda: verificar_resposta(perguntas[index]['resposta_correta']))
btn_verificar.pack(side="top", pady=10)

# Botão para avançar para a próxima imagem
btn_avancar = tk.Button(frame_perguntas, text="Avançar para a Próxima Imagem", command=avancar)

# Botões para Sair e Salvar
btn_sair = tk.Button(frame_perguntas, text="Sair", command=sair_do_jogo)
btn_salvar = tk.Button(frame_perguntas, text="Salvar", command=salvar_jogo)

# Botão para voltar à página anterior
btn_voltar = tk.Button(frame_perguntas, text="Voltar à Página Anterior", command=voltar_pagina_anterior)

# Inicialização da primeira pergunta
mostrar_pergunta()

# Execute o loop da interface
root.mainloop()
