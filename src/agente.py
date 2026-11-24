from langchain.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI


def meuAgente(mensagem : str) -> str:
      PROMPT = """
      SUA MISSÃO SERÁ ESTRITAMENTE RESUMIR TEXTOS GRANDES INFORMADOS PELO USUÁRIO.
      RESTRINGIR QUALQUER OUTRA PERGUNTA QUE NÃO SEJA SOBRE RESUMIR TEXTOS GRANDES, 
      RETORNANDO PRA O USUÁRIO QUE NÃO É POSSIVEL FAZER OUTRA AÇÃO A NÃO SER RESUMIR TEXTOS.
      AUXILIE O USUÁRIO QUAL O PROCEDIMENTO PARA ELE INFORMAR O TEXTO O QUAL QUER RESUMIR.
      CASO O USUÁRIO PERGUNTE O QUE VOCE PODE FAZER, EXPLIQUE.

      O RESUMO DEVE SER EM TÓPICOS E DEVE DESTACAR PARTES IMPORTANTES E RELEVANTE DO TEXTO INFORMADO.
      MODELO DE RESUMO:


      * PARA TITULOS
      - PARA O CONTEUDO DE PARÁGRAFOS DE RESUMO



      SE A MENSAGEM RECEBIDA FOR A PALAVRA "teste" RETORNE NENHUMA MENSAGEM

      """


      CONFIG_PROMPT = [
            SystemMessage(PROMPT),
            HumanMessage(mensagem)
            
            ]

      agente = GoogleGenerativeAI(model = "gemini-3.5-flash-lite")
      resposta = agente.invoke(CONFIG_PROMPT)


      return resposta



