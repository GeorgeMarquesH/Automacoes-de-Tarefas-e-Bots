# bibliotecas  = pacotes de código
# pip install pyautogui
# passo a passo do programa:
# Passo 1: entrar no sistema da empresa
# Passo 2: fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos

import pyautogui
import time
import pandas

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)

pyautogui.PAUSE = 0.5  # pausa de 0.5 segundo entre cada comando
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# se fosse com import webbrowser:
# webbrowser.open(link) 
# Fazer uma pausa maior pro site carregar 
# time.sleep(3)
# depois usar o pyautogui.click

# passo a passo do programa usando pyautogui:

# Passo 1: entrar no sistema da empresa:

# Abrir o navegador
pyautogui.press("win") 
pyautogui.write("edge") 
pyautogui.press("enter") 
# Espera mais tempo para garantir que o navegador abriu 
time.sleep(2)
# Seleciona a barra de endereços 
pyautogui.hotkey("ctrl", "l") 
time.sleep(1)
# Digita o link 
pyautogui.write(link) 
pyautogui.press("enter")
# Fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 2: fazer login:

# Clicar no campo de email - (criar arquivo auliar para pegar a posição da tela: auxiliar.py)
pyautogui.click(x=804, y=459)
pyautogui.write("georgemarquesh@gmail.com")
time.sleep(2)
pyautogui.press("tab") 
pyautogui.write("wasjk832@kjs")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
# Fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 3: Abrir a base de dados (importar o arquivo):
# rodar pip install pandas e openpyxl no terminal

tabela = pandas.read_csv("Aula1/produtos1.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    # codigo
    pyautogui.click(x=642, y=313)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preco_unitario
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # obs
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    # voltar para o início da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos