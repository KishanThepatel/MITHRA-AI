import http
import speech_recognition as sr
import webbrowser
import pyttsx3
from decouple import config
from datetime import datetime
import keyboard
import requests

loading_call_list =[
    "just a second"
]

listening = False

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('volume',1.5)
engine.setProperty('rate', 195 )
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
USER = config('USER', default = 'Kishan')
HOSTNAME = config('BOT', default = 'mythhra')
newsApi = "386fb4f3ba594671b96b222e6121f072"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def song(songName):
    webbrowser.open(f"https://www.youtube.com/results?search_query={songName}")

def take_command():
    global listening
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=4, phrase_time_limit=3)
 
        try:
            queri = r.recognize_google(audio, language='en-in').lower()
            print(f"Recognized: {queri}")

            if 'mitra' in queri:
                listening = True
                queri = queri.replace('mitra', "").strip()
                return queri

            if 'exit' in queri or 'stop' in queri:                                    
                hour = datetime.now().hour
                listening = False
                if hour >= 21 and hour < 6:
                    speak("Good night take care")
                else:
                    speak("Have a good day")
                exit()

        except sr.UnknownValueError:
                speak("Couldn't catch that. Please repeat.")
                print("Couldn't catch that. Please repeat.")
                return None
        except sr.RequestError as e:
                speak("Could not request results; check your internet connection.")
                print("Could not request results; {0}".format(e))
                return None

    return None        
            

def handle_command(query):
    if query:
        if "how are you" in query:
            speak("I am absolutely fine")  

        elif 'mitra' in query:
            speak('yes')               

        elif "open" in query:
            query = query.replace("open", "").strip()
            webbrowser.open(f"https://{query}.com")
            speak(f"opening {query}")
            
                    
        elif "play" in query:
            songName = query.replace("play", "").strip()
            song(songName)

        elif "news" in query:
            webbrowser.open("https://www.google.com/search?q=news")  
            news = requests.get(f'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={newsApi}')
            data = news.json()
            if data.get('status') == 'ok':
                for article in data['articles']:
                    print(article['title'])
                    speak(article['title'])
            else:
                speak('failed to retrieve recent news')              

if __name__ == '__main__':
    while True:
        if not listening:
            trigger_word = take_command()
            if trigger_word:
                handle_command(trigger_word)
        else:
            query = take_command()
            handle_command(query)
            listening = False                

             

               

           
     
    #  processCommand(command)                           

                                                


    # except Exception as e:
    #     print("Error; {0}".format(e))

        
    