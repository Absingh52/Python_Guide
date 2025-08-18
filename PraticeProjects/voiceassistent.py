import pyttsx3
engine=pyttsx3.init('sapi5')  ##SAPI5 HERE IS THE PREINSTALL VOICES IN THE MICROSOFT WINDOW 
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)     # I SET THIS PROPERTY FOR CONTROLLING SPEED OF THE  VOICE 
import os
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyaudio
import requests
import json

# CREATING FUNCTION FOR SPEAK MEANS IT CONVERT TEXT INTO SPECCH 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
# NOW FUNCTION FOR WISH
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")     
    speak(" jarvis at your service sir . How may i help you ?")    
    
# TAKE COMMAND FUNCTION WHICH IS USED TO CONVERT THE AUDIO INTO SPEDCH 

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
           
    try:   
        print("Recognizing......")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e :
        print("say that again please.")
        return "None"
    return query 
  # FUNCTION FOR WHEATER

def getWeather(city):
    api_key = "e3ea863a015a5bd13874d2d7ce582656"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(weather_url)
    weather = response.json()
    if weather["cod"] != "404":
        main = weather["main"]
        wind = weather["wind"]
        weather_desc = weather["weather"][0]["description"]
        temp = main["temp"]
        wind_speed = wind["speed"]
        speak(f"The weather in {city} is as follows:")
        speak(f"Temperature: {temp} degree Celsius")
        speak(f"Weather description: {weather_desc}")
        speak(f"Wind speed: {wind_speed} meter per second")

if __name__=="__main__"	:
    wishme()
    while True :
        query=takeCommand().lower()
        if 'wikipedia' in query :
            speak("Searching wikipedia....")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2) # WIKIPEDIA IS LIBRARY ,HERE IN RESULTS IT WILL PRINT THE SUMMARY OF THE QUERY IN TWO SENTENCES WE INCREASE SENTENCES LENGTH
            speak("According to wikipedia")
            print(results) # IT PRINT THE RESULTS ON THE SCREEN
            speak(results) # JARVIS SPEAKS THE RESULTS 
        elif 'open google' in query:
            speak("Opening google..")
            webbrowser.open("google.com")   
        elif 'open youtube' in query:
            speak("Opening youtube..")
            webbrowser.open("youtube.com")
        elif 'open vscode' in query :
            speak("Opening vs code..")
            codepath="C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")
        elif 'weather report' in query :
            speak("please tell me the city name")
            city=takeCommand()
            if city:
                getWeather(city)
        elif 'exit the program' in query:
            exit()
