import http
import speech_recognition as sr
import webbrowser
import pyttsx3
from decouple import config
from datetime import datetime
import keyboard

loading_call_list =[
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
    speak(f"{HOSTNAME} here, how may I assist you?")  
    print('to initialize press ctrl+alt+m')      


listening = False    
    
def start_listening():
    global listening
    listening = True
    print('listening...')

def pause_listening():
    global  listening
    listening = False
    print('shutting off') 
    speak('shutting off')
    
keyboard.add_hotkey('ctrl+alt+m', start_listening)
keyboard.add_hotkey('ctrl+alt+i', pause_listening)                        


def speak(text):
    engine.say(text)
    engine.runAndWait()

def song(songName):
    webbrowser.open(f"https://www.youtube.com/results?search_query={songName}")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'exit' in queri or 'stop' in queri:
            speak(loading_call_list)
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night take care")
            else:
                speak("Have a good day")
            exit()

    except Exception:
        speak("Sorry I couldn't understand. Can you please repeat that?")
        queri = 'None'
    return queri


if __name__ == '__main__':
    greet()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am absolutely fine sir. What about you")  

            elif "open" in query:
                query = query.replace("open", "").strip()
                webbrowser.open(f"https://{query}.com")
                speak(f"opening {query}")
        
                
            elif "play" in query:
                songName = query.replace("play", "").strip()
                song(songName)

            elif "news" in query:
                webbrowser.open("https://www.google.com/search?q=news")  

               

           
     
    #  processCommand(command)                           

                                                


    # except Exception as e:
    #     print("Error; {0}".format(e))

        
    