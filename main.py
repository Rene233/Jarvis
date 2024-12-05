import pyttsx3
import speech_recognition as sr
import keyboard
import os
import subprocess as sp
from decouple import config
from datetime import datetime
from conv import random_text 
from random import choice
from online import find_my_ip, search_on_google, search_on_wikipedia, youtube

engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.5)
engine.setProperty('rate',225)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

USER = config('USER')
HOSTNAME = config('BOT')




def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.now().hour
    if (hour>=6) and (hour < 12):
        speak(f'Good Morning {USER}')
    elif (hour >= 12) and (hour <=16 ):
        speak(f'Good Afternoon {USER}')
    elif (hour >= 16) and (hour < 19):
        speak(f'Good evening {USER}')
    speak(f"I am {HOSTNAME}. How can I Assist you Today? {USER}")


listening = False

def start_listening():
    global listening
    listening = True
    print("start listening ")

def pause_listening():
    global listening
    listening = False
    print("stopped listening")


keyboard.add_hotkey("ctrl+n" ,start_listening)
keyboard.add_hotkey("ctrl+m" ,pause_listening)




def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing.....")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak('Good night Sir,take care!')
            else:
                speak('Have a good day sir.')
            exit()
    except Exception:
        speak("Sorry I couldn't understand you! Can you please repeat that?")
        queri = 'None'
    return queri




if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
             query = take_command().lower()
             if "How are you?" in query:
                speak("I am absolutely fine sir.")

             elif "open command prompt" in query:
                 speak("Opening command prompt sir")
                 os.system('start cmd')

             elif "open camera" in query:
                 speak("opening Camera sir")
                 sp.run('start microsoft.windows.camera:',shell=True)

             elif "open notepad" in query:
                 speak('opening Notepad sir')
                 notepad_path = "C:\\Windows\\System32\\notepad.exe"
                 os.startfile(notepad_path)


             elif "open discord" in query:
                 speak('open Discord sir')
                 discord_path = "C:\\Users\\Rene\\AppData\\Local\\Discord\\app-1.0.9173\\Discord.exe"
                 os.startfile(discord_path)

             elif "open code editor" in query:
                speak("Opening VS code sir")
                VS_code_location = "C:\\Users\\Rene\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(VS_code_location)
             elif "ip adress" in query:
                 ip_adress = find_my_ip()
                 speak(
                     f"your ip adress is {ip_adress}"
                 )
                 print(f"Your Ip Adress is {ip_adress}")

             elif "open youtube" in query:
                 speak("What do you want to play on Youtube sir?")
                 video = take_command().lower()
                 youtube(video)
                 
             elif "open google" in query:
                 speak("What do you want to search {USER}")
                 query = take_command().lower()
                 search_on_google(query)
        
        
             elif "wikipedia" in query:
                 speak("What do you want to search on Wikipedia sir")
                 search = take_command().lower()
                 results = search_on_wikipedia(search)
                 speak(f"According to wikipedia,{results}")
                 speak("I am printing it on Terminal.")
                 print(results)    