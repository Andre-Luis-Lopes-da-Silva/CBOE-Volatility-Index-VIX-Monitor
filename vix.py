from tkinter import *
from yahoo_fin import stock_info as si
import pyttsx3
import speech_recognition as sr

janela: Tk = Tk()   # create the window
janela.title('VIX monitor')
janela.resizable(False, False)  # Prevents anyone from being able to resize the window

label1 = Label(janela, text='VIX = ', bg='white', fg='blue', font=("Arial", 20), padx=20, pady=20).grid(row=2, column= 2)  
vix_cotacao = round(si.get_live_price('^VIX'),2) # get the current value of VIX
label2 = Label(janela, text=vix_cotacao, bg='white', fg='blue', font=("Arial", 20), padx=20, pady=20).grid(row=2, column= 3) 

tempo_att = 1000 #ms

def neue_fenster(mensagem):
    fenster: Tk = Tk()   # create the new window
    fenster.title('ALERT')
    fenster.resizable(False, False)  # Prevents anyone from being able to resize the window
    Label(fenster, text=mensagem, bg='white', fg='blue', font=("Arial", 20), padx=20, pady=20).grid(row=2, column= 2)  
    
def sprechen(mensagem):
    engine = pyttsx3.init()
    engine.say(mensagem)
    engine.runAndWait()

def upd():   
    vix_cotacao = round(si.get_live_price('^VIX'),2) 
    label2 = Label(janela, text=vix_cotacao, bg='white', fg='blue', font=("Arial", 20), padx=20, pady=20, anchor = 'e').grid(row=2, column= 3) 
    if vix_cotacao > 25.1:
        mensagem = 'Volatility requires attention'
        neue_fenster(mensagem)
        sprechen(mensagem)
    elif vix_cotacao > 36.1:    
        mensagem =  'High volatility, be carefull'
        neue_fenster(mensagem)
        sprechen(mensagem)
    elif vix_cotacao > 48.9:     
        mensagem = 'Critical volatility, urgently use hedging strategies'
        neue_fenster(mensagem)
        sprechen(mensagem)
    
janela.after(tempo_att, upd)   # keeps Vix updated every 1000 millisecond interval
janela.mainloop() 

