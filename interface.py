import tkinter as tk
from automacao import preencher_formulario

def iniciar_automacao():
    numero_pedido = entrada_pedido.get()
    nome_cliente = entrada_cliente.get()

    # Verifica se ambos os campos estão vazios
    if numero_pedido.strip() and nome_cliente.strip():
        valor_digitado = f"{numero_pedido} - {nome_cliente}"
        preencher_formulario(valor_digitado)
    else:
        print("Erro: Nenhum valor digitado!")

def limpar_campos():
    entrada_pedido.delete(0, tk.END) # Limpa o campo pedido
    entrada_cliente.delete(0, tk.END) # Limpa o campo nome
    
    
# Criar janela interface gráfica
janela = tk.Tk()
janela.title("ZAP compras")

# Configurar altura e largura da janela
janela.geometry("600x300")

# Adicionar um título
titulo = tk.Label(janela, text="ITEM: CARTÃO DE VISITA VERNIZ LOCAL 500UND")
titulo.pack(pady=10)

# Número do pedido
tk.Label(janela, text="Número do pedido: ").pack()
entrada_pedido = tk.Entry(janela, font=("Arial", 12), width=30)
entrada_pedido.pack(pady=5)

# Nome do cliente
tk.Label(janela, text="Nome do cliente: ").pack()
entrada_cliente = tk.Entry(janela, font=("Arial", 12), width=20)
entrada_cliente.pack(pady=5)

# Botão para iniciar
botao = tk.Button(janela, text="Adicionar ao carrinho", command=iniciar_automacao)
botao.pack(pady=5)

# Botão para limpar os campos
botao_limpar = tk.Button(janela, text="Limpar", font=("Arial", 12), command=limpar_campos)
botao_limpar.pack(pady=5)

# Iniciar interface gráfica
janela.mainloop()