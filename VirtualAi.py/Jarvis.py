# speech_recognition library=> use to convert the audio into text taken from input,use multiple engines(google,IBM etc)
import speech_recognition as sr
#  now text to audio => pyttsx3
import pyttsx3 

# webbrowser=> Use to open the urls and web apps in default web browser 
import webbrowser

# musicLibrary=>Use to Play files or songs ,basically perform crud operations(add,view,delete)
# import musicLibrary

# requests=> use to send the http requests like api (post,get) and manage the responses from web servers
import requests

# openAI=> Accesses OpenAi's API(like models of GPT)
import openai

# gTTTs=> convert text to audio ,plays and saves  output as MP3 files 
from gtts import gTTS

#  pygame=> use with gTTs(for playback of audio and video , game development and playing sound files )
import pygame

# os=> interacts with operating system

import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
# 🔹 Initialize pyttsx3 (offline TTS)

# weather
def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params ={
         "q":city,
         "appid":API_KEY,
         "units":"metric"
    }

    response=requests.get(base_url,params=params)

    if response.status_code ==200:
        data=response.json()
        temp=data["main"]["temp"]
        humidity=data["main"]["humidity"]
        desc=data["weather"][0]["description"]
        return f"The weather in {city} is {desc} with {temp}°C temperature and {humidity}% humidity."

    else:
        return "Sorry, I couldn't fetch the weather. Please check the city name."
# speak Offline 
def speak_offline(text):
    engine=pyttsx3.init()
    engine.setProperty("rate",150)  #speaking speed
    engine.setProperty("volume",1.0) #volume 
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# speak online
def speak_online(text,filename="voice.mp3"):
    tts=gTTS(text=text,lang="en")
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

# lets take input from user 

def take_command():
    r= sr.Recognizer()
    with sr.Microphone () as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1) # noise Handling
        try:
            audio=r.listen(source,timeout=5)
        except sr.WaitTimeoutError:
            print("Listening timed out. Try again...")
           
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-IN")
        print("You said:",query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry,I did not catch that.")
        return""
    except sr.RequestError:
        print("Speech service unavailable.")
        return""
    
def process_command(query):
    if "open google" in query :
        speak_offline("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in query :
        speak_offline("Opening you tube")
        webbrowser.open("https://youtube.com")

    elif "weather" in query or "weather of my location" in query or "today's weather" in query:

            words=query.split()
            if "in" in words or "of" in words:
                city_index=words.index("in")+1
                country_index=words.index("in")+1

                if city_index<len(words):
                    city=" ".join(words[city_index:])
                    report = get_weather(city)  
                    print(report)                # ✅ print in terminal
                    speak_offline(report)    
    elif "stop jarvis" in query or "exit" in query:
          speak_offline("Goodbye! Have a nice day.")
          exit()

if __name__=="__main__":
    speak_offline("Hello, I am Jarvis. How can i help you?")
    while True:
        query=take_command()
        if(query):
            process_command(query)