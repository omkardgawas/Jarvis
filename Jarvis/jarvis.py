import pyttsx3
import pywhatkit
import pywhatkit as kit
import speech_recognition as sr
import datetime
from bs4 import BeautifulSoup
import time
import os
import cv2
import random
import wikipedia
import wikipedia as googlescrap
import pyaudio
import requests
from requests import get
import sys
import pyjokes
import pyautogui
import json
import webbrowser
import instaloader
import PyPDF2
import pytz
import speedtest
from playsound import playsound

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voice[0].id)
engine.setProperty('voice', voices[2].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# wish the user
def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour <= 12:
        speak("good morning")
    elif 12 < hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("i am jarvis, please tell me how can i help you")


def temp():
    search = "temperature in pune"
    url = f"http://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", "BNeawe").text
    speak(f"the temperature outside is {temperature}")


def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c547e42321434d619b63a1b2c9a372ef"
    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ",head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


def pdf_reader():
    book = open('E:\\3rd Year Seminar\\Smart Assistant.pdf', 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("sir enter the page number that i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)


def run():
    while True:
        permission = takecommand()
        if "wake up" in permission:
            taskexecution()
        elif "goodbye" in permission:
            sys.exit()


def setalarm():
    speak("Enter the time: ")
    t = input(": Enter the time :")

    while True:
        time_ac = datetime.datetime.now()
        now = time_ac.strftime("%H:%M:%S")
        if now == t:
            speak("Time to wake up sir!")
            speak("Time to wake up sir!")
            speak("Time to wake up sir!")
            speak("Time to wake up sir!")

        elif now > t:
            break


# speech to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query


def taskexecution():
    wish()
    while True:
        query = takecommand().lower()

        def speedTest():
            speak("checking speed.......")
            speed = speedtest.Speedtest()
            downloading = speed.download()
            correctDown = int(downloading / 800000)
            uploading = speed.upload()
            correctUp = int(uploading / 800000)

            if "uploading" in query:
                speak(f"the uploading speed is {correctUp} mbps")

            elif "downloading" in query:
                speak(f"the downloading speed is {correctDown} mbps")

            else:
                speak(f"the uploading speed is {correctUp} mbps and the downloading speed is {correctDown} mbps")

        # logic building tasks
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

            # to close the application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system('start cmd')

        elif "internet speed" in query:
            speedTest()

        elif "read pdf" in query:
            pdf_reader()

        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")

        elif "open camera" in query:
            cam = cv2.VideoCapture(0)
            while True:
                ret, img = cam.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cam.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold th screen for a few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder, now i am ready to do other tasks")

        elif "ip address" in query:
            ip = get('http://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "play song on youtube" in query:
            kit.playonyt("shape of you")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipadd = requests.get('http://api.ipify.org').text
                print(ipadd)
                url = 'http://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # print geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, due to some network issue i a not able to find where we are")
                pass

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif "google search" in query:
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            speak("this is what i found on the web")
            pywhatkit.search(query)

            try:
                result = googlescrap.summary(query, sentences=3)
                speak(result)

            except:
                speak("No data available, please check your internet connection")

        elif "set alarm" in query:
            setalarm()

        elif "temperature" in query:
            temp()

        elif "remember that" in query:
            remember_msg = query.replace("remember that", "")
            remember_msg = remember_msg.replace("jarvis", "")
            speak("You tell me to remind you that: " + remember_msg)
            remember = open('data.txt', 'w')
            remember.write(remember_msg)
            remember.close()

        elif "is there any reminder" in query:
            remember = open('data.txt', 'r')
            speak("you told me that" + remember.read())

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir, please enter the user name correctly.")
            name = input("Enter the username:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download the profile picture of this account?")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak(
                    "i am done sir, profile picture is saved in our main folder, now i am ready to do other tasks")
            else:
                pass

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powprof.dll,SetSuspendState 0,1,0")

        elif "you can sleep now" in query or "sleep now" in query:
            speak("okay sir, i am goind to sleep you can call me any time")
            break

        # only after sleep now command, goodbye command can get executed

        speak("sir, do you have any other work")
