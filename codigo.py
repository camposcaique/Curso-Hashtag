# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
   # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Dar uma pausa um pouco maior (3 segundos)
pyautogui.time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=803, y=405)
pyautogui.write("camppos.caique@gmail.com")

# Escrever a senha
pyautogui.press("tab")
pyautogui.write("30082019")

# Clickar no botão de logar
pyautogui.click(x=958, y=569)

# Passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
# Selecionar uma linha da tabela
for linha in tabela.index:

    # Clickar no primeiro campo
    pyautogui.click(x=742, y=291)

    # Código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # Tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # Categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # Preço do produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")    

    # Executar o botão de enviar
    pyautogui.press("enter")
    pyautogui.press("home")

# Passo 5: Repetir o processo de cadastro até acabar as informações
