import speech_recognition as sr
import pyttsx3 as tts

r = sr.Recognizer()
engine = tts.init()


def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = r.listen(source)
        command = r.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            alexa_command = command.replace('alexa', '')
        else:
            alexa_command = "I didn't quite get that, can you say it again?"
    return alexa_command


def talk(command):
    engine.say(command)
    engine.runAndWait()



