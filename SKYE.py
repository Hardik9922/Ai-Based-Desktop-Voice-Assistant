import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia
import webbrowser
import pywhatkit as kit
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=9)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am SKYE sir. please tell me how can i help you")



if __name__ == "__main__":
    wish()
    #takecommand()
    #speak("hello sir")
    while True:
    #if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open epic games launcher" in query:
            epath = "D:\\PROG FILES\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(epath)

        elif "open code blocks" in query:
            cpath = "C:\\Program Files (x86)\\CodeBlocks\\CodeBlocks.exe"
            os.startfile(cpath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "close code blocks" in query:
            speak("okay sir, closing code blocls")
            os.system("taskkill /f /im codeblocks.exe")

        elif 'alarm' in query:
            speak("sir please tell me the time to set alarm.")
            tt = takecommand()
            tt = tt.replace("set alarm to", "")
            tt = tt.replace(".","")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        #elif "open youtube" in query:
            #speak("sir, what should i search on youtube")
            #cm = takecommand().lower()
            #webbrowser.open(f"{cm}")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open google" in query:
            speak("sir, what should i search on youtube")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open youtube" in query:
            speak("sir, what should i search on youtube")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
        speak("sir, do you have any other work")

