from kivy.lang import Builder
from kivymd.app import MDApp
from controller import *
import model


def presser(app, btn): 
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
    
    #checa se alguém ganhou
    model.win(app)