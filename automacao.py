from selenium import webdriver 
import time 
import tkinter as tk


def preencher_formulario(valor_digitado):
    print(f"Automação iniciada com: {valor_digitado}")

    # Abrir navegador 
    navegador = webdriver.Chrome()

    # Acessar um site
    navegador.get("https://www.zapgrafica.com.br/produto")

    # Colocar o navegador em tela cheia 
    navegador.maximize_window()

    # selecionar elemento na tela 
    botao_login = navegador.find_element("id", "hoverDropdown")
    botao_login.click()

    # Escrever em campo na tela
    input_email = navegador.find_element("id", "input-home1-email") 
    input_email.send_keys("adm@graficaconceito.com")

    # Escrever em campo na tela
    input_senha = navegador.find_element("id", "input-home1-senha")
    input_senha.send_keys("Conce1to8675.")

    btn_entrar = navegador.find_element("id", "btnEntrarHome")
    btn_entrar.click()
    time.sleep(10)

    elements = navegador.find_elements("class name", "btn-card-compra-v2")

    # lista de botões com "Comprar"
    btns_comprar = [element for element in elements if "Comprar" in element.text]

    # Dar scroll
    if len(btns_comprar) > 1:
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", btns_comprar[2])
        time.sleep(2)
        btns_comprar[2].click()
    else:
        print("Botão 'Comprar' não encontrado!")
        
    nome_pedido = navegador.find_element("name", "edtNomeServico")
    nome_pedido.send_keys(valor_digitado)
    time.sleep(3)
    
    btn_check = navegador.find_element("id", "chkTermos")
    btn_check.click()
    time.sleep(2)
    # selecionar uma aba
    navegador.get("https://www.zapgrafica.com.br/home/categoria/cartoes-de-visita/couche-300g/verniz-localizado-/lam-fosca-e-verniz-localizado-frente-e-verso")

    
    btn_finalizar_compra = navegador.find_element("id", "btnComprar")
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", btn_finalizar_compra)
    
   
    btn_finalizar_compra.click()        
    time.sleep(10)


