import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from sinteze import ouvir_microfone
from threading import Thread
# janela = tk.Tk()
# janela.title('Dúvida sobre')
# janela.geometry('300x300')

from geminiText import chat_ai

resp = ''



class Th(Thread):

    def __init__ (self, num):
            Thread.__init__(self)
            self.num = num

    def run(self):

        ouvir_microfone()


def iniciar_Thread():
    a = Th(1)
    a.start()   

def consultarAi():

    resp = msg.get()
    # // verificar campo em branco

    if msg.get() == '':
        print('Campo em branco')
        messagebox.showwarning(title='Erro', message='👻Campo(s) de preenchimento obrigatório')

    else:
        resp = chat_ai(resp).replace('*', ',')
        textbox_1.configure(state='normal')
        textbox_1.insert(tk.END, f'USUÁRIO 🙂: {msg.get()} \n IASEP 🤖: {resp} \n\n')
        textbox_1.configure(state='disabled')
        
        msg.delete(0, tk.END)

            # abrirRemessa(ent_rem_abrir.get())



# texto = tk.Label(janela, text='Olá Mundo!')
# texto.pack()

# botao = tk.Button(janela, text='Clique Aqui', command=clique)
# botao.pack()


# janela.mainloop()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')


janela = customtkinter.CTk()
janela.resizable(False, False)

janela.title('JARVIS PARA SAÚDE')
janela.geometry('1000x600')

lbl_textbox1 = customtkinter.CTkLabel(janela, text='JARVIS PARA A SAÚDE', font=('Arial', 35))
lbl_textbox1.pack(padx=10, pady=10)

frame = customtkinter.CTkFrame(master=janela, width=200, height=400)
frame.pack(side='left', padx=10)

global imagemlogo
imagemlogo = customtkinter.CTkImage(Image.open("img/seg.jpeg"),  size=(110, 110)) 

lbl_imagem_logo = customtkinter.CTkLabel(frame, text="",image=imagemlogo)
lbl_imagem_logo.pack(padx=10, pady=10)

lbl_msg = customtkinter.CTkLabel(frame, text='Dúvida:', font=('Arial', 23))
lbl_msg.pack(padx=10, pady=10)

msg = customtkinter.CTkEntry(frame, width=200, height=30, text_color='yellow', font=('Arial', 16, 'bold'))
msg.pack(padx=30, pady=10)

# chk_termo = customtkinter.CTkCheckBox(frame, text='Aceito os termos de uso')
# chk_termo.pack(padx=10, pady=10)
buttom_1 = customtkinter.CTkButton(frame, text='Consultar', command=consultarAi, font=('Arial', 18))
buttom_1.pack(padx=10, pady=20)

buttom_1 = customtkinter.CTkButton(frame, text='Conversar', command=iniciar_Thread, font=('Arial', 18))
buttom_1.pack(padx=10, pady=20)

frame2 = customtkinter.CTkFrame(master=janela, width=800, height=200)
frame2.pack(side='right', padx=10)

lbl_textbox1 = customtkinter.CTkLabel(frame2, text='Histórico:', font=('Arial', 23))
lbl_textbox1.pack(padx=10, pady=10)

textbox_1 = customtkinter.CTkTextbox(frame2, width=800, height=200, font=('Arial', 14, 'bold'), text_color='green')
textbox_1.pack(padx=5, pady=5)
textbox_1.configure(state='disabled')

lbl_textbox2 = customtkinter.CTkLabel(frame2, text='Dicas:', font=('Arial', 23))
lbl_textbox2.pack(padx=10, pady=10)

textbox_2 = customtkinter.CTkTextbox(frame2, width=800, height=100, font=('Arial', 12, 'bold'), text_color='orange')
textbox_2.insert(tk.END, f'- Jarvis o que é cirúrgia segura\n - Jarvis o que é segurança do paciente\n- Jarvis o que é protocolo de identificação do paciente\n- Jarvis o que é protocolo de segurança no uso e administração de medicamentos\n- Jarvis o que é protocolo de risco de queda\n- Jarvis o que é protocolo de higienização das mãos\n- Jarvis o que é protocolo de úlcera por pressão\n- Como realizar o procedimento seguro seguindo o protocolo administraçao de medicamentos\n')

textbox_2.pack(padx=5, pady=5)
textbox_2.configure(state='disabled')





janela.mainloop()