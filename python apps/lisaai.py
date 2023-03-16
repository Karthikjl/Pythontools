import speech_recognition as sr
import webbrowser
from time import ctime, sleep

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I can't get that.")
        except sr.RequestError:
            print("Sorry, server is down.")
        return voice_data
    
def respond(voice_data):
    if 'what is your name' in voice_data:
        print("Hi there, my name is lisa")
    if 'what is the time now' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q='+ search
        webbrowser.get().open(url)
        sleep(3)  
        print('Here is what i found for ' + search)

print("Hi, How can i help you!")
voice_data = record_audio()
respond(voice_data)
