import tkinter as tk
from PIL import Image, ImageTk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Tornar a janela em tela cheia

        self.image_frame = tk.Frame(root, width=0.8 * root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.image_frame.pack(side="left", fill="both", expand=True)
        self.qa_frame = tk.Frame(root, bg="white")
        self.qa_frame.pack(side="left", fill="both", expand=True)

        # Carregar a imagem
        image_path = "imagem1.png"  # Substitua "imagem1.png" pelo caminho da sua imagem
        self.image = Image.open(image_path)
        self.image = self.image.resize((10, 10), Image.ANTIALIAS)  # Redimensionar a imagem conforme necessário
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.image_frame, image=self.image)
        self.image_label.pack(side="left", fill="both", expand=True, padx=10)

        self.question_label = tk.Label(self.qa_frame, text="Pergunta vai aqui")
        self.question_label.pack(side="top", fill="both", expand=True)

        self.answers = ["Resposta 1", "Resposta 2", "Resposta 3", "Resposta 4"]
        self.buttons = []
        for i, answer in enumerate(self.answers):
            button = tk.Button(self.qa_frame, text=answer, command=lambda i=i: self.check_answer(i))
            button.pack(side="top", fill="both", expand=True)
            self.buttons.append(button)

        self.current_question = 0
        self.load_question(self.current_question)

        self.root.bind("<Configure>", self.handle_resize)

    def load_question(self, question_number):
        if question_number < 5:
            self.question_label.config(text=f"Pergunta {question_number + 1} vai aqui")
            for button in self.buttons:
                button.config(text="Resposta")
        else:
            self.image_label.config(text="Imagem cheia vai aqui (100%)")
            self.qa_frame.pack_forget()

    def handle_resize(self, event):
        # Atualizar o layout quando a janela é redimensionada
        self.root.update()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        # Modificar para 80% da largura
        self.image_label.config(width=window_width * 0.8)
        self.qa_frame.config(width=window_width * 0.2)

    def check_answer(self, answer_index):
        # Lógica para verificar a resposta correta
        # Se a resposta estiver correta, marque o botão como verde
        if self.current_question < 5:
            # Lógica de verificação de resposta correta
            self.buttons[self.current_question].config(bg="green")
            self.current_question += 1
            self.load_question(self.current_question)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
