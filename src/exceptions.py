class Tratamento_mensagem:
     def __init__(self, mensagem : str):
          self.mensagem = mensagem


     def eVazio(self):
          return True if len(self.mensagem) == 0 else False

     def saoApenasNumeros(self):
          return self.mensagem.isdigit()


     def getMensagem(self):
          return self.mensagem