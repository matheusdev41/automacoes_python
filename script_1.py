from selenium import webdriver 
import time 

# Abrir navegador 
navegador = webdriver.Chrome()

# Acessar um site
navegador.get("https://www.zapgrafica.com.br/produto")

# Colocar o navegador em tela cheia 
navegador.maximize_window()

# selecionar elemento na tela 
botao_login = navegador.find_element("id", "hoverDropdown")
botao_login.click()

input_email = navegador.find_element("id", "input-home1-email")
input_email.send_keys("adm@graficaconceito.com")

input_senha = navegador.find_element("id", "input-home1-senha")
input_senha.send_keys("Conce1to8675.")

btn_entrar = navegador.find_element("id", "btnEntrarHome")
btn_entrar.click()

time.sleep(10)