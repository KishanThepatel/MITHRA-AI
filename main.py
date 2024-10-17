import http
import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def musicLibrary():
    songs = {
        "xxxsong":"spotifycodefotthecode"
    }


def playMusic():
    webbrowser.open(f"https://open.spotify.com/search/{""}")

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")   
    elif "open netflix" in c.lower():
        webbrowser.open("https://netflix.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")          
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")  

    #add your favorite songs to a musics urls to a 
    # separate py file and use that here
    elif "play" in c.lower():
       song = c.lower()
       playMusic()                
    

if __name__ == "__main__":
    speak("Initializing AI assistant")  
    
    print("Recognizing...")

    try:
        while True:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit=1)
            order = r.recognize_google(audio)
            if(order.lower() == "ai assistant"):
                speak("Yes")

                with sr.Microphone() as source:
                    print("AI Assistant Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)   

                                                


    except Exception as e:
        print("Error; {0}".format(e))


     
    