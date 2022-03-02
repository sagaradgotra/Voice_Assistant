import pyttsx3
import datetime
import wikipedia
import requests
from bs4 import BeautifulSoup
import webbrowser as wb
import os

import speech_recognition as sr

import pywhatkit as kit

 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty(voices, voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening.....")
        #r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def play_on_youtube(video):
    kit.playonyt(video)



def search_on_google(query):
    kit.search(query)

def get_weather_report():
    res = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=jammu&appid=b0d8e1a2d31c2a92f411f10d6f3b764e").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


def play_audio(song_name):
    song_name = song_name.replace(' ', '%20')
    url = 'https://gaana.com/search/{}'.format(song_name)
    source_code = requests.get(url)
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text, "html.parser")
    links = soup.findAll('a', {'class': 'rt_arw'})
    wb.open(links[0]['href'])    


wishMe()


while True:
    query=takeCommand().lower()
    
    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        speak(results)
    elif 'open youtube' in query:
        wb.open("youtube.com")
    
    elif 'open google' in query:
        wb.open("google.com")
    
    elif 'open stackoverflow' in query:
        wb.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir= 'D:\\songs\\PUNJABI SONGS (1)' 
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0])) 
    
    
    elif 'play ganna' in query:
        son=takeCommand()
        play_audio(son)

    elif "the time" in query:
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(strtime)
    
    
    elif 'open code' in query:
        path="C:\\Users\\sagar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
    
    elif "play on youtube" in query:
        q="What should I play sir?"
        speak(q)
        video=takeCommand()
        play_on_youtube(video)
   
    
    elif "search google" in query:
        w="what should i search sir?"
        speak(w)
        search=takeCommand()
        search_on_google(search)
    
    elif "weather" in query:
        t=get_weather_report()
        speak(t);
    
    elif "close this application" in query:
        sp="which application sir?"
        speak(sp)
        r=takeCommand()
        os.close(r)
    
    
    elif "shut up" in query:
        exit
        


