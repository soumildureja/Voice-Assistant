 
import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import wikipedia as googleScrap
from playsound import playsound

engine=pyttsx3.init()

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


recognizer=sr.Recognizer()


def cmd():

    with sr.Microphone() as source:

        print("Clearing background noises...Please wait")

        recognizer.adjust_for_ambient_noise(source,duration=0.5)

        print('Ask me anything..')

        recordedaudio=recognizer.listen(source)

    try:

        text=recognizer.recognize_google(recordedaudio,language='en_US')

        text=text.lower()

        print('Your message:',format(text))



    except Exception as ex:
      print(ex)


    if 'chrome'in text:
       a='Opening chrome..'

       engine.say(a)

       engine.runAndWait()

       programName = "chrome.exe"

       subprocess.Popen([programName])

    if 'time' in text:

        time = datetime.datetime.now().strftime('%I:%M %p')

        print(time)

        engine.say(time)

        engine.runAndWait()

    if 'play' in text:

        a='opening youtube..'

        engine.say(a)

        engine.runAndWait()

        pywhatkit.playonyt(text)

    if 'youtube' in text:

        b='opening youtube'

        engine.say(b)

        engine.runAndWait()


        webbrowser.open('www.youtube.com')

    if 'who made you' in text:
        q= "I am made my Soumil Dureja"
        engine.say(q)
        engine.runAndWait()
        print(q)
    
    if 'google search' in text:
        q10= 'this is what i found on web'
        q11= 'no speakable data availabe'
        text = text.replace('google search', '')
        text= text.replace('google','')
        engine.say(q10)
        engine.runAndWait()
        pywhatkit.search(text)

        try:
            result = googleScrap.summary(text, 2)
            engine.say(result)
            engine.runAndWait()
        except:
            engine.say(q11)
            engine.runAndWait()
    
    if 'open amazon' in text:
        q2= 'opening amazon.com'
        engine.say(q2)
        engine.runAndWait()
        webbrowser.open('www.amazon.com')

    if 'how are you' in text:
        q3 = 'am fine'
        engine.say(q3)
        engine.runAndWait()
    
    if 'open discord' in text:
        q4= 'opening discord'
        engine.say(q4)
        engine.runAndWait()
        webbrowser.open('www.discord.com')
    
    if 'hello' in text:
        q5= 'hello there how can i help you, sir'
        engine.say(q5)
        engine.runAndWait()
    
    if 'open github' in text:
        q6= 'opening github'
        engine.say(q6)
        engine.runAndWait()
        webbrowser.open('www.github.com')
    
    if 'are you mad' in text:
        qa= 'Am just trying to help'
        engine.say(qa)
        engine.runAndWait()
    
    if 'open freelancer' in text:
        qb = 'opening freelancer'
        engine.say(qb)
        engine.runAndwait()
        webbrowser.open('www.freelancer.com')
    


while True:
   cmd()