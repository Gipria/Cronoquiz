import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Função para iniciar o jogo de perguntas 1
def iniciar_jogo_perguntas1():
    root.destroy()  # Fecha a janela de início
    import jogo_perguntas1  # Importa o módulo do jogo de perguntas 1
    jogo_perguntas1.iniciar_jogo()  # Inicia o jogo de perguntas 1

# Função para iniciar o jogo de perguntas 2
def iniciar_jogo_perguntas2():
    root.destroy()  # Fecha a janela de início
    import jogo_perguntas2  # Importa o módulo do jogo de perguntas 2
    jogo_perguntas2.iniciar_jogo()  # Inicia o jogo de perguntas 2

# Função para iniciar o jogo de perguntas 3
def iniciar_jogo_perguntas3():
    root.destroy()  # Fecha a janela de início
    import jogo_perguntas3  # Importa o módulo do jogo de perguntas 3
    jogo_perguntas3.iniciar_jogo()  # Inicia o jogo de perguntas 3

# Função para mover as imagens de fundo continuamente
def mover_imagens_fundo():
    global pos_x1, pos_x2
    pos_x1 -= velocidade_deslocamento  # Desloca a imagem 1 para a esquerda
    pos_x2 -= velocidade_deslocamento  # Desloca a imagem 2 para a esquerda
    if pos_x1 <= -largura_janela:
        pos_x1 = largura_janela  # Reinicia a posição quando a imagem 1 sair da janela
    if pos_x2 <= -largura_janela:
        pos_x2 = largura_janela  # Reinicia a posição quando a imagem 2 sair da janela
    canvas.coords(label_imagem_fundo1, pos_x1, 0)  # Atualiza a posição da imagem 1
    canvas.coords(label_imagem_fundo2, pos_x2, 0)  # Atualiza a posição da imagem 2
    root.after(10, mover_imagens_fundo)  # Chama a função novamente após um intervalo de tempo

# Criação da janela de início
root = tk.Tk()
root.title("Jogo de Perguntas e Respostas - Início")

# Define o tamanho da janela (largura x altura)
largura_janela = root.winfo_screenwidth()  # Largura igual à largura da tela
altura_janela = root.winfo_screenheight()  # Altura igual à altura da tela

# Use o método geometry para definir o tamanho da janela
root.geometry(f"{largura_janela}x{altura_janela}")

# Carregue a imagem de plano de fundo original
imagem_fundo_original = Image.open("background.png")

# Redimensione a imagem de fundo para o tamanho da janela
imagem_fundo_original = imagem_fundo_original.resize((largura_janela, altura_janela), Image.LANCZOS)

# Converta a imagem redimensionada para o formato do Tkinter
imagem_fundo = ImageTk.PhotoImage(imagem_fundo_original)

# Crie dois rótulos para as imagens de plano de fundo
canvas = tk.Canvas(root, width=largura_janela, height=altura_janela)
canvas.pack()
label_imagem_fundo1 = canvas.create_image(0, 0, image=imagem_fundo, anchor='nw')
label_imagem_fundo2 = canvas.create_image(largura_janela, 0, image=imagem_fundo, anchor='nw')

# Posições iniciais das imagens
pos_x1 = 0
pos_x2 = largura_janela

# Velocidade de deslocamento (ajuste conforme necessário)
velocidade_deslocamento = 1  # Aumente para um deslocamento mais rápido

# Inicie a função de movimento das imagens de fundo
mover_imagens_fundo()

# Estilo personalizado para os botões
style = ttk.Style()
style.configure("TButton",
    font=("Helvetica", 16),  # Tamanho da fonte médio
    background="#697a7a",
    relief="flat",  # Remove o efeito 3D
    width=20,  # Largura personalizada
    padding=(10, 5),  # Preenchimento personalizado
)
style.map("TButton",
    background=[("active", "white")],  # Substitua pela cor desejada
    foreground=[("active", "#7a6f69")]  # Cor do texto quando o botão estiver ativo
)

# Botões para iniciar os jogos
btn_jogo1 = ttk.Button(root, text="Jogo de Perguntas 1", command=iniciar_jogo_perguntas1, style="TButton")
btn_jogo2 = ttk.Button(root, text="Jogo de Perguntas 2", command=iniciar_jogo_perguntas2, style="TButton")
btn_jogo3 = ttk.Button(root, text="Jogo de Perguntas 3", command=iniciar_jogo_perguntas3, style="TButton")

# Centralize os botões verticalmente
btn_jogo1.place(relx=0.5, rely=0.4, anchor='center')
btn_jogo2.place(relx=0.5, rely=0.5, anchor='center')
btn_jogo3.place(relx=0.5, rely=0.6, anchor='center')

root.mainloop()
