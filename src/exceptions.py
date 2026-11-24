from os import getenv
from agente import meuAgente
import langchain_google_genai


class Tratamento_mensagem:
     def __init__(self, mensagem : str):

          # atributo privado
          self.__mensagem = mensagem


     def eVazio(self):
          return True if len(self.__mensagem) == 0 else False

     def saoApenasNumeros(self):
          return self.__mensagem.isdigit()

     def getMensagem(self):
          return self.__mensagem


class Tratamento_credenciais:

     def __init__(self):
          # atributo privado
          self.__chaveAPI = getenv("GOOGLE_API_KEY") 

     def chaveApiEstaVazia(self):
          return False if self.__chaveAPI else True
     

     def chaveApiInvalida(self):
          try:
               meuAgente("teste")
               return False
               
          except  langchain_google_genai.chat_models.GoogleAuthenticationError as e:

               if "401" in str(e):
                    return True
               
          


