from kivy.lang import Builder
from kivymd.app import MDApp
from controller import *
import model


def presser(app, btn): 
	#FUNÇÃO CHAMADA AO APERTAR O BOTÃO
	#COLOCA NO BOTÃO O JOGADOR QUE APERTOU (X OU BOLA)
	#E DIZ DE QUEM É A VEZ
    if app.turn == "X":
      btn.text = "X"
      btn.disabled = True
      app.root.ids.score.text = "VEZ DE O"
      app.turn = "O"
    else:
      btn.text = "O"
      btn.disabled = True
      app.root.ids.score.text = "VEZ DE X"
      app.turn = "X"
    
    #CHECA SE ALGUÉM GANHOU
    model.win(app)