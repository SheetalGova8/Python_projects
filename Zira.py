import pyttsx3  
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("good Evening!")
        
    speak("hello! sheetal Ma'am, i am Zira, please tell me how can i help you? ")
    
def refferal():
    # its take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        print('please Say that again..')
        return "None"
    return query
        
        
if __name__ == "__main__":
     wishMe()
     while 1:
         query = refferal().lower()
         
         if 'wikipedia' in query:
             speak('Searching Wikipedia....')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("according to wikipedia")
             print(results)
             speak(results)
             
         elif 'open youtube' in query:
             webbrowser.open("youtube.com")
             
         elif 'open google' in query:
            webbrowser.open("google.com")
            
        
    

