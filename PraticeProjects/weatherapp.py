# import the libraries 
import requests
from tkinter import *
from tkinter import messagebox   #tkinter is used for making graphicak user interface 
import json
#function for get weather like city name and etc 


def get_weather(city):
    api_key='f58acc9aa8f3e7603e58875662564e2a'
    base_url='http://api.openweathermap.org/data/2.5/weather'
    params ={
        'q':city,
        'appid':api_key,
        'units':'metric'
    }
    response=requests.get(base_url,params=params)

    if response.status_code==200:
        data=response.json()
        city_name=data['name']
        country=data['sys']['country']
        temp=data['main']['temp']
        weather=data['weather'][0]['description']
        return f'{city_name},{country}\n Temperature:{temp}C\n Weather:{weather}'
    else:
        return 'city not found!'
    
#function for gui
def show_weather():
    city=city_entry.get()
    weather_info=get_weather(city)
    messagebox.showinfo('Weather information',weather_info)
    
    root=Tk
    root.title('Weather App')

    #CREATING FRAME FOR ROOT AND ROOT TITLE
    frame=Frame(root)
    frame.pack(pady=20)
    #CREATING ENTRY WHICH WILL  DISPLAY TEXT 
    city_entry=Entry(frame,width=30)
    city_entry.grid(row=0,column=0,padx=10)
    # MAKING GET WEATHER BUTTON 
    get_weather_button=Button(frame,text='Get Weather',command=show_weather())
    get_weather_button.grid(row=0,column=1)

    root.mainloop()