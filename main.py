import http
import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

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
              
    

if __name__ == "__main__":
    speak("Initializing mythrah")  
    
    print("Recognizing...")

    try:
        while True:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 5, phrase_time_limit=5)
            order = r.recognize_google(audio)
            if(order.lower() == "mitra"):
                speak("Yes")

                with sr.Microphone() as source:
                    print("MitraAI Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)   

                                                


    except Exception as e:
        print("Error; {0}".format(e))


     
    