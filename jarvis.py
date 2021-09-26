# from _typeshed import SupportsReadline
from os.path import splitext
from requests.models import get_cookie_header
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
#  import random
from requests import get
from urllib3.packages.six import with_metaclass
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import time
import requests, geocoder
import instaloader
import pytz
import PyPDF2

# Twittor Bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#  -
from wikipedia.wikipedia import page
import operator

# GUI
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUI import Ui_JarvisUI



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



# To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    c_time(hour)
    # speak("I am jarvis sir. please tell me how i can help you")

def c_time(h):
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    if h >=0 or h<12:
        speak(f"It is {current_time} AM")
    else:
        speak(f"It is {current_time} PM")

    # speak(f"It is {current_time}")
    speak("I am jarvis sir. please tell me how i can help you")

# To send Email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email', 'Password')
    server.sendmail('Your Email', to, content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=b6d2b3f298f74dfc83407b1bb99a4f98'
    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        #print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is:  {head[i]}")

# Twittor Bot
def account_info():
    with open('account_info.txt', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password

def pdf_reader():
    book = open('pdf2.pdf', 'rb') 
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in the this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

# GUI class
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        # self.TaskExecution()
        speak("please say wakeup to continue")
        while True:
            self.query = self.takecommand()
            if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
                self.TaskExecution()
            if "goodbye" in self.query or "good bye" in self.query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()
                
    # To convert voice into text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1, phrase_time_limit=7)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("say that again please...")
            return "none"
        query = query.lower()
        return query


    def TaskExecution(self):
        wish()
        while True:
            # if 1:
            self.query = self.takecommand().lower()

            # logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open adobe reader" in self.query:
                npath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
                os.startfile(npath)

            elif "open chrome" in self.query:
                npath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(npath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyWindow()

            elif "play music" in self.query:
                music_dir = "C:\\Users\\DELL\\Music"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in self.query:
                ip = get('http://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open instagram" in self.query:
                webbrowser.open("www.instagram.com")

            elif "open discord" in self.query:
                webbrowser.open("www.discord.com")

            elif "open stack overflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "sleep" in self.query:
                speak("ok sir, you can call me any time sir")
                break

            elif "send message" in self.query:
                speak("sir, what should i send message")
                cm = self.takecommand().lower()
                # kit.sendwhatmsg("+96560480702", "This is Testing protocol is ", hour, min )
                kit.sendwhatmsg("+96560480702", f"{cm}", 17, 53)

            elif "send email to burhan" in self.query:
                try:
                    speak("what should i say?")
                    content = self.takecommand().lower()
                    to = "Burhanuddinmarcha@gmai.com"
                    sendEmail(to, content)
                    speak("Email has been send to Burhan")

                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to sent this mail to Burhan")

            elif "play song on youtube" in self.query:
                speak("sir, which song i play on youtube")
                cm = self.takecommand().lower()
                kit.playonyt(f"{cm}")

            elif "no thanks" in self.query or "thank you" in self.query:
                speak("You're are welcome")
                

            # To close any application
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "close adobe reader" in self.query:
                speak("okay sir, closing adbe reader")
                os.system("taskkill /f /im AcroRd32.exe")

            # To set an alarm
            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                setalarm = float(input("Enter the alarm to set"))
                if nn == setalarm:
                    music_dir = "C:\\Users\\DELL\\Music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            # To find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("Please wait sir, feteching the latest news")
                news()

            elif "can you tweet" in self.query:
                speak("sir, what should i tweet")
                cmm = self.takecommand().lower()
                tweet = cmm
                email, password = account_info()
                options = Options()
                options.add_argument("start.maximized")
                driver = webdriver.Chrome(options=options)
                
                driver.get("http://twitter.com/login")

                email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
                password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
                login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div'

                time.sleep(2)

                driver.find_element_by_xpath(email_xpath).send_keys(email)
                # time.sleep(3)
                driver.find_element_by_xpath(password_xpath).send_keys(password)
                driver.find_element_by_xpath(login_xpath).click()

                tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
                message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
                post_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span'
    
                time.sleep(4)

                driver.find_element_by_xpath(tweet_xpath).click()
                driver.find_element_by_xpath(message_xpath).send_keys(tweet)
                driver.find_element_by_xpath(post_xpath).click()

                # os.system('python TwitterBot.py')
    
            # To find the location 
            elif "where i am" in self.query:
                ip = requests.get('http://api.ipify.org/').text
                location = geocoder.ip(ip)
                print(location.city, pytz.country_names[location.country])
                speak(f"sir i am not sure, but i think we are in {location.city} city of {pytz.country_names[location.country]} country")
            
            # To download Instagram Profile
            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name = self.takecommand().lower()
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile of this account.")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only = True)
                    speak("i am done sir, profile picture is saved in our main folder. now i am ready")
                else:
                    pass
            

            # Take Screenshot
            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("sir, please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("please sir hold the screen for few seconds, I am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I am done sir, the screenshot is saved in our main folder. Now i am ready for next command")

            elif "read pdf" in self.query:
                pdf_reader()

            elif "hide all file" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("sir, all the files in this folder are now hidden.")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("sir, all the files in this folder are now visible to everyone. I wish you are taking this decision in your own peace.")

                elif "leave it" in condition:
                    speak("ok sir")
           
            # To calculate mathematics
            elif "do some calculation" in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what  you want to calculate, example: 3 plus 3")
                    print("listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                try:
                    def get_operator_fn(op):
                        return {            
                            '+' : operator.add,
                            '-' : operator.sub,
                            'x' : operator.mul,
                            'divided' : operator.__truediv__,
                        }[op]
                    def eval_binary_expr(op1, oper, op2):
                        op1,op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    speak("your result is ")
                    speak(eval_binary_expr(*(my_string.split())))

                except:
                    speak("Wrong calcution given")
                    
                    
            elif "volume up" in self.query:
                pyautogui.press("volumeup")

            elif "volume down" in self.query:
                pyautogui.press("volumedown")

            elif "volume mute" in self.query:
                pyautogui.press("volumemute")


            elif "how are you" in self.query:
                speak("I am fine sir, what about you?")
                query = self.takecommand()
                if "fine" in query or "good" in query:
                    speak("that's great to hear from you")

            elif "where i am" in self.query:
                ip = requests.get('http://api.ipify.org/').text
                location = geocoder.ip(ip)
                print(location.city, pytz.country_names[location.country])
                speak(f"sir i am not sure, but i think we are in {location.city} city of {pytz.country_names[location.country]} country")

            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name = self.takecommand().lower()
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile of this account.")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only = True)
                    speak("i am done sir, profile picture is saved in our main folder. now i am ready")
                else:
                    pass
            
            elif "temperature" in self.query:
                from bs4 import BeautifulSoup
                # cmd = takecommand()
                search = self.query
                # search = "temperature in Banswara"
                url = f"http://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")

            elif "activate how to do mod" in self.query:
                from pywikihow import search_wikihow
                speak("How to do mode is activated please tell me what you want to know")
                how = self.takecommand()
                max_result = 1
                how_to = search_wikihow(how, max_result)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)

            elif "how much power left" in self.query or "how much power we have" in self.query or "battery" in self.query or "charge" in self.query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")

            elif "internet speed" in self.query or "internet" in self.query:
                import speedtest
                try:
                    os.system('cmd /k "speedtest"')
                except:
                    speak("there is no internet connection")

            

            
            
            # speak("sir, do you have any other work")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/DELL/Downloads/IR1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/DELL/Downloads/IR2.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(3000)
        startExecution.start()
        
    def showTime(self):

        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        lable_time = current_time.toString('hh:mm:ss')
        lable_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(lable_date)
        self.ui.textBrowser_2.setText(lable_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())

