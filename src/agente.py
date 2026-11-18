from langchain.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
try:  
      load_dotenv()


except:
      print("Chave invalida")



def meuAgente(mensagem : str) -> str:
     CONFIG_PROMOT = [
           SystemMessage("apenas converse com o usuario de acordo com o que ele responder"),
           HumanMessage(mensagem)
           
           ]

     agente = GoogleGenerativeAI(model = "gemini-3.5-flash-lite")
     resposta = agente.invoke(CONFIG_PROMOT)


     return resposta