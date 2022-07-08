from kivy.lang import Builder
from kivymd.app import MDApp
from model import *

#CONTROLLER
def end_game(app, a, b, c):
    app.winner = True
    a.color = "red"
    b.color = "red"
    c.color = "red"

    #desabilitando todos os botões
    disable_all_buttons(app)

    #mostrando quem ganhou
    app.root.ids.score.text = f"{a.text} Ganhou!"

def disable_all_buttons(app):
    app.root.ids.btn.disabled = True
    app.root.ids.btn2.disabled = True
    app.root.ids.btn3.disabled = True
    app.root.ids.btn4.disabled = True
    app.root.ids.btn5.disabled = True
    app.root.ids.btn6.disabled = True
    app.root.ids.btn7.disabled = True
    app.root.ids.btn8.disabled = True
    app.root.ids.btn9.disabled = True

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
    win(app)

def restart(app): 
    #X sempre começa
    app.turn = "X"

    #botões voltam a funcionar
    app.root.ids.btn.disabled = False
    app.root.ids.btn2.disabled = False
    app.root.ids.btn3.disabled = False
    app.root.ids.btn4.disabled = False
    app.root.ids.btn5.disabled = False
    app.root.ids.btn6.disabled = False
    app.root.ids.btn7.disabled = False
    app.root.ids.btn8.disabled = False
    app.root.ids.btn9.disabled = False

    #limpa o texto dos botões
    app.root.ids.btn.text = ""
    app.root.ids.btn2.text = ""
    app.root.ids.btn3.text = ""
    app.root.ids.btn4.text = ""
    app.root.ids.btn5.text = ""
    app.root.ids.btn6.text = ""
    app.root.ids.btn7.text = ""
    app.root.ids.btn8.text = ""
    app.root.ids.btn9.text = ""

    #reseta as cores
    app.root.ids.btn.color = "white"
    app.root.ids.btn2.color = "white"
    app.root.ids.btn3.color = "white"
    app.root.ids.btn4.color = "white"
    app.root.ids.btn5.color = "white"
    app.root.ids.btn6.color = "white"
    app.root.ids.btn7.color = "white"
    app.root.ids.btn8.color = "white"
    app.root.ids.btn9.color = "white"

    app.root.ids.score.text = "X VAI PRIMEIRO"

    app.winner = False