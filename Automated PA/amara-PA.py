import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia    
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#print(voices)


def speak(audio):
    # speak whatever text is passed to it.

    engine.say(audio)
    engine.runAndWait()

def greetme():
    # Greet the user.

    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour < 12:
        speak("Good Morning!") 
    elif hour>=12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!") 
    speak("I am Amara, a personal assistant of Akshat, how can I help you?")


def takeCommand():
    # Listens to the user for spoken commands and returns strings.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration= 1)
        r.energy_threshold = 200
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
    
    except Exception as e:
        print(e)
        print("Say that again please ..")
        return "None"
    return query


if __name__ == "__main__":
    greetme()
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    while True:
        query = takeCommand().lower()

        #lookup Wikipedia
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia:")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
        
        elif 'open github' in query:
            webbrowser.get(chrome_path).open("https://github.com/Akshatt")
        
        elif 'inbox' in query:
            webbrowser.get(chrome_path).open("https://mail.google.com/mail/u/0/#inbox")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is: {strTime}")
        
        elif 'blue j' in query:
            filepath = "C:\\Program Files\\BlueJ\\BlueJ.exe"    
            os.startfile(filepath)

        elif 'bye' in query:
            speak("Goodbye, it was nice talking to you!")
            break
