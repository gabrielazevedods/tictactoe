from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
  def build(self):
    self.theme_cls.theme_style = "Dark"
    self.theme_cls.primary_palette= "BlueGray"
    return Builder.load_file('main.kv')

  #define de quem é a vez
  turn = "X"

  #diz se alguém já ganhou ou não
  winner = False

  #caso de empate
  def no_winner(self):
    if self.winner == False and \
    self.root.ids.btn.disabled == True and \
    self.root.ids.btn2.disabled == True and \
    self.root.ids.btn3.disabled == True and \
    self.root.ids.btn4.disabled == True and \
    self.root.ids.btn5.disabled == True and \
    self.root.ids.btn6.disabled == True and \
    self.root.ids.btn7.disabled == True and \
    self.root.ids.btn8.disabled == True and \
    self.root.ids.btn9.disabled == True:
      self.root.ids.score.text = "EMPATE"

  def end_game(self, a, b, c):
    self.winner = True
    a.color = "red"
    b.color = "red"
    c.color = "red"

    #desabilitando todos os botões
    self.disable_all_buttons()

    #mostrando quem ganhou
    self.root.ids.score.text = f"{a.text} Ganhou!"
  
  def disable_all_buttons(self):
    self.root.ids.btn.disabled = True
    self.root.ids.btn2.disabled = True
    self.root.ids.btn3.disabled = True
    self.root.ids.btn4.disabled = True
    self.root.ids.btn5.disabled = True
    self.root.ids.btn6.disabled = True
    self.root.ids.btn7.disabled = True
    self.root.ids.btn8.disabled = True
    self.root.ids.btn9.disabled = True

  def win(self):
    # horizontal
    if self.root.ids.btn.text != "" and self.root.ids.btn.text == self.root.ids.btn2.text and self.root.ids.btn2.text == self.root.ids.btn3.text:
      self.end_game(self.root.ids.btn, self.root.ids.btn2, self.root.ids.btn3)
    
    if self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn6.text:
      self.end_game(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)

    if self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text == self.root.ids.btn9.text:
      self.end_game(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)

    # vertical
    if self.root.ids.btn.text != "" and self.root.ids.btn.text == self.root.ids.btn4.text and self.root.ids.btn4.text == self.root.ids.btn7.text:
      self.end_game(self.root.ids.btn, self.root.ids.btn4, self.root.ids.btn7)
    
    if self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn8.text:
      self.end_game(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)

    if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text == self.root.ids.btn9.text:
      self.end_game(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

    # diagonal
    if self.root.ids.btn.text != "" and self.root.ids.btn.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn9.text:
      self.end_game(self.root.ids.btn, self.root.ids.btn5, self.root.ids.btn9)

    if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn7.text:
      self.end_game(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

    self.no_winner()

  def presser(self, btn): 
    if self.turn == "X":
      btn.text = "X"
      btn.disabled = True
      self.root.ids.score.text = "VEZ DE O"
      self.turn = "O"
    else:
      btn.text = "O"
      btn.disabled = True
      self.root.ids.score.text = "VEZ DE X"
      self.turn = "X"
    
    #checa se alguém ganhou
    self.win()

  def restart(self): 
    #X sempre começa
    self.turn = "X"

    #botões voltam a funcionar
    self.root.ids.btn.disabled = False
    self.root.ids.btn2.disabled = False
    self.root.ids.btn3.disabled = False
    self.root.ids.btn4.disabled = False
    self.root.ids.btn5.disabled = False
    self.root.ids.btn6.disabled = False
    self.root.ids.btn7.disabled = False
    self.root.ids.btn8.disabled = False
    self.root.ids.btn9.disabled = False

    #limpa o texto dos botões
    self.root.ids.btn.text = ""
    self.root.ids.btn2.text = ""
    self.root.ids.btn3.text = ""
    self.root.ids.btn4.text = ""
    self.root.ids.btn5.text = ""
    self.root.ids.btn6.text = ""
    self.root.ids.btn7.text = ""
    self.root.ids.btn8.text = ""
    self.root.ids.btn9.text = ""

    #reseta as cores
    self.root.ids.btn.color = "white"
    self.root.ids.btn2.color = "white"
    self.root.ids.btn3.color = "white"
    self.root.ids.btn4.color = "white"
    self.root.ids.btn5.color = "white"
    self.root.ids.btn6.color = "white"
    self.root.ids.btn7.color = "white"
    self.root.ids.btn8.color = "white"
    self.root.ids.btn9.color = "white"

    self.root.ids.score.text = "X VAI PRIMEIRO"

    self.winner = False

MainApp().run()

