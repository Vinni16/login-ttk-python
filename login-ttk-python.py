import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

# ttkbootstrap é uma biblioteca dentro do TkInter, onde possui temas prontos.
# Aula https://www.youtube.com/watch?v=7xtYNBB17PY

app = ttk.Window("Formulário") # Nome da janela
app.geometry("550x500") # Tamanho padrão que a janela irá abrir
style = Style(theme="solar") # Tema que será usado da biblioteca Bootstrap
# https://ttkbootstrap.readthedocs.io/en/latest/#sample-themes

# eixo horizontal (x)
# eixo vertical (y)
# pad = padding, distância da borda,

label = ttk.Label(app, text="Formulário de Inscrição")
label.pack(pady=35)
label.config(font=("Arial", 20, "bold"))

nome = ttk.Frame(app)
nome.pack(pady=18, padx=10, fill="x")
ttk.Label(nome, text="Nome").pack(side=LEFT, padx=5) # Titulo do campo
ttk.Entry(nome).pack(side=LEFT, fill="x", expand=True, padx=5) # Campo de digitação

email = ttk.Frame(app)
email.pack(pady=18, padx=10, fill="x")
ttk.Label(email, text="Email").pack(side=LEFT, padx=5)
ttk.Entry(email).pack(side=LEFT, fill="x", expand=True, padx=5)

idade = ttk.Frame(app)
idade.pack(pady=18, padx=10, fill="x")
ttk.Label(idade, text="Idade").pack(side=LEFT, padx=5)
ttk.Entry(idade).pack(side=LEFT, fill="x", expand=True, padx=5)

checkbox = ttk.Frame(app)
checkbox.pack(pady=15, padx=10, fill="x")
ttk.Checkbutton(checkbox, bootstyle="round-toggle", text="Lembrar dados?").pack(side=LEFT, padx=15) # Não sei o padx certo!

botao = ttk.Frame(app)
botao.pack(pady=30, padx=10, fill="x")
ttk.Button(botao, bootstyle="SUCCESS", text="Enviar").pack(side=LEFT, padx=15)
ttk.Button(botao, bootstyle="DANGER", text="Cancelar").pack(side=LEFT, padx=15)



app.mainloop() # Mantém a janela do programa aberta