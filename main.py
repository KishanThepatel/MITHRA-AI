import http
import speech_recognition as sr
import webbrowser
import pyttsx3
from decouple import config
from datetime import datetime
import random
import keyboard

loading_call_list = [
    "working on it",
    "on it",
    "just a second"
]

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('volume',1.5)
engine.setProperty('rate', 195 )
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
USER = config('USER', default = 'Kishan')
HOSTNAME = config('BOT', default = 'mythhra')
newsApi = "386fb4f3ba594671b96b222e6121f072"


def greet():
    hour = datetime.now().hour
    if(hour>=6 and hour<=12):
        speak(f"Good morning {USER}")
    elif(hour>=12 and hour<=16):
        speak(f"Good afternoon {USER}")
    elif(hour>=16 and hour<=19):
        speak(f"good evening {USER}")
    speak(f'{HOSTNAME} here, How may I assist you?')                        


def speak(text):
    engine.say(text)
    engine.runAndWait()

def song(songName):
    webbrowser.open(f"https://www.youtube.com/results?search_query={songName}")


def processCommand(c):
    if "open" in c.lower():
        c = c.lower().replace("open", "").strip()
        webbrowser.open(f"https://{c}.com")
        speak(f"opening {c}")
   
        
    elif "play" in c.lower():
        songName = c.lower().replace("play", "").strip()
        song(songName)

    elif "news" in c.lower():
        webbrowser.open("https://www.google.com/search?q=news")
 
    

def take_command():
    speak("Initializing mythhra") 

    greet() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google_cloud(audio,language='en-in')
        print(query)
        if not 'stop' in query or 'exit' in query:
            speak(random.choice(loading_call_list))
        else:
            speak('shutting off')
            exit()


    except Exception:
        speak("sorry couldn't catch that")
        query = 'None'
    return query

listening = False

def start_listening():
    global listening
    listening = True
    print('listening')

def pause_listening():
    global  listening
    listening = False
    print('shutting off')

keyboard.add_hotkey('')       

if __name__ == "main":
    greet()
    while True:
        query1 = take_command().lower()
        if 'how are you' in query1:
            speak('I am absolutely fine, how about you?')


               

           
     
    #  processCommand(command)                           

                                                


    # except Exception as e:
    #     print("Error; {0}".format(e))

        
    