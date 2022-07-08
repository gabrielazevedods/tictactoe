from kivy.lang import Builder
from kivymd.app import MDApp
from controller import *

#caso de empate
#MODEL
def no_winner(app):
  if app.winner == False and \
  app.root.ids.btn.disabled == True and \
  app.root.ids.btn2.disabled == True and \
  app.root.ids.btn3.disabled == True and \
  app.root.ids.btn4.disabled == True and \
  app.root.ids.btn5.disabled == True and \
  app.root.ids.btn6.disabled == True and \
  app.root.ids.btn7.disabled == True and \
  app.root.ids.btn8.disabled == True and \
  app.root.ids.btn9.disabled == True:
    app.root.ids.score.text = "EMPATE"

def win(app):
    # horizontal
    if app.root.ids.btn.text != "" and app.root.ids.btn.text == app.root.ids.btn2.text and app.root.ids.btn2.text == app.root.ids.btn3.text:
      end_game(app, app.root.ids.btn, app.root.ids.btn2, app.root.ids.btn3)
    
    if app.root.ids.btn4.text != "" and app.root.ids.btn4.text == app.root.ids.btn5.text and app.root.ids.btn5.text == app.root.ids.btn6.text:
      end_game(app, app.root.ids.btn4, app.root.ids.btn5, app.root.ids.btn6)

    if app.root.ids.btn7.text != "" and app.root.ids.btn7.text == app.root.ids.btn8.text and app.root.ids.btn8.text == app.root.ids.btn9.text:
      end_game(app, app.root.ids.btn7, app.root.ids.btn8, app.root.ids.btn9)

    # vertical
    if app.root.ids.btn.text != "" and app.root.ids.btn.text == app.root.ids.btn4.text and app.root.ids.btn4.text == app.root.ids.btn7.text:
      end_game(app, app.root.ids.btn, app.root.ids.btn4, app.root.ids.btn7)
    
    if app.root.ids.btn2.text != "" and app.root.ids.btn2.text == app.root.ids.btn5.text and app.root.ids.btn5.text == app.root.ids.btn8.text:
      end_game(app, app.root.ids.btn2, app.root.ids.btn5, app.root.ids.btn8)

    if app.root.ids.btn3.text != "" and app.root.ids.btn3.text == app.root.ids.btn6.text and app.root.ids.btn6.text == app.root.ids.btn9.text:
      end_game(app, app.root.ids.btn3, app.root.ids.btn6, app.root.ids.btn9)

    # diagonal
    if app.root.ids.btn.text != "" and app.root.ids.btn.text == app.root.ids.btn5.text and app.root.ids.btn5.text == app.root.ids.btn9.text:
      end_game(app, app.root.ids.btn, app.root.ids.btn5, app.root.ids.btn9)

    if app.root.ids.btn3.text != "" and app.root.ids.btn3.text == app.root.ids.btn5.text and app.root.ids.btn5.text == app.root.ids.btn7.text:
      end_game(app, app.root.ids.btn3, app.root.ids.btn5, app.root.ids.btn7)

    no_winner(app)

