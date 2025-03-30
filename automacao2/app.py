from pywinauto.application import Application
from pywinauto.keyboard import send_keys 
from pywinauto.mouse import click
from time import sleep
import os 
#  - Passos manuais para realizar esse processo

# 1 - Abrir aplicação
app  = Application().start(r'C:\Users\User\Desktop\sistema_produtos\app.exe')
sleep(2)

# 2 - Encontrar janela
window = app.window(title='Login') 


# 3 - Interagir com os campos
# identifica os campos disponíveis na aplicação
# window.print_control_identifiers()

window.set_focus()
# Campo usuário
send_keys("jhonatan{TAB}")
# Campo senha
send_keys("123456")

# Entrando no sistema 
botao_x, botao_y = 867,599
click(coords=(botao_x, botao_y))

sleep(2)

# Verifica se o arquivo produtos.txt existe
caminho_arquivo = "produtos.txt"

if not os.path.exists(caminho_arquivo):
    print("arquivo produtos.txt não encontrado00")

else:
    # Abrindo bloco de notas 
    with open('produtos.txt', 'r') as file:
        for linha in file:
            dados = linha.strip().split(',')

            if len(dados) != 3:
                print(f"Erro ao ler linha {linha}")
                continue
            
            produto, quantidade, preco = dados 
            
            window = app.window(title="Cadastro de Produtos")
            window.set_focus()

            # campo produto
            send_keys(produto + "{TAB}")
            send_keys(quantidade + "{TAB}")
            send_keys(preco)
            
            botao_cadastrar = (595, 741)
            click(coords=botao_cadastrar)
            sleep(1)
            
            # Retornar para o campo "Produto"
            botao_produto = (690, 527)
            click(coords=botao_produto)
            sleep(1)
