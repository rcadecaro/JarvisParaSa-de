# -*- coding: utf-8 -*-
#instalar o pyaudio  pip install pipwin pelo pipwin e depois instalar usando python -m pipwin pyaudio
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import pyttsx3
from datetime import datetime, timedelta
from geminiText import awnser_ai, chat_ai
import webbrowser


def ouvir_microfone():

    cont = 0

    speak = pyttsx3.init()
    # speak.setProperty('voice', 'portugal')
    speak.setProperty("rate", 280)
    # voices = speak.getProperty('voices')
    # speak.setProperty("voice", voices[0].id)


    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        iniciado = 0
        iniciado_temp = 0

        while True:
            speak.runAndWait() 
            tempoagora = datetime.now()

                                                                                                
            # iniciação
            if (iniciado == 0):

                # webbrowser.open(f'https://bno23.pythonanywhere.com/monitoramento/jarvis iniciado e disponível,A temperatura da sala do datacenter está em {temp} graus celsius e a umidade está em {hum} por cento/2399368517623')

                speak.say(f"jarvis iniciado e disponível!")
                speak.runAndWait()  

                iniciado = 1

            monitoraFrase = ''            

            microfone.adjust_for_ambient_noise(source)              
            try:
                audio = microfone.listen(source)
                frase = microfone.recognize_google(audio, language='pt-BR')

                frasemin = frase.lower()
                monitoraFrase = frasemin

                if 'jarvis' in frasemin or 'Chaves' in frasemin :
                    anwserAI = awnser_ai(f"{frasemin}, resuma no máximo 5 linhas")
                    resp = anwserAI.replace('*', ',')

                    print(resp)
                    speak.say(resp)   

                # if 'jarvis ativar texto' in frasemin or 'jarvis abrir texto'  or 'chaves abrir texto' in frasemin:
                #     os.system('start swriter.exe')
                #     print('Libre office Texto Ativado ')
                #     # webbrowser.open(f'https://bno23.pythonanywhere.com/monitoramento/aplicativo de office calc iniciado/2399368517623')
                #     speak.say(f"Libre office Texto Ativado!")
                #     speak.runAndWait()  

                # if 'jarvis ativar planilha' in frasemin or 'jarvis abrir planilha' or 'chaves abrir planilha' in frasemin:
                #     os.system('start scalc.exe')
                #     print('Libre office planilha ativado ')
                #     speak.say(f"Libre office planilha ativado!")
                #     speak.runAndWait()  

                    # webbrowser.open(f'https://bno23.pythonanywhere.com/monitoramento/aplicativo de office writer iniciado/2399368517623')
                    
                if 'jarvis menu' in frasemin in frasemin:
                    menu = """
                        Os comandos disponíveis são 
                        Para apresentar: jarvis apresentação, jarvis próximo, jarvis anterior e jarvis encerrar,
                        Para utilitários: jarvis conversão, jarvis download,
                        Para usar chat gpt: assitente pergunta, jarvis o que é
                    """
                    print(menu)
                    speak.say(menu)   

                print(frase)
                frase = ''
                monitoraFrase = ''
                            
            except LookupError:
                print(f'1: Não Entendi {monitoraFrase}')
                print(tempoagora)

            except sr.UnknownValueError as e:
                print(f'2: Valor Inválido {monitoraFrase}')
                print(tempoagora)

            except KeyboardInterrupt:
                print(f'3: keyboard interrupt {monitoraFrase}')
                print(tempoagora)
                
            except:
                print(f'{cont}')
                print(tempoagora)
            cont +1
