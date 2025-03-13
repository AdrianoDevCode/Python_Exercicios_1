import tkinter as tk
from tkinter import messagebox

# Criar a janela principal
root = tk.Tk()
root.title("Lista de Compras")
root.geometry("400x500")
root.config(bg="#6a0dad")  # Fundo roxo

# Título
title_label = tk.Label(root, text="Lista de Compras", font=("Arial", 16, "bold"), bg="#6a0dad", fg="white")
title_label.pack(pady=10)

# Caixa de entrada para adicionar itens
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

# Lista para armazenar os itens
listbox = tk.Listbox(root, font=("Arial", 12), width=30, height=10, bg="#ffcc00")  # Fundo amarelo
listbox.pack(pady=10)

# Função para adicionar item
def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

# Função para remover item selecionado
def remove_item():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Erro", "Nenhum item selecionado!")

# Botões
btn_add = tk.Button(root, text="Adicionar", font=("Arial", 12), command=add_item, bg="white")
btn_add.pack(pady=5)

btn_remove = tk.Button(root, text="Remover", font=("Arial", 12), command=remove_item, bg="white")
btn_remove.pack(pady=5)

# Iniciar loop da interface
root.mainloop()
