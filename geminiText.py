import pathlib
import textwrap
import google.generativeai as genai
from key import GEMINIKEY
from treinamento import HISTORY

genai.configure(api_key=GEMINIKEY)

def awnser_ai(question):
    try:

        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        return response.text
    except:
        return 'Não entendi a pergunta'
    
def chat_ai(text):
    try:
        model = genai.GenerativeModel('gemini-pro')

        chat = model.start_chat(history = HISTORY)
            
        response = chat.send_message(f"{text}")
        return response.text
    except:
        return 'Não entendi a pergunta'

# print(chat_ai("""
#     Resuma o pop que fala sobre liberação no sistema hemovida em 5 linhas
# """))
# print(chat_ai("""
#     comente a importância da portaria de consolidação n 5 anexo iv, faça um comentário de até 2 linhas sobre o Em Auditoria Interna realizada no dia 12/04/2024, evidenciado o acondicionamento de Concentrado de Hemácias em refrigerador apresentando temperatura mínima abaixo de 2°C, estando em desacordo com os itens 55 e 66.
# """))
# print(chat_ai("""
#     qual a importância do protocolo de cirúrgia segura
# """))
    
# model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("Qual o significado da vida?")
# print(response.text)

