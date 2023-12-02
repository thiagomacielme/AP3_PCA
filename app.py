import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz de Ciências - Reino Animal")
        self.score = 0
        self.question_number = 0
        self.questions = [
            {
                "pergunta": "Qual é o maior animal terrestre?",
                "opcoes": ["Elefante", "Girafa", "Rinoceronte", "Hipopótamo"],
                "resposta": "Elefante"
            },
            {
                "pergunta": "Quantas patas tem uma aranha?",
                "opcoes": ["6", "8", "10", "12"],
                "resposta": "8"
            },
            {
                "pergunta": "Qual é o único mamífero capaz de voar?",
                "opcoes": ["Morcego", "Pássaro", "Esquilo", "Abelha"],
                "resposta": "Morcego"
            },
            {
                "pergunta": "Onde os pinguins vivem?",
                "opcoes": ["Antártica", "África", "Austrália", "América do Sul"],
                "resposta": "Antártica"
            },
            {
                "pergunta": "Qual é o animal símbolo da Austrália?",
                "opcoes": ["Canguru", "Koala", "Tigre", "Elefante"],
                "resposta": "Canguru"
            },
            {
                "pergunta": "Qual é o réptil mais venenoso do mundo?",
                "opcoes": ["Cobra Coral", "Naja", "Taipan", "Crocodilo"],
                "resposta": "Taipan"
            },
            {
                "pergunta": "Quantos corações tem um polvo?",
                "opcoes": ["1", "2", "3", "4"],
                "resposta": "3"
            },
            {
                "pergunta": "Qual é o animal mais rápido do mundo?",
                "opcoes": ["Guepardo", "Águia", "Falcão", "Leopardo"],
                "resposta": "Guepardo"
            },
            {
                "pergunta": "Quais animais são conhecidos como os 'reis da selva'?",
                "opcoes": ["Tigres", "Leões", "Panteras", "Jaguares"],
                "resposta": "Leões"
            },
            {
                "pergunta": "Qual é o maior animal marinho?",
                "opcoes": ["Tubarão Branco", "Baleia Azul", "Orca", "Golfinho"],
                "resposta": "Baleia Azul"
            }
        ]
        
        self.label = tk.Label(root, text="")
        self.label.pack(pady=10)
        self.radio_var = tk.StringVar()
        
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value=str(i))
            self.radio_buttons.append(rb)
            rb.pack(pady=5)
        
        self.next_button = tk.Button(root, text="Próxima", command=self.next_question)
        self.next_button.pack(pady=10)
        
        self.load_question()

    def load_question(self):
        if self.question_number < len(self.questions):
            question_data = self.questions[self.question_number]
            self.label.config(text=question_data["pergunta"])
            for i in range(4):
                self.radio_buttons[i].config(text=question_data["opcoes"][i])
        else:
            self.show_result()

    def next_question(self):
        selected_option = self.radio_var.get()
        if selected_option == self.questions[self.question_number]["resposta"]:
            self.score += 1
        
        self.question_number += 1
        self.radio_var.set(-1)  # Limpa a seleção
        self.load_question()

    def show_result(self):
        messagebox.showinfo("Resultado", f"Sua pontuação: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()