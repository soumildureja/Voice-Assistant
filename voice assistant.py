
import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import wikipedia

engine=pyttsx3.init()

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


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
    
    if 'wikipedia' in text:
        engine.say("Searching Wikipedia...")
        engine.runAndWait()
        word = input("What you wanna search for:")
        titles = wikipedia.search(word)
        print("These are the titles for your search: ",titles)
        index = int(input("Which title to show:"))
        try:
            results = wikipedia.summary(titles[index-1], sentences=2)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        engine.say("According to wikipedia")
        engine.runAndWait()
        print(results)
        engine.say(results)
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
        q5= 'hello there how can i help you'
        engine.say(q5)
        engine.runAndWait()
    
    if 'open github' in text:
        q6= 'opening github'
        engine.say(q6)
        engine.runAndWait()
        webbrowser.open('www.github.com')
    


while True:
   cmd()