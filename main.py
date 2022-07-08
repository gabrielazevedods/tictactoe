from kivy.lang import Builder
from kivymd.app import MDApp
from model import *
import view
from controller import *

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
  def empate(self):
    no_winner(self)

  def fim_de_jogo(self):
    end_game(self)

  def vencedor(self):
    win(self)

  def presser(self, btn): 
    view.presser(self, btn)

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

