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