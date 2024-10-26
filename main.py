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
r.energy_threshold = 300
engine.setProperty('rate', 195 )
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
USER = config('USER', default = 'Kishan')
HOSTNAME = config('BOT', default = 'mythhra')
newsApi = "386fb4f3ba594671b96b222e6121f072"
hugging_face_api = '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'
headers = {
    "Authorization": f"Bearer {hugging_face_api}"
}


def greet():
    hour = datetime.now().hour
    if(hour>=6 and hour<=12):
        speak(f"Good morning {USER}")
    elif(hour>=12 and hour<=16):
        speak(f"Good afternoon {USER}")
    elif(hour>=16 and hour<=19):
        speak(f"good evening {USER}")
    speak(f'{HOSTNAME} here, How may I assist you?') 

def query_huggingface(model: str, prompt: str):
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    payload = {"inputs": prompt}
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        print(f"Error {response.status_code}: {response.json()}")
        return None
    
def handle_user_query(user_query):
    response = query_huggingface("Flan-T5", user_query)
    if response:
        print("hey:", response)
        speak(response)  
    else:
        speak("I'm having trouble generating a response right now.")    


def speak(text):
    engine.say(text)
    engine.runAndWait()

def song(songName):
    webbrowser.open(f"https://www.youtube.com/results?search_query={songName}")

def take_command():
    global listening
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=4, phrase_time_limit=2)
 
        try:
            queri = r.recognize_google(audio, language='en-in').lower()

            if 'hey' in queri:
                listening = True
                print(f"Recognized: {queri}")
                queri = queri.replace('hey', "").strip()
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

        elif 'hey' in query:
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
        else:             
            response = query_huggingface("gpt2", query)
            if response:
                print("Assistant:", response)
                speak(response)
            else:
                speak("I'm having trouble generating a response right now.")                                               

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

        
    