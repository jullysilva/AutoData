import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.7

# PASSO 1: Entrear no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# - Abrir o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# print(pyautogui.position())

pyautogui.click(x=961, y=581)
pyautogui.hotkey("ctrl", "t")
time.sleep(2)

# - Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# PASSO 2: Fazer Login
time.sleep(3)
# print(pyautogui.position())
pyautogui.click(x=757, y=1488)
pyautogui.write("jornadapython@gmail.com")
pyautogui.press("tab")
pyautogui.write("jornadapython")
pyautogui.press("enter")

time.sleep(3)
# PASSO 3: Importar a base de dados
tabela = pandas.read_csv("produtos.csv")

print(pyautogui.position())
# pyautogui.click(x=757, y=1488)


for linha in tabela.index:
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(10000)
# PASSO 4: Cadastrar 1 produto

# PASSO 5: Repetir parar todos os produtos 