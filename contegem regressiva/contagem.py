from time import sleep
import PySimpleGUI as sg

class telapytho:
    def __init__(self):
        #layout
        layout = [
            [sg.Text("Vamos para a contagem")],
            [sg.Text("Início: "), sg.Input(size=(15, 0), key="inicio")],
            [sg.Text("Fim: "), sg.Input(size=(15,0), key="fim")],
            [sg.Button("Começar a contagem")]
        ]
        #janela
        self.janela = sg.Window("Contagem").layout(layout)


    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()


tela = telapytho()
tela.iniciar()