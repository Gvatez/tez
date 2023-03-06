import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import search_engine_parser as sep
import datetime
import pyjokes
import pandas as pd
import numpy as np

#input
contact_no=pd.read_excel("contacts.xlsx")
#contact_no=contact_no.applymap(str)
print(contact_no.head())

bot_name = ["alexa","jarvis","tez","tezi","texa"]
questions = ["who","what","say","about"]

listerner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',(voices)[1].id)

#pywhatkit.sendwhatmsg("+919488125365","This is a message",6,00)

def talk(text):
    engine.say(text)
    engine.runAndWait();

def take_command():
    try:

        with sr.Microphone() as source:
            var.set("Listening.....")
            voice = listerner.listen(source)
            command = listerner.recognize_google(voice)
            command = command.lower()
            #print(command)
            if 'jarvis' in command:
                #print(command)
                talk(command)
                command = command.replace('hey jarvis', ' ')
                #print(command)
    except:
        command = "raakh edukathada ena ethachi pesi tholadaw da de!!!"
    return command



def run_command():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", " ")
        #song = song.strip()
        print("playing..." + song)
        talk(song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I : %M %p')
        print(time)
        talk('current time is' + time)
    elif "who" in command:
        person = command.replace("who is", " ")
        print(person)
        info = pywhatkit.info(person,lines=2)
        print(info)
        talk(info)
    elif "are you single" in command:
        print("Im morattu single")
        talk("Im morattu single")
    elif "send" in command:
       if "at" in command:
           msg = command[command.index("send") + 5:command.index("at") - 1]
           print(msg)
           timimg_hour = int(command[command.index("at") + 3:command.index("at") + 5])
           timimg_min = int(command[command.index("at") + 5:])
           #phone_no =
           print(timimg_hour, timimg_min)
           message =  pywhatkit.sendwhatmsg("+919894110525", msg,timimg_hour,timimg_min)
           print(message)
       else:
           msg = command[command.index("send") + 5:]
           print(msg)
           new_time  = datetime.datetime.now()+datetime.timedelta(minutes = 1)
           print(new_time)
           timimg_hour = new_time.strftime('%H')
           timimg_min = new_time.strftime('%M')
           print(timimg_hour, timimg_min)
           message = pywhatkit.sendwhatmsg("+919894110525", msg, timimg_hour, timimg_min)
           print(message)
    elif "joke" in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif "google me" in command:
        searching = command.replace("google me", " ")
        searching = pywhatkit.search(searching)
        print("searching...")
        print(searching)
        talk(searching)
    else:
        #talk("raakh edukathada ena ethachi pesi tholadaw da de!!!")
        print("raakh edukathada ena ethachi pesi tholadaw da de!!!")

while(True):
    run_command()