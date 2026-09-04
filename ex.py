import tkinter as tk
from random import randint

def sortear():
    numeros = tuple(randint(1, 10) for _ in range(5))
    
    lbl_numeros.config(text="  ".join(str(n) for n in numeros))
    lbl_maior.config(text=f"Maior valor sorteado: {max(numeros)}")
    lbl_menor.config(text=f"Menor valor sorteado: {min(numeros)}")

app = tk.Tk()
app.title("Exercício 074 - Sorteio em Tupla")
app.geometry("420x320")
app.configure(bg="#f8fafc")
app.resizable(False, False)

lbl_titulo = tk.Label(
    app, 
    text="🎲 Sorteador de Números", 
    font=("Helvetica", 16, "bold"),
    bg="#f8fafc",
    fg="#0f172a"
)
lbl_titulo.pack(pady=(20, 10))

btn_sortear = tk.Button(
    app,
    text="Sortear 5 Números",
    font=("Helvetica", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    padx=15,
    pady=8,
    relief="flat",
    cursor="hand2",
    command=sortear
)
btn_sortear.pack(pady=10)

frame_card = tk.Frame(
    app, 
    bg="#ffffff", 
    bd=1, 
    relief="solid", 
    highlightthickness=0
)
frame_card.pack(pady=10, padx=30, fill="both", expand=True)

lbl_subtitulo = tk.Label(
    frame_card,
    text="Valores sorteados na tupla:",
    font=("Helvetica", 9),
    bg="#ffffff",
    fg="#64748b"
)
lbl_subtitulo.pack(pady=(12, 2))

lbl_numeros = tk.Label(
    frame_card,
    text="-  -  -  -  -",
    font=("Helvetica", 22, "bold"),
    bg="#ffffff",
    fg="#1e293b"
)
lbl_numeros.pack(pady=5)

lbl_maior = tk.Label(
    frame_card,
    text="Maior valor sorteado: -",
    font=("Helvetica", 10, "bold"),
    bg="#ffffff",
    fg="#16a34a"
)
lbl_maior.pack(anchor="w", padx=20, pady=(10, 2))

lbl_menor = tk.Label(
    frame_card,
    text="Menor valor sorteado: -",
    font=("Helvetica", 10, "bold"),
    bg="#ffffff",
    fg="#dc2626"
)
lbl_menor.pack(anchor="w", padx=20, pady=(0, 12))

app.mainloop()