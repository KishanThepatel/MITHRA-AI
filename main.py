import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")  
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout = 2)  

    print("Recognizing...")
    

     
    