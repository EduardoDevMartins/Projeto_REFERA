import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def confirmar_alternativa():
    # Defina as informações do site
    # Substitua pela URL do site que você deseja acessar
    url = ""

    xpath_usuario = "/html/body/app-root/dx-drawer/div/div[2]/div[2]/div/app-container/login/div/div[1]/div/div[4]/div[1]/pm-form/form/div/div/div[1]/pm-input/div/div/pm-text/div/input"

    xpath_senha = "/html/body/app-root/dx-drawer/div/div[2]/div[2]/div/app-container/login/div/div[1]/div/div[4]/div[1]/pm-form/form/div/div/div[2]/pm-input/div/div/pm-text/div/input"

    xpath_alternativa = "//button[@class='pm-btn-icon']"

    # Inicialize o driver do Selenium (escolha o driver correto para o seu navegador)
    # Substitua pelo driver do seu navegador (por exemplo, Firefox ou Safari)
    driver = webdriver.Firefox()

    # Acesse o site
    driver.get(url)

    # Insira o usuário
    elemento_usuario = driver.find_element(By.XPATH, xpath_usuario)
    elemento_usuario.send_keys("")

    # Insira a senha
    elemento_senha = driver.find_element(By.XPATH, xpath_senha)
    elemento_senha.send_keys("")

    # Envie o formulário de login pressionando Enter
    elemento_senha.send_keys(Keys.RETURN)


# Defina os horários em que deseja confirmar a alternativa
horarios = ["09:00", "14:00", "18:45"]  # Substitua pelos horários desejados

while True:
    # Obtenha o horário atual
    agora = datetime.now().strftime("%H:%M")

    # Verifique se o horário atual está na lista de horários desejados
    if agora in horarios:
        # Chame a função para confirmar a alternativa
        confirmar_alternativa()
        print("Alternativa confirmada às", agora)

    # Aguarde um minuto antes de verificar novamente
    time.sleep(60)
