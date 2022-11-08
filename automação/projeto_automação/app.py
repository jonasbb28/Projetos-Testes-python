import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuário
pyautogui.click(668,401,duration=0.5)
pyautogui.write("Jonas")
# 2 - Clicar e digitar minha senha
pyautogui.click(670,428,duration=0.5)
pyautogui.write("123456")
# 3 - Clicar em "Entrar"
pyautogui.click(547,454,duration=0.5)
# 4 - Extrair cada produto
with open("produtos.txt", "r") as arquivo:
    for linha in arquivo:
        produto = linha.split(",")[0]
        quantidade = linha.split(",")[1]
        preco = linha.split(",")[2]
        # 1 - Clicar e digitar produto
        pyautogui.click(382,388,duration=0.5)
        pyautogui.write(produto)
        # 2 - Clicar e digitar quantidade
        pyautogui.click(374,414,duration=0.5)
        pyautogui.write(quantidade)
        # 3 - Clicar e digitar preço
        pyautogui.click(369,440,duration=0.5)
        pyautogui.write(preco)
        # 4 - Clicar em "registrar"
        pyautogui.click(268,597,duration=0.5)
        sleep(1)

