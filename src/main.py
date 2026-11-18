import agente
from exceptions import Tratamento_mensagem

def main():
     while True:

          mensagem_usuario = Tratamento_mensagem(input("digite algo ('sair' para sair):"))
          

          if(mensagem_usuario.eVazio() or mensagem_usuario.saoApenasNumeros()):
               print("mensagem invalida")


          elif mensagem_usuario.getMensagem() == "sair":
               print("programa encerrado")
               break

          else:
               resposta = agente.meuAgente(mensagem_usuario.getMensagem())
               print(resposta, end="\n\n")






if __name__ == "__main__":
     main()