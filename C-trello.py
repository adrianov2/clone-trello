import tkinter as tk
from tkinter import simpledialog, messagebox

# Função para criar um novo cartão
def add_card(column_frame):
    card_text = simpledialog.askstring("Novo Cartão", "Digite o título do cartão:")
    if card_text:
        card_frame = tk.Frame(column_frame, bg="#DFF6FF", padx=5, pady=5, relief="raised", bd=2)
        card_frame.pack(pady=5, fill="x")
        
        card_label = tk.Label(card_frame, text=card_text, bg="#DFF6FF", font=("Arial", 10), wraplength=150)
        card_label.pack(side="left", padx=5)
        
        delete_button = tk.Button(card_frame, text="X", bg="red", fg="white", font=("Arial", 8),
                                  command=lambda: card_frame.destroy())
        delete_button.pack(side="right", padx=5)
        
        # Permitir arrastar o cartão
        card_frame.bind("<Button-1>", lambda e: start_drag(e, card_frame))
        card_frame.bind("<B1-Motion>", lambda e: drag(e, card_frame))

# Funções para drag-and-drop
def start_drag(event, widget):
    widget.lift()
    widget.start_x = event.x
    widget.start_y = event.y

def drag(event, widget):
    x = widget.winfo_x() - widget.start_x + event.x
    y = widget.winfo_y() - widget.start_y + event.y
    widget.place(x=max(0, x), y=max(0, y))  # Restringe o movimento ao frame

# Criar a janela principal
root = tk.Tk()
root.title("Clone Trello")
root.geometry("900x500")
root.configure(bg="#F0F0F0")

# Criar as colunas
columns = ["Por Fazer", "Fazendo", "Concluído"]
frames = []

for i, col in enumerate(columns):
    frame = tk.Frame(root, bg="#F8F9FA", relief="sunken", bd=2)
    frame.place(relx=i * 0.33, rely=0, relwidth=0.33, relheight=1)
    
    # Adicionar título da coluna
    label = tk.Label(frame, text=col, bg="#007BFF", fg="white", font=("Arial", 14, "bold"))
    label.pack(fill="x", pady=5)
    
    # Botão para adicionar cartões
    add_button = tk.Button(frame, text="+ Adicionar Cartão", bg="#28A745", fg="white",
                           font=("Arial", 10, "bold"), command=lambda f=frame: add_card(f))
    add_button.pack(pady=5)
    
    frames.append(frame)

# Rodar o aplicativo
root.mainloop()
