import agente
from os import system
from exceptions import Tratamento_mensagem, Tratamento_credenciais
from dotenv import load_dotenv
import langchain_google_genai 

# carregando variaveis de ambiente no modulo
load_dotenv()

def main():

     if Tratamento_credenciais().chaveApiEstaVazia():
          print("ERRO: CHAVE DE API ESTA VAZIA NO ARQUIVO .ENV. INSIRA A CHAVE DE API NO ARQUIVO MENCIONADO")

     elif Tratamento_credenciais().chaveApiInvalida():

          print("ERRO: CHAVE DE API INVÁLIDA, DIGITE UMA CHAVE DE API VÁLIDA NO .ENV")


     else:
          
               while True:

                    mensagem_usuario = Tratamento_mensagem(input("digite algo ('sair' para sair):\n"))
                    print("\n")
                    

                    if(mensagem_usuario.eVazio() or mensagem_usuario.saoApenasNumeros()):
                         print("mensagem invalida")


                    elif mensagem_usuario.getMensagem() == "sair":
                         print("programa encerrado")
                         return 0

                    else:
                         try:
                              print("Trabalhando nisso...")
                              resposta = agente.meuAgente(mensagem_usuario.getMensagem())

         
                              """ 
                              limpa o terminal, porém não se sabe qual sistema operacional o usuário está utilizando
                              para isso a função 'system' retorna 1 para caso o comando nao existir no terminal e retorna 0 para quando o comando executar sem erro
                              """
                              system("clear") if not system("clear") else system("cls")




                              print(resposta, end="\n\n")



                         except langchain_google_genai.chat_models.GoogleAPIError as e:
                              if "503" in  str(e):
                                   print("ERRO: SERVIDOR OCUPADO, TENTE NOVAMENTE MAIS TARDE")
                                   print("programa encerrado")
                                   break

                              elif "501" in str(e):

                                   print("ERRO: RESPOSTA DO AGENTE DEMOROU MUITO: TIMEOUT")
                                   print("programa encerrado")
                                   break

                        





if __name__ == "__main__":
     main()