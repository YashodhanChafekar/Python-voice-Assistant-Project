# Import Module
from __future__ import print_function
import pyttsx3
import speech_recognition as sr
import datetime
import warnings
import playsound
import webbrowser
from selenium import webdriver
import subprocess
from fpdf import FPDF
from tkinter import *

# create root window
root = Tk()
color = "white"
# root window title and dimension
root.title("THEA")
# Set geometry (widthxheight)
root.geometry('800x400')
# Create a Label
lab = Label(text="I am Thea, your virtual assistant", font=("helvetica", 20), bg="white", fg="black")
lab.pack(pady=10)
dat = datetime.datetime.now()
dat = (dat.strftime("%H:%M:%S %b %d %Y"))
lab = Label(text=f"{dat}", font=("helvetica", 15), bg="white", fg="black")
lab.pack(pady=5)
# Create a function for voice assistant

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SCOPESgmail = ["https://www.googleapis.com/auth/gmail.readonly"]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = "I am THEA your virtual assistant. My name is inspired From character played by Angelina Jolie from movie eternals."
    speak(assname)
    speak("Please, press command button for instructions.")


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    print("Welcome Mr." + uname)

    speak("Please tap on command for instructions")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def note(text):
    speak("What should I name this file")
    name = takeCommand()
    file_name = name
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def pdfconv(filename):
    # save FPDF() class into
    # a variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # open the text file in read mode
    f = open(f"{filename}.txt", "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')

    # save the pdf with name .pdf
    pdf.output(f"{filename}.pdf")


def wish():
    wishMe()


def user():
    username()


def close():
    root.quit()
    exit()


def click():
    lab1 = Label(text="Listen", fg="black")
    lab1.pack()
    speak("I am Thea your virtual assistant. Waiting for Your Command")
    speak(f"Thea Reporting today, {dat}")
    while True:

        query = takeCommand().lower()
        if query == 'stop':  # To get back on main window where we have to again press button
            root.mainloop()
        elif 'google' in query:
            # speak("Here you go to Google\n")
            # webbrowser.open("google.com")
            speak("What would you like to search")
            search_string = takeCommand()
            search_string = search_string.replace(' ', '+')
            webbrowser.open(search_string)
        elif 'facebook' in query:
            speak("Here You Go\n")
            webbrowser.open("https://www.facebook.com")
        elif 'note' in query:
            speak("What would you like me to write down? ")
            write_down = takeCommand()
            write_down = "Date:" + " " + str(datetime.datetime.now()) + "\n" + write_down
            note(write_down)
            speak("I've made a note of that.")
        elif 'website' in query:
            speak("Which webpage you would like to visit. Please name it with .com")
            name = takeCommand()
            speak(f"Opening {name} for you ")
            webbrowser.open(f"https://www.{name}")
        elif 'question' in query:
            speak("What is it")
            search_string = takeCommand()
            speak("Directing you to related google search")
            search_string = search_string.replace(' ', '+')
            browser = webdriver.Chrome('chromedriver')
            for i in range(1):
                browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))
        elif ' video song' in query:
            webbrowser.open('https://www.youtube.com/watch?v=zdhKRTvua6Q')
        elif 'text to pdf' in query:
            try:
                speak("Please tell me filename")
                filename = takeCommand()
                pdfconv(filename)
                speak("Desired file is converted to pdf")
            except FileNotFoundError:
                speak("mentioned File does not exist")
        elif 'internet speed' in query:
            speak("Taking you to fast by Netflix")
            webbrowser.open('https://fast.com')
        elif 'cricket score' in query:
            speak("Showing you all cricket matches today")
            webbrowser.open(
                'https://www.google.com/search?q=cricket+score&rlz=1C1CHBF_enIN959IN959&oq=cricket&aqs=chrome.0.69i59j69i57j0i433i512j46i433i512j0i433i512j46i433i512j0i20i263i433i512j69i60.3108j1j7&sourceid=chrome&ie=UTF-8')
        elif 'youtube' in query:
            speak("What should I search")
            name = takeCommand()
            speak(f"Opening {name} for you")
            webbrowser.open(f"https://www.youtube.com/results?search_query={name}")
        elif 'sing me a song' in query:
            speak('''Feel your eyes, they all over me
                     Don't be shy, take control of me
                     Get the vibe, it's gonna be lit tonight
                     Baby girl, yuh a carry ten ton a phatness, gimme some a' dat
                     Pink sweetie badness, look how she hot
                     She a black like goddess, but a nah jus dat
                     It's a good piece 'a mentals under di cap
                     Hot piece of gear mami love how yuh chat
                     Watching every step 'a di pepper deh whe yuh got
                     Stayin' in ma brain, memberin' all the touch
                     Mainly my aim is to give you this love
                     Feel your eyes, they all over me
                     Don't be shy, take control of me''')
        elif 'visit earth' in query:
            webbrowser.open("https://earth.google.com/web/")
        elif 'shopping' in query:
            speak("Happy Shopping")
            webbrowser.open("https://www.amazon.com/")
        elif 'images' in query:
            speak("Tell me what you wish to see")
            search_string = takeCommand()
            search_string = search_string.replace(' ', '+')
            webbrowser.open(
                f"https://www.google.co.in/search?q={search_string}&hl=en&tbm=isch&sxsrf=AOaemvJXgjpF9nzxHdBqPIvlgDOjQANKPQ%3A1641905633035&source=hp&biw=1536&bih=714&ei=4X3dYawXis35Br-5rYgD&iflsig=ALs-wAMAAAAAYd2L8YDmvbC_U9U8b6PqGqNbZtWYh0Ex&ved=0ahUKEwjsi4qQ36n1AhWKZt4KHb9cCzEQ4dUDCAY&uact=5&oq=ms+dhoni&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIICAAQgAQQsQM6BwgjEO8DECc6CwgAEIAEELEDEIMBOggIABCxAxCDAToKCCMQ7wMQ6gIQJ1AAWPAfYPghaAJwAHgAgAGSAYgB_AmSAQQwLjEwmAEAoAEBqgELZ3dzLXdpei1pbWewAQo&sclient=img")
        elif 'weather' in query:
            webbrowser.open(
                "https://www.google.com/search?q=google+wether&rlz=1C1CHBF_enIN959IN959&oq=google+wether&aqs=chrome..69i57j0i10i131i433j0i10l2j0i10i433l2j0i10l4.3673j0j7&sourceid=chrome&ie=UTF-8")
        elif query == 'exit':
            speak("Thea exiting, goodbye")
            root.quit()  # To close app totally
            exit()
            break


# Create a button
btn = Button(text="Command", command=click, font=8, bg="black", fg="white", bd=2, relief="raised")
btn.pack(pady=10)
btn1 = Button(text="About Me", command=wish, font=8, bg="black", fg="white", bd=2, relief="raised")
btn1.pack(pady=10)
btn2 = Button(text="Introduce", command=user, font=8, bg="black", fg="white", bd=2, relief="raised")
btn2.pack(pady=10)
btn3 = Button(text="Close", command=close, font=8, bg="black", fg="white", bd=2, relief="raised")
btn3.pack(pady=10)

root.configure(bg=color)
# all widgets will be here
# Execute Tkinter
root.mainloop()
